"""Build taxonomy.csv: 195 ViMeLeaf class folders -> scientific names (GBIF-checked).

Run:  python build_taxonomy.py [--root E:\\ViMeLeaf_Dataset] [--refresh]
No randomness (no seed). Dataset is read-only (listdir + xlsx read only).

Inputs
  - E:\\ViMeLeaf_Dataset\\images\\** + _review\\** : folder (class) names, 195 unique
  - metadata/ViMeLeaf Dataset 80 Special.xlsx : STT -> Vietnamese name, scientific name, family
  - manual_map.csv : folder -> xlsx STT ('#N'), thesis row ('#NT'), literal name, or empty (unknown)
  - THESIS : scientific names from the thesis (docs/01. TOAN VAN LUAN VAN.pdf, Phu luc A, bang 12)
    for the rows the xlsx left blank / mislabelled
  - GBIF species/match (public, no key), cached in gbif_cache.json
POWO API returns HTTP 403 to scripted clients, so powo_id is not produced; gbif_key is used.
"""
import argparse, csv, json, re, time, urllib.parse, urllib.request
from collections import Counter
from pathlib import Path

import openpyxl

HERE = Path(__file__).parent
CACHE = HERE / "gbif_cache.json"
FIELDS = ["folder", "vietnamese_name", "scientific_name", "genus", "authorship", "family", "gbif_key",
          "gbif_accepted_name", "gbif_status", "match_status", "note", "name_source", "source_dirs"]

# thesis Phu luc A, bang 12 (STT -> scientific name as printed)
THESIS = {21: "Solanum procumbens Lour", 22: "Piper lolot C. DC",
          23: "Andrographis paniculata (Burm.f.) Nees", 70: "Uncaria sp. (Uncaria rhynchophylla)",
          71: "Allamanda cathartica L.", 72: "Boehmeria nivea", 73: "Stachytarpheta jamaicensis",
          74: "Costus speciosus Smith", 75: "Phyllanthus urinaria L.", 76: "Averrhoa carambola L.",
          77: "Clerodendrum japonicum (Thunb.) Sweet", 78: "Eurycoma longifolia",
          79: "Abelmoschus sagittifolius", 80: "Abrus precatorius L."}
# name as printed -> (name to query GBIF, why)
QUERY_FIX = {
    "Radix Fallopiae multiflorae": ("Fallopia multiflora", "tên dược liệu, truy vấn theo tên cây"),
    "Rhizoma Lasiae spinosae": ("Lasia spinosa", "tên dược liệu, truy vấn theo tên cây"),
    "Ludwigia prostrate": ("Ludwigia prostrata", "sửa chính tả epithet"),
    "Nelumbo nuciera Gaertn": ("Nelumbo nucifera", "sửa chính tả epithet"),
    "Alocazia odora (Roxb) C. Koch": ("Alocasia odora", "sửa chính tả chi (Alocazia -> Alocasia)"),
    "Cleistocalyx Operculatus": ("Cleistocalyx operculatus", "chuẩn hoá chữ hoa"),
    "Euphorbia tithymaloides subs. padifolia": ("Euphorbia tithymaloides", "bỏ phân loài"),
    "Cymbopogon spp": ("Cymbopogon", "chỉ tới chi"),
    "Uncaria sp. (Uncaria rhynchophylla)": ("Uncaria rhynchophylla", "luận văn ghi 'Uncaria sp.'"),
    "Pseuderanthemum palatiferum (Nees) Radlk": ("Pseuderanthemum palatiferum", ""),
}


def list_folders(root):
    root = Path(root)
    found = {}
    for sub in sorted((root / "images").iterdir()):
        for p in (sorted(sub.iterdir()) if sub.name == "raw" else [sub]):
            for d in sorted(x for x in p.iterdir() if x.is_dir()):
                found.setdefault(d.name, []).append(f"{sub.name}/{p.name}" if sub.name == "raw" else sub.name)
    for c in sorted((root / "_review").iterdir()):
        for d in sorted(x for x in c.iterdir() if x.is_dir()):
            found.setdefault(d.name, []).append(f"_review/{c.name}")
    return found


def load_xlsx(root):
    wb = openpyxl.load_workbook(Path(root) / "metadata" / "ViMeLeaf Dataset 80 Special.xlsx", read_only=True)
    return {r[0]: dict(vn=r[2], sci=(r[5] or "").strip(), fam=(r[6] or "").strip())
            for r in list(wb.active.iter_rows(values_only=True))[1:] if isinstance(r[0], int)}


