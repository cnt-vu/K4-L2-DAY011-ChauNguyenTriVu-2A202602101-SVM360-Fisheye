# QA review · B3-dense

Mã khóa: BE48-6187

| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_199770.jpg | L7 | R05 | Đối tượng ThreeWheeler chạm sát mép trái khung hình (xtl=0) bị cắt thân xe nhưng attribute truncated đang để false, cần đổi thành true theo R05. |
| adasind_145860.jpg | ego_body | R07 | Phần nắp ca-pô/thân xe ego ở đáy ảnh chưa được vẽ polygon ignore_region với reason ego_body theo R07. |
| adasind_167700.jpg | ego_body | R07 | Chưa có polygon ignore_region phủ phần thân xe ego ở đáy khung hình theo R07. |

Ghi finding r2_qa: cell=L_only, rule_id có giá trị, why để trống.
