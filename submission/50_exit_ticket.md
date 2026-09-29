# Exit ticket

Đọc `docs/10-svm360-reading-vi.md` trước khi trả lời câu 1–2. Các câu về zone, `why`, rework, parking và sampling
đã nằm trong file tương ứng nên không hỏi lại ở đây.

1. **Một vật ở vùng seam giữa hai camera thật xuất hiện với hai box khác nhau: đó là lỗi `DUPLICATE` hay cần một quy tắc riêng? Vì sao?**  
   Đây **không phải lỗi `DUPLICATE`**, mà là hiện tượng vật lý bình thường cần một **quy tắc riêng (cross-camera seam policy)**. Trên hai camera vật lý khác nhau, vật thể được chụp từ hai góc nhìn phối cảnh và mức độ méo quang học khác nhau (ví dụ: là vùng `edge` ở camera trước nhưng là vùng `mid` ở camera hông). Cả hai box 2D đều là quan sát hợp lệ trên ảnh cảm biến. Nếu tự ý xóa một box vì cho là `DUPLICATE`, tầng Perception của camera đó sẽ mất vết vật thể. Việc dung hợp hai quan sát này thành một đối tượng duy nhất phải do tầng Sensor Fusion / 3D Object Detection phía sau xử lý dựa trên calibration.

2. **Một vật đi qua nhiều frame trên cùng camera: khi nào giữ cùng track ID, khi nào thêm keyframe hoặc trạng thái Outside? Nêu bằng chứng sẽ cần trước khi nối track qua hai camera.**  
   - *Giữ Track ID:* Khi vật thể tiếp tục xuất hiện trong trường nhìn và duy trì được tính liên tục về danh tính (identity continuity) giữa các frame liên tiếp.
   - *Thêm Keyframe:* Khi vật thể có sự thay đổi lớn về hình học, hướng di chuyển (ví dụ xe rẽ góc, chuyển từ nhìn đuôi sang nhìn sườn) hoặc thay đổi tỷ lệ kích thước đột ngột do tiến lại gần camera.
   - *Trạng thái Outside:* Khi vật thể đi hoàn toàn ra khỏi vùng nhìn thấy của ống kính hoặc bị vật khác che khuất hoàn toàn quá ngưỡng thời gian quy định.
   - *Bằng chứng cần trước khi nối track qua hai camera:* Cần đồng bộ thời gian phần cứng chính xác (timestamp sync mức micro/mili-giây), ma trận extrinsic chuẩn xác giữa hai camera, và phép kiểm tra tính tương thích vector vận tốc/vị trí không gian 3D trên hệ tọa độ xe ego.

3. **Nhìn lại cả buổi: một chỗ bạn tin nhãn mình đúng nhưng reference hoặc người soát nghĩ khác (dẫn frame/`object_ref`), bạn đã xử lý thế nào, và nếu làm lại slice này bạn sẽ đổi gì trong cách làm?**  
   Tại frame `adasind_199770.jpg` đối tượng `L7` (xe ba bánh ThreeWheeler ở sát mép trái $x=0$), ban đầu tôi cho rằng thân xe chính đã nằm trọn trong khung hình nên để `truncated=false`. Tuy nhiên, khi kiểm tra kỹ lại theo luật R05, một phần rìa bánh xe và cản trước đã bị cạnh khung hình cắt qua nên bắt buộc phải đặt `truncated=true`. Tôi đã xử lý bằng cách cập nhật lại thuộc tính trong đợt Rework, đồng thời làm Escalation Ticket đề xuất quy chuẩn cho vật thể vùng cực rìa. Nếu làm lại slice này từ đầu, tôi sẽ kiểm tra tọa độ biên của các box sát cạnh ảnh ($x=0$ hoặc viền vành kính) ngay từ khâu gán nhãn nháp và vẽ ngay polygon `ego_body` ở đáy ảnh trước khi vẽ các box đối tượng.
