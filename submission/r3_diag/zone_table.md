# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 9 | 2 | 1 | 2 | 3 | WRONG_CLASS (1) |
| mid | 7 | 3 | 0 | 3 | 4 | MISSING (3) |
| edge | 4 | 2 | 0 | 4 | 3 | MISSING (2) |

## Nhận xét

- **Zone người (L) và model (M) gãy nhiều nhất:**
  - Đối với người gán nhãn (L): Gãy nhiều nhất về số lượng tuyệt đối ở zone `mid` (3 missing) và tỷ lệ cao nhất ở zone `edge` (2/4 = 50% missing). Lỗi chủ đạo là `MISSING`.
  - Đối với model (M): Gãy nghiêm trọng nhất ở zone `edge`, bỏ sót 4/4 (100% missing) và có 3 box thừa; ở zone `mid` cũng bỏ sót 3 vật và sinh 4 box thừa.
- **Giả thuyết nguyên nhân và giới hạn mẫu:**
  - *Nguyên nhân model gãy:* Model YOLO26m đóng băng vốn được tiền huấn luyện trên ảnh phối cảnh phẳng (pinhole). Khi gặp ảnh fisheye với méo cong phi tuyến cực mạnh ở rìa (`edge` $r/R \ge 0.6$), đặc trưng hình học của vật thể bị biến dạng méo mó, dẫn đến model không nhận diện được (FN) hoặc bắt nhầm các cấu trúc nền thành vật thể (FP).
  - *Nguyên nhân người gán nhãn gãy:* Ở vùng `mid` và `edge`, các phương tiện nhỏ dần và bị che khuất một phần trong dòng giao thông đông đúc (`dense`), khiến người gán nhãn dễ bỏ sót các xe đạt ngưỡng chiều cao $H \ge 40\text{px}$.
  - *Giới hạn:* Slice chỉ gồm 3 frame với tổng cộng 20 đối tượng tham chiếu ($n_{ref}=20$), cỡ mẫu nhỏ nên các con số phản ánh xu hướng thử nghiệm trong bài lab, chưa đủ để khái quát hóa toàn bộ phân phối dữ liệu vận hành thực tế.
