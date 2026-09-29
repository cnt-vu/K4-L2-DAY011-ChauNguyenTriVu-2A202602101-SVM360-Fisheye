# Quan sát vạch ô đỗ

- **Hai vạch `parking_line` đã vẽ (mô tả vị trí trong ảnh):** Các đoạn sơn trắng phân chia từng ô đỗ xe riêng lẻ ở tiền cảnh (foreground) và trung cảnh (midground) của bãi đỗ xe (các vạch chéo phân chia các ô đỗ nhìn thấy rõ bề mặt sơn trên mặt đường).
- **Một vạch/dấu sơn hoặc biên không vẽ, và vì sao:** Không vẽ các đường mép đường/vỉa hè (curb edge) và các vạch kẻ đường ở dải đường lộ phía xa, vì chúng đóng vai trò chỉ dẫn làn đường giao thông hoặc ranh giới lòng đường, không phải vạch phân chia ranh giới ô đỗ xe (`parking_line`).
- **Polygon `free_space` dừng ở đâu; có phần bị che nào không:** Vùng `free_space` bao trọn phần mặt đường trống của lối xe chạy chính giữa hai dãy ô đỗ; polygon dừng lại ở chân/đầu các vạch chia ô đỗ và mép khung hình; không bị che khuất và không vẽ cắt lấn vào trong lòng ô đỗ hay chướng ngại vật.
- **Ca chưa chắc cần hỏi người soát (nếu không có, ghi “không có”):** Không có.