def gbif(name, cache, refresh=False):
    if name in cache and not refresh:
        return cache[name]
    q = urllib.parse.urlencode({"name": name, "kingdom": "Plantae", "verbose": "true"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen("https://api.gbif.org/v1/species/match?" + q, timeout=30) as f:
                cache[name] = json.load(f)
            break
        except Exception as e:
            cache[name] = {"error": str(e)}
            time.sleep(2)
    time.sleep(0.2)
    return cache[name]


def best_hit(g, qname):
    """Top match; if only a higher rank came back, pick the alternative with the exact canonical name."""
    if g.get("matchType") in ("EXACT", "FUZZY") and g.get("rank") in ("SPECIES", "GENUS", "SUBSPECIES", "VARIETY"):
        return g
    cands = [a for a in g.get("alternatives", []) if a.get("canonicalName", "").lower() == qname.lower()]
    cands.sort(key=lambda a: a.get("status") != "ACCEPTED")
    if cands:
        return cands[0]
    return g if g.get("matchType") == "HIGHERRANK" and g.get("rank") == "GENUS" and " " not in qname else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"E:\ViMeLeaf_Dataset")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    folders = list_folders(a.root)
    xl = load_xlsx(a.root)
    mmap = {r["folder"]: r for r in csv.DictReader(open(HERE / "manual_map.csv", encoding="utf-8"))}
    assert set(mmap) == set(folders), (set(mmap) ^ set(folders))
    cache = json.load(open(CACHE, encoding="utf-8")) if CACHE.exists() else {}
    out = []
    for folder, dirs in sorted(folders.items()):
        m = mmap[folder]
        key, notes = m["key"].strip(), [m["note"]] if m["note"] else []
        row = dict.fromkeys(FIELDS, "")
        vn = re.sub(r"^\s*\d+\.\s*", "", folder)
        row.update(folder=folder, vietnamese_name=vn, source_dirs=";".join(dirs))
        sci, fam_x, src = "", "", ""
        if key.startswith("#") and key.endswith("T"):
            n = int(key[1:-1]); sci, src = THESIS[n], f"thesis#{n}"
        elif key.startswith("#"):
            n = int(key[1:]); r = xl[n]
            if r["sci"]:
                sci, fam_x, src = r["sci"], r["fam"], f"xlsx#{n}"
            else:
                sci, src = THESIS[n], f"thesis#{n}"
        elif key:
            sci, src = key, "manual-proposal"
        row["name_source"] = src
        status = m["status"]
        if not sci:
            row.update(match_status="unknown", note="; ".join(notes))
            out.append(row)
            continue
        if ";" in sci:
            notes.append(f"xlsx có nhiều tên: {sci}; lấy tên đầu")
            sci = sci.split(";")[0].strip()
        row["scientific_name"] = sci
        qname, why = QUERY_FIX.get(sci, (" ".join(sci.split()[:2]).replace("Persimilis", "persimilis"), ""))
        if why:
            notes.append(f"{why} ('{qname}')")
        toks = sci.split()
        row["genus"] = toks[0]
        row["authorship"] = " ".join(toks[2:]) if len(toks) > 2 and toks[1].islower() else ""
        g = None
        if not why and len(toks) > 2 and toks[1].islower():  # try with authorship first (disambiguates homonyms)
            g = best_hit(gbif(re.sub(r"[.,]+$", "", " ".join(toks)), cache, a.refresh), qname)
            if g and g.get("canonicalName", "").lower() != qname.lower():
                g = None
        g = g or best_hit(gbif(qname, cache, a.refresh), qname)
        if g:
            row["gbif_key"] = g.get("acceptedUsageKey") or g["usageKey"]
            row["gbif_status"] = g.get("status", "")
            row["family"] = g.get("family", "")
            row["gbif_accepted_name"] = (g.get("species") or g.get("canonicalName", "")) if g.get("status") == "SYNONYM" else g.get("canonicalName", "")
            if g.get("status") == "SYNONYM":
                notes.append(f"GBIF: '{qname}' là synonym của {row['gbif_accepted_name']}")
            if g.get("matchType") == "FUZZY":
                notes.append("GBIF khớp mờ"); status = "fuzzy" if status == "exact" else status
            fx = re.search(r"\(([A-Za-z]+)", fam_x)
            if fx and fx.group(1).lower() != row["family"].lower():
                notes.append(f"họ xlsx={fx.group(1)} khác GBIF={row['family']}")
            if " " not in qname:
                status = "ambiguous"; notes.append("chỉ xác định tới chi")
        else:
            notes.append("GBIF không khớp")
            if status == "exact":
                status = "ambiguous"
            fx = re.search(r"\(([A-Za-z]+)", fam_x)
            row["family"] = fx.group(1) if fx else ""
        row.update(match_status=status, note="; ".join(n for n in notes if n))
        out.append(row)
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    with open(HERE / "taxonomy.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, FIELDS); w.writeheader(); w.writerows(out)
    print(len(out), "folders;", dict(Counter(r["match_status"] for r in out)))


if __name__ == "__main__":
    main()

