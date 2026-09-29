# Guideline patch

- **Rule mới đề xuất:** R12 — Ngưỡng diện tích nhìn thấy tối thiểu ở vùng cực rìa ($r/R \ge 0.85$): Đối với các phương tiện bị cắt bởi vành kính hoặc cạnh khung hình tại vùng rìa cực biên ($r/R \ge 0.85$), nếu phần thân xe nhìn thấy được ước lượng $< 20\%$ tổng thể tích hoặc chỉ thấy chi tiết rời rạc (ví dụ chỉ thấy một góc đèn/vệt bánh xe bị kéo dãn) dù chiều cao phóng đại vẫn thỏa $H \ge 40\text{px}$, không bắt buộc vẽ bounding box mà đưa vào `ignore_region` với `reason = unreadable`.
- **Áp dụng cho:** Tất cả 6 class động (`Car`, `Bus`, `Truck`, `ThreeWheeler`, `Bike`, `Pedestrian`) tại zone `edge` ($r/R \ge 0.85$), liên quan trực tiếp đến thuộc tính `truncated` và `ignore_region.reason`.
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** Luật hiện tại (R01, R05) chỉ căn cứ đơn thuần vào chiều cao $H \ge 40\text{px}$ trên ảnh gốc. Do hiệu ứng kéo giãn quang học cực mạnh của thấu kính mắt cá ở rìa, một mẩu vụn thân xe chỉ vài cm ngoài đời thực cũng có thể bị kéo dài thành vệt $> 40\text{px}$, dẫn đến việc các annotator bất đồng về việc có nên đóng khung box hay coi là không đọc được.
- **`rules_version` mới:** v1.1.0
- **Hiệu lực từ:** rework
