#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""RES-46 Audit: sample 20 rows taxonomy.csv vs POWO/GBIF"""

import csv
import sys

# Read taxonomy.csv
with open('units/research/experiments/vimeleaf/taxonomy.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Sample rows 2-21 (1-indexed = rows[1:21] in 0-indexed)
sample = rows[1:21]

print('=== TAXONOMY SAMPLE AUDIT (20 rows, positions 2-21) ===\n')

issues = []
pass_count = 0

for i, row in enumerate(sample, start=2):
    vi_name = row.get('vietnamese_name', '').strip()
    sci_name = row.get('scientific_name', '').strip()
    gbif_accepted = row.get('gbif_accepted_name', '').strip()
    gbif_status = row.get('gbif_status', '').strip()
    match_status = row.get('match_status', '').strip()
    source = row.get('source_dirs', '').strip()
    
    print(f"Row {i}: {vi_name}")
    print(f"  Scientific: {sci_name}")
    print(f"  GBIF Accepted: {gbif_accepted}")
    print(f"  GBIF Status: {gbif_status} | Match: {match_status}")
    print(f"  Source: {source}")
    
    # Check for issues
    if not sci_name:
        issues.append(f"Row {i}: missing scientific name ({vi_name})")
    elif gbif_status not in ['ACCEPTED', 'SYNONYM', '']:
        issues.append(f"Row {i}: unexpected GBIF status '{gbif_status}' ({vi_name})")
    elif match_status == 'unknown':
        issues.append(f"Row {i}: unidentified species ({vi_name})")
    elif match_status not in ['exact', 'fuzzy', 'ambiguous', '']:
        issues.append(f"Row {i}: unclear match_status '{match_status}' ({vi_name})")
    else:
        pass_count += 1
    
    print()

print(f"\n=== SUMMARY ===")
print(f"Total rows sampled: {len(sample)}")
print(f"Pass (identified): {pass_count}")
print(f"Issues found: {len(issues)}")

if issues:
    print(f"\nIssue list:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("No issues in sample.")

# Check supplement exclusion
supplement_rows = [r for r in rows if 'supplement' in r.get('source_dirs', '').lower()]
print(f"\nSupplement rows (should be excluded from publication):")
print(f"  Total supplement rows: {len(supplement_rows)}")
print(f"  Example: {supplement_rows[0]['vietnamese_name'] if supplement_rows else 'None'}")

sys.exit(0 if not issues else 1)
