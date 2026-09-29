# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| `adasind_199770.jpg` (zone `edge`) | 5 ca MISSING, 1 ca ATTRIBUTE | Vùng rìa ngoài cùng có độ méo quang học thấu kính fisheye cực đại; tỷ lệ bỏ sót vật thể cao nhất (Model missing 100%, annotator sót nhiều xe nhỏ). Đây là vùng điểm mù dễ va chạm khi xe chuyển làn. | File XML so sánh L/R/M, overlay `model_compare.html`, crop ảnh phóng to vùng rìa trái $x=0$. |
| `adasind_167700.jpg` (zone `mid` / `dense`) | 4 ca MISSING, 1 ca WRONG_CLASS | Mật độ giao thông hỗn hợp dày đặc với nhiều loại phương tiện đặc thù (ThreeWheeler đi sát Bike và Car), nguy cơ nhầm lẫn class và bỏ sót xe che khuất cao. | Bảng `local_quality_confusion.csv`, `qa_overlay.html`, ảnh đối chiếu box L vs R. |

**Giới hạn của kết luận từ ba frame ADASIND:** Ba frame chỉ thuộc một camera fisheye đơn gắn trước trong một đoạn hành trình ngắn ban ngày, không đại diện cho sự biến thiên môi trường (đêm, ngược sáng, trời mưa) cũng như đặc tính góc nhìn của 3 camera còn lại quanh xe (Rear, Left, Right).

## Chuyển sang kế hoạch bốn camera giả lập

**Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv` và giới hạn suy luận:**
- *Cách soát độ phủ:* Áp dụng lấy mẫu phân tầng theo camera và độ khó (`front/rear/left/right × normal/hard`). Để tránh lấy trùng lặp các frame liên tiếp trong cùng một chuỗi thời gian (temporal redundancy), cần áp dụng ngưỡng lọc bước nhảy thời gian (keyframe interval tối thiểu 2–3 giây giữa các frame).
- *Giới hạn suy luận tỷ lệ lỗi:* Kế hoạch 200 frame là tập mẫu có chủ đích tập trung vào các ca khó, ca góc (corner cases / edge cases) để phát hiện lỗ hổng guideline và lỗi mô hình. Do không tuân theo phân phối ngẫu nhiên độc lập (i.i.d), tỷ lệ lỗi quan sát được trên tập này không thể quy đổi trực tiếp thành tỷ lệ lỗi hệ thống (systemic failure rate) của 50.000 frame.
