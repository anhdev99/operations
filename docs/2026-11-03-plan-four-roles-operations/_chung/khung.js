/*
 * Dựng sidebar trái cho tài liệu HTML nhiều trang.
 *
 * Đọc danh sách trang từ window.TAI_LIEU (file muc-luc.js), rồi:
 *   - vẽ tên tài liệu + danh sách trang, đánh dấu trang đang mở;
 *   - dưới trang đang mở, liệt kê các mục trong trang (h2[id] và [data-muc][id]);
 *   - tô mục đang đọc khi cuộn; thêm nút Trang trước / Trang sau ở cuối nội dung;
 *   - màn hẹp: sidebar gập thành thanh trên cùng, bấm "Mục lục" để mở.
 *
 * Chạy được khi mở thẳng file (file://) — không fetch, không module, không thư viện.
 * KHÔNG sửa file này cho riêng một tài liệu. Thêm trang = sửa muc-luc.js.
 * Nguồn gốc: skill tai-lieu-html (~/.claude/skills/tai-lieu-html/mau/_chung/khung.js).
 */
(function () {
  "use strict";

  var TL = window.TAI_LIEU;
  var ben = document.querySelector("[data-khung-ben]");
  var noiDung = document.querySelector("[data-khung-noi-dung]");
  if (!TL || !ben || !noiDung) return;

  var hienTai = decodeURIComponent(location.pathname.split("/").pop() || "") || "index.html";

  function tao(the, lop, chu) {
    var el = document.createElement(the);
    if (lop) el.className = lop;
    if (chu != null) el.textContent = chu;
    return el;
  }

  // ── Đầu sidebar ────────────────────────────────────────────────
  var dau = tao("div", "ben__dau");
  var dauChu = tao("div", "ben__dau-chu");
  var ten = tao("a", "ben__ten", TL.ten || "Tài liệu");
  ten.href = "index.html";
  dauChu.appendChild(ten);
  if (TL.phu) dauChu.appendChild(tao("p", "ben__phu", TL.phu));
  dau.appendChild(dauChu);

  var nut = tao("button", "ben__nut", "Mục lục");
  nut.type = "button";
  nut.setAttribute("aria-expanded", "false");
  nut.setAttribute("aria-controls", "ben-dieu-huong");
  nut.addEventListener("click", function () {
    var mo = ben.classList.toggle("ben--mo");
    nut.setAttribute("aria-expanded", String(mo));
  });
  dau.appendChild(nut);

  // ── Danh sách trang ────────────────────────────────────────────
  var nav = tao("nav", "ben__dieu-huong");
  nav.id = "ben-dieu-huong";
  nav.setAttribute("aria-label", "Mục lục tài liệu");

  var dsTrang = [];
  var lienKetMuc = [];

  (TL.trang || []).forEach(function (muc) {
    if (muc.nhom) {
      nav.appendChild(tao("p", "ben__nhom", muc.nhom));
      return;
    }
    dsTrang.push(muc);
    var a = tao("a", "ben__muc", muc.ten);
    a.href = muc.tep;
    nav.appendChild(a);

    if (muc.tep !== hienTai) return;
    a.classList.add("ben__muc--on");
    a.setAttribute("aria-current", "page");

    var dauMuc = noiDung.querySelectorAll("h2[id], [data-muc][id]");
    if (!dauMuc.length) return;
    var ul = tao("ul", "ben__con");
    Array.prototype.forEach.call(dauMuc, function (el) {
      var li = tao("li", el.hasAttribute("data-muc") ? "ben__con-phu" : "");
      var link = tao("a", "", (el.getAttribute("data-muc") || el.textContent).trim());
      link.href = "#" + el.id;
      li.appendChild(link);
      ul.appendChild(li);
      lienKetMuc.push({ el: el, a: link });
    });
    nav.appendChild(ul);
  });

  // Bấm một mục trên màn hẹp thì gập mục lục lại để thấy nội dung.
  nav.addEventListener("click", function (e) {
    if (e.target.tagName === "A" && ben.classList.contains("ben--mo")) {
      ben.classList.remove("ben--mo");
      nut.setAttribute("aria-expanded", "false");
    }
  });

  ben.textContent = "";
  ben.appendChild(dau);
  ben.appendChild(nav);

  // ── Tô mục đang đọc ────────────────────────────────────────────
  if (lienKetMuc.length && "IntersectionObserver" in window) {
    var dangXem = null;
    var quan = new IntersectionObserver(function (ds) {
      ds.forEach(function (m) {
        if (!m.isIntersecting) return;
        var tim = lienKetMuc.filter(function (x) { return x.el === m.target; })[0];
        if (!tim) return;
        if (dangXem) dangXem.classList.remove("dang-xem");
        tim.a.classList.add("dang-xem");
        dangXem = tim.a;
      });
    }, { rootMargin: "0px 0px -70% 0px" });
    lienKetMuc.forEach(function (x) { quan.observe(x.el); });
  }

  // ── Trang trước / sau ──────────────────────────────────────────
  var viTri = -1;
  dsTrang.forEach(function (m, i) { if (m.tep === hienTai) viTri = i; });
  if (viTri !== -1 && dsTrang.length > 1) {
    var chan = tao("nav", "chuyen-trang");
    chan.setAttribute("aria-label", "Chuyển trang");
    var oChuyen = function (m, lop, nhan) {
      var a = tao("a", lop);
      a.href = m.tep;
      a.appendChild(tao("span", "", nhan));
      a.appendChild(tao("b", "", m.ten));
      return a;
    };
    if (viTri > 0) chan.appendChild(oChuyen(dsTrang[viTri - 1], "truoc", "← Trang trước"));
    if (viTri < dsTrang.length - 1) chan.appendChild(oChuyen(dsTrang[viTri + 1], "sau", "Trang sau →"));
    (noiDung.querySelector(".trong") || noiDung).appendChild(chan);
  }
})();
