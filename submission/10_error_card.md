# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B3 | MISSING | 5 |
| center | B3 | SPURIOUS | 4 |
| center | B3 | WRONG_CLASS | 1 |
| center | C0 | SPURIOUS | 1 |
| center | C0 | WRONG_CLASS | 1 |
| edge | B3 | ATTRIBUTE | 2 |
| edge | B3 | IGNORE_SCOPE | 1 |
| edge | B3 | MISSING | 6 |
| edge | B3 | SPURIOUS | 3 |
| edge | C0 | WRONG_CLASS | 1 |
| mid | B3 | IGNORE_SCOPE | 3 |
| mid | B3 | MISSING | 8 |
| mid | B3 | SPURIOUS | 4 |
| mid | C0 | WRONG_CLASS | 1 |
| unknown | B3 | IGNORE_SCOPE | 1 |

## Top defects
- MISSING: 19 (ví dụ frame adasind_167700.jpg)
- SPURIOUS: 12 (ví dụ frame adasind_019560.jpg)
- IGNORE_SCOPE: 5 (ví dụ frame adasind_145860.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- **Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy:**
  - Lỗi nổi bật nhất là `MISSING` (19 ca) và `SPURIOUS` (12 ca), tập trung chủ yếu ở hai zone `mid` và `edge` của block B3 (`B3-dense`).
  - *Đối với Model (`why = E4_model_domain`):* Mô hình YOLO26m được huấn luyện trên miền ảnh phối cảnh thông thường (pinhole), khi áp dụng trực tiếp lên camera fisheye góc siêu rộng, độ biến dạng hình học phi tuyến ở rìa ($r/R \ge 0.6$) làm biến đổi hoàn toàn tỷ lệ khung hình và đặc trưng biên của phương tiện, khiến model bỏ sót hầu hết vật thể ở rìa và nhận nhầm các vệt sáng / kết cấu mặt đường thành box ảo.
  - *Đối với Người gán nhãn (`why = E1_annotator_error`):* Trong cảnh giao thông mật độ cao (`B3-dense`), các phương tiện ở vùng mid/edge bị che khuất một phần (occluded) và kích thước thu nhỏ, khiến annotator mắt thường dễ bỏ sót các đối tượng vẫn thỏa mãn ngưỡng chiều cao $H \ge 40\text{px}$.
- **Cách sửa và ai nhận việc (`owner`):**
  - *Annotator (`owner = annotator`):* Cần zoom ảnh ở mức 150%–200% khi quét qua vùng `mid` và `edge`, kiểm tra kỹ các phương tiện bị che khuất và dùng công cụ đo kích thước trên CVAT để không bỏ sót các xe $H \ge 40\text{px}$.
  - *AI Team (`owner = ai_team`):* Cần bổ sung tập dữ liệu huấn luyện đặc thù cho camera fisheye, áp dụng data augmentation mô phỏng méo vành kính hoặc tiền xử lý nắn phẳng cục bộ trước khi đưa vào mạng nơ-ron phát hiện vật thể.
- **Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule):**
  - Dòng findings: `adasind_167700.jpg` (`R2+M7`, `R4+M4`, `R8+M9` đều bị MISSING theo R01), `adasind_199770.jpg` (`R3+M10`, `R4`, `R5`, `R6` bị MISSING).
  - Ảnh minh chứng: `submission/screenshots/edge_distortion_missing.png` (thể hiện hiện tượng méo quang học cực mạnh ở rìa khung hình khiến việc phát hiện box gặp khó khăn).
