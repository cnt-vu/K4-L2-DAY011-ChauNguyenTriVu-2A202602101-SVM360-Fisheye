# Đối chiếu chất lượng cục bộ — rectangle

Teaching reference, không phải gold set đã phê duyệt; không có điểm đạt tự động.
Nguồn: export r1_craft đã khóa SHA256 `be486187e8907816e0364fec65bfece6109188e3ae121342c6fdc8a495d8c89b`; slice `B3-dense`.
Ghép hình học greedy một-một theo IoU ≥ 0.50, rồi so class; H ≥ 40 px.
Box trái nằm chủ yếu trong ignore_region reference không tính. Polygon, polyline, track không được chấm.
Đây là phép tính offline của lab, không phải báo cáo hay kết quả tương đương CVAT Premium.

Frame được tính: adasind_145860.jpg, adasind_167700.jpg, adasind_199770.jpg. Frame thiếu trong export: không.
TP=13; FP=1; FN=7; số lần đối chiếu=20; mean IoU của TP=0.754.

| Chỉ số | Micro | Macro | Nhãn thấp nhất |
|---|---:|---:|---:|
| accuracy | 0.650 | 0.920 | 0.850 |
| precision | 0.929 | 0.950 | 0.750 |
| recall | 0.650 | 0.650 | 0.500 |
| jaccard | 0.619 | 0.620 | 0.500 |
| dice | 0.765 | 0.760 | 0.667 |

| Nhãn | TP | FP | FN | Accuracy | Precision | Recall | Jaccard | Dice |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bike | 3 | 0 | 3 | 0.850 | 1.000 | 0.500 | 0.500 | 0.667 |
| Car | 1 | 0 | 1 | 0.950 | 1.000 | 0.500 | 0.500 | 0.667 |
| Pedestrian | 3 | 0 | 1 | 0.950 | 1.000 | 0.750 | 0.750 | 0.857 |
| ThreeWheeler | 3 | 0 | 1 | 0.950 | 1.000 | 0.750 | 0.750 | 0.857 |
| Truck | 3 | 1 | 1 | 0.900 | 0.750 | 0.750 | 0.600 | 0.750 |

| Frame | TP | FP | FN | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| adasind_145860.jpg | 2 | 0 | 0 | 1.000 | 1.000 | 1.000 |
| adasind_167700.jpg | 6 | 1 | 3 | 0.667 | 0.857 | 0.667 |
| adasind_199770.jpg | 5 | 0 | 4 | 0.556 | 1.000 | 0.556 |

Confusion matrix: hàng = teaching reference; cột = export đã khóa.
`<missing>` là thiếu box; `<extra>` là box thừa. Xem `local_quality_confusion.csv`.

| Reference \ Export | Bike | Car | Pedestrian | ThreeWheeler | Truck | <missing> |
|---|---:|---:|---:|---:|---:|---:|
| Bike | 3 | 0 | 0 | 0 | 0 | 3 |
| Car | 0 | 1 | 0 | 0 | 1 | 0 |
| Pedestrian | 0 | 0 | 3 | 0 | 0 | 1 |
| ThreeWheeler | 0 | 0 | 0 | 3 | 0 | 1 |
| Truck | 0 | 0 | 0 | 0 | 3 | 1 |
| <extra> | 0 | 0 | 0 | 0 | 0 | 0 |

Chi tiết xung đột trong `local_quality_conflicts.csv`; dữ liệu máy đọc trong `local_quality.json`.
Mismatching label đóng góp một FP cho class vẽ và một FN cho class reference; attribute khác được báo riêng.
Micro accuracy đếm mỗi cặp ghép sai class là một lần đối chiếu; Jaccard đếm cả FP và FN.
Macro/worst bỏ nhãn không xuất hiện ở cả hai phía; chỉ số không có mẫu là N/A.
