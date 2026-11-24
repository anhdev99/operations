# operations

Nơi điều hành công việc ở 4 nơi: giảng dạy đại học, tổ chuyển đổi số, PHD Group, LucidTech.
Kế hoạch đầy đủ: `docs/2026-11-03-plan-four-roles-operations/index.html`.

## Luật bắt buộc

1. **Chỉ đọc mặc định.** Không tạo/sửa/xoá gì ở OpenProject, Kimai, GitHub, Slack khi chưa được xác nhận.
   Soạn nháp rồi hỏi trước (tạo ticket dùng skill `openproject-ticket`).
   Ngoại lệ đã được cho phép (2026-11-24): comment review PR trên GitHub được tự đăng theo mẫu cố định;
   approve và request changes vẫn phải chờ bạn đồng ý từng PR.
2. **Không trộn dữ liệu giữa các nơi.** Mỗi nơi một thư mục trong `units/`. Làm việc sâu ở nơi nào thì
   chỉ đọc `units/<nơi>/`. Bản tóm tắt chung (`shared/`) chỉ chứa tiêu đề, hạn và link.
3. **Token chỉ nằm ở `~/.claude/<nơi>.env`** (chmod 600). Không ghi token vào repo, log, chat hay commit.
4. Snapshot (`units/*/snapshot/`) và `shared/morning-brief.html` nằm ngoài git.
5. **Nhánh và merge (2026-11-24).** Mọi project đều có nhánh `develop`. Agent tách nhánh `agent/<mã-issue>` từ `develop`,
   mở PR nhắm vào `develop` và dừng; **không agent nào được merge** vào `develop`, `main`, `master`. Chỉ chủ sở hữu merge
   và phát hành `develop` sang `main`. Có PR của agent thì `scripts/pr_watch.py` báo Slack kênh của công ty đó.
   Việc của chính repo này cũng đi qua PR vào `develop`.

## Cấu trúc

- `units/<role>/sources.json` — nguồn dữ liệu của từng nơi (không chứa token).
- `units/<role>/CLAUDE.md` — ngữ cảnh riêng của nơi đó.
- `teaching/` — giảng dạy, không có hệ thống nguồn.
- `scripts/` — script đọc: `python3 scripts/op_read.py <role>`, `python3 scripts/github_read.py [<role>]`.
- `scripts/pr_watch.py` — theo dõi PR cần review và PR do agent mở (chạy mỗi 10 phút qua Paperclip); `pr_fetch.py`, `pr_file.py` đọc PR;
  `pr_act.py` ghi comment/approve (approve cần bạn đồng ý). `pc_task.py` tạo và xem ticket Paperclip qua REST (CLI Windows cắt mô tả nhiều dòng).
- `.claude/skills/morning-brief/` — tóm tắt sáng.

## Thêm hoặc đổi nguồn của một nơi

Mỗi nơi một tệp env duy nhất, đã tạo sẵn (mẫu để trống) ở `~/.claude/`:
`digital-transformation.env`, `phd-group.env`, `lucidtech.env`. Trong đó có `OP_BASE_URL`/`OP_TOKEN`,
`KIMAI_BASE_URL`/`KIMAI_TOKEN`, `SLACK_TOKEN`. Điền giá trị vào đó (không đưa token vào repo hay chat), rồi:

```bash
python3 scripts/check_setup.py     # xem nguồn nào đã điền và chạy được; không in token
```

GitHub không cần token (dùng `gh`); chỉ cần owner trong `sources.json` → `github.owners`.
Giới hạn OpenProject theo project bằng `openproject.projects`; để trống thì lấy mọi project bạn tham gia.

## Quy ước

- Nội dung tiếng Việt; tên tệp và code tiếng Anh. Commit message tiếng Anh, không gắn attribution.
- Commit theo tính năng, không commit từng bước.
