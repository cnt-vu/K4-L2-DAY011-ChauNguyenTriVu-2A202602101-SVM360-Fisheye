# Sensor context

- **Rig:** Camera fisheye đơn được gắn cố định ở phía trước xe (khu vực nắp ca-pô / cản trước hoặc nóc xe ego), hướng về phía trước với trường nhìn siêu rộng (FOV xấp xỉ 180°–190°) để quan sát toàn cảnh giao thông phía trước và hai bên hông xe.
- **`ego_body`:** Xuất hiện ở phần đáy trung tâm của khung hình (phần viền cản trước / nắp ca-pô hoặc mép thân xe ego). Thấy được ở phần lớn các frame (46/48 frame ADASIND), ngoại trừ 2 frame ngoại lệ không thấy thân xe (adasind_006840.jpg và adasind_271039.jpg).
- **Vòng kính (lens circle):** Nằm cân đối ở trung tâm ảnh, tạo thành một vòng tròn quang học rõ nét với viền đen bao quanh ngoài rìa (`lens_border`), chiếm khoảng 75%–80% diện tích khung hình chữ nhật.
