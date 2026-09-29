# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_145860.jpg
## adasind_167700.jpg
- L8 mid IGNORE_SCOPE
- L9 mid IGNORE_SCOPE
- L5+R4 center WRONG_CLASS
- R2 mid MISSING
- R8 center MISSING
## adasind_199770.jpg
- L5 edge IGNORE_SCOPE
- L6 mid IGNORE_SCOPE
- L7+R2 edge ATTRIBUTE
- R3 mid MISSING
- R4 mid MISSING
- R5 edge MISSING
- R6 edge MISSING

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 9 | 7 | 2 | 1 |
| mid | 7 | 4 | 3 | 0 |
| edge | 4 | 2 | 2 | 0 |
