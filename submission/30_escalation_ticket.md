# Escalation ticket

## Ticket 1

- **Frame:** adasind_199770.jpg
- **Ảnh chụp:** submission/screenshots/escalation_edge_vehicle.png
- **Expected impact:** Đối tượng ThreeWheeler ở sát mép trái (tọa độ $x=0$) bị thấu kính fisheye kéo giãn méo dạng quạt cong và bị cắt cụt bởi vành đen. Việc ép đóng bounding box trục thẳng (axis-aligned bounding box) trên ảnh gốc khiến box bị loãng, chứa tới hơn 60% diện tích là nền đường và vành kính, gây nhiễu nghiêm trọng khi chuyển đổi chiếu sang mặt phẳng mắt chim (Bird's-Eye View - BEV) hoặc ước lượng khoảng cách trong hệ thống SVM 360°.
- **Owner:** guideline
- **Recommendation:** Ban hành quy chuẩn phân ranh giới cho vật thể mép rìa: cho phép sử dụng polygon bao bọc đường viền thực tế hoặc quy định cụ thể ngưỡng loại trừ `ignore_region` để tránh sai số hình học khi mapping 3D.
