# Đề xuất gold set theo camera — tình huống giả lập

**Đầu bài:** 50.000 frame từ bốn camera SVM, ngân sách chọn 200 frame để review/gold. Đây là tình huống trên slide,
**không phải** 50.000 frame có trong repo. Phân bổ đúng 200 ở `45_sampling_plan.csv` cho bốn camera, mỗi camera có
normal và hard slice. “Gold set” ở đây là **kế hoạch tạo** reference sau kiểm chứng, không phải teaching reference
ADASIND hoặc nhãn bạn vừa vẽ. Nếu cần, dùng `notebooks/day11-svm360-colab.ipynb` để thử tổng phân bổ; notebook
không làm thay phần lý do.

| camera_id | Hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Ngược sáng lúc hoàng hôn/bình minh, trời mưa ướt thấu kính, người đi bộ cắt ngang sát đầu xe ($< 5\text{m}$). | Chói lóa làm mất biên dạng viền, giọt nước gây méo cục bộ, mật độ che khuất phức tạp. | Tọa độ ảnh fisheye 2D gốc kèm ma trận hiệu chuẩn nội suy/ngoại suy (intrinsics/extrinsics) chuẩn xác. | Hai reviewer độc lập gán nhãn mù (dual blind), tính độ khớp IoU $\ge 0.85$; nếu lệch thì Senior QA phân xử trên chuỗi frame. |
| rear | Đèn pha xe sau chiếu lóa vào ban đêm, bụi bẩn/bùn bám mặt kính, vật cản thấp sát cản sau ($< 1\text{m}$). | Lóa sáng (halo/flare) xóa nhòa ranh giới xe, điểm mù tầm thấp khó ước lượng khoảng cách. | Giữ nguyên hệ tọa độ camera sau kết hợp mặt phẳng mặt đường (ground plane homography). | Đối chiếu với cảm biến siêu âm / radar lùi hoặc đám mây điểm LiDAR đồng bộ thời gian. |
| left | Xe hai bánh luồn lách sát sườn xe, phương tiện vắt ngang vùng chồng lấn góc trước-trái (seam front-left). | Độ méo cực đại ở rìa thấu kính, một phần xe nằm ở camera trước và một phần nằm ở camera trái với góc xoay khác nhau. | Calibration đồng bộ thời gian (hardware timestamp sync) giữa camera trước và camera trái. | Mở đồng thời cả 2 ảnh front và left tại cùng timestamp, kiểm tra tính nhất quán hình học trước khi duyệt nhãn. |
| right | Đậu xe sát vỉa hè có cây cối bóng đổ đan xen, người đi bộ bước từ vỉa hè xuống lòng đường ở góc khuất cột B/C. | Kết cấu lề đường phức tạp dễ lẫn viền, bóng cây gây ra hiện tượng nhận diện giả (false positive). | Giữ nguyên polygon mask vùng mù thân xe bên phải (`ego_body`) và thông số méo góc rộng. | Soát độc lập 2 vòng, đối chiếu với chuỗi video 5 frame trước và sau để xác nhận chuyển động. |

- **Khi nào cần refresh gold set (đổi camera, calibration hoặc rule):**
  1. Khi nâng cấp hoặc thay đổi phần cứng cảm biến (thay đổi độ phân giải, FOV hoặc loại ống kính fisheye).
  2. Khi hiệu chuẩn vị trí camera (extrinsic calibration) bị xê dịch sau va chạm, bảo dưỡng hoặc rung lắc cơ học kéo dài.
  3. Khi guideline gán nhãn được cập nhật phiên bản mới (ví dụ ban hành rule R12 bổ sung ngưỡng mép rìa hoặc tách class mới).
  4. Định kỳ kiểm tra phát hiện hiện tượng trôi dạt dữ liệu (data drift) do thay đổi mùa/thời tiết.
- **Một ca seam/cross-camera cần policy và evidence trước khi ghép hai box:**
  - *Tình huống:* Một chiếc xe máy đi sát sườn xe ego tại vùng góc trước-trái, xuất hiện đồng thời trên cả camera Front (nửa đuôi xe ở rìa phải ảnh) và camera Left (nửa đầu xe ở rìa trái ảnh).
  - *Policy cần có:* Quy định rõ tầng Perception sẽ xuất 2 box 2D độc lập trên từng camera rồi để tầng Sensor Fusion / Tracking 3D gộp lại, hay buộc annotator phải ghép thành 1 đối tượng duy nhất trên ảnh BEV.
  - *Evidence cần có:* Timestamp đồng bộ phần cứng ở mức mili-giây, ma trận extrinsic chính xác giữa 2 camera và kiểm tra giao thoa hình học 3D trên mặt đất để chứng minh hai hình chiếu 2D thuộc về cùng một thực thể vật lý duy nhất.
- **Vì sao peer agreement hoặc quality report trên ảnh một camera chưa chứng minh gold set đúng cho cả bốn camera:**
  - Báo cáo chất lượng trên 1 camera (như tập ADASIND) chỉ đo độ khớp cục bộ trong một góc nhìn đơn lẻ. Nó hoàn toàn bỏ qua các sai số hệ thống cốt lõi của SVM 360°: sự lệch pha timestamp giữa các camera, hiện tượng đứt gãy hình ảnh tại 4 đường nối seam, sự chênh lệch phơi sáng giữa các hướng (ví dụ hướng trước chói nắng nhưng hướng sau bóng râm), và tính nhất quán 3D khi hợp nhất sang Bird's-Eye View (BEV). Vì vậy, kết quả tốt trên 1 camera không thể bảo chứng cho chất lượng Gold Set của toàn bộ hệ thống 4 camera.
