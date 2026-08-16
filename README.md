## Thông số mỗi file

| Thông số | Giá trị |
|----------|---------|
| Số dòng | 499,999 |
| Số trường (field) mỗi dòng | 10 |
| Ký tự phân cách | `;` (dấu chấm phẩy) |
| Độ dài mỗi chuỗi | 10 ký tự |
| Bộ ký tự | `a-zA-Z` (chữ hoa + thường, 52 ký tự) |
| Dung lượng | ~55 MB / file |
| Tổng | ~550 MB / 10 file |

**Tổng số chuỗi (token) mỗi file:** 499,999 × 10 = **4,999,990**

## Các chuỗi "phổ biến" (xuất hiện nhiều lần)

| Rank | Chuỗi | Count mỗi file | Tổng 10 file |
|------|-------|----------------|--------------|
| 1 | `aBcDeFgHiJ` | 500 | 5,000 |
| 2 | `KlMnOpQrSt` | 450 | 4,500 |
| 3 | `UvWxYzAbCd` | 400 | 4,000 |
| 4 | `EfGhIjKlMn` | 350 | 3,500 |
| 5 | `OpQrStUvWx` | 300 | 3,000 |
| 6 | `YzAbCdEfGh` | 250 | 2,500 |
| 7 | `IjKlMnOpQr` | 200 | 2,000 |
| 8 | `StUvWxYzAb` | 150 | 1,500 |
| 9 | `CdEfGhIjKl` | 100 | 1,000 |
| 10 | `MnOpQrStUv` | 50 | 500 |

## Các chuỗi còn lại

- **4,997,240 chuỗi** mỗi file
- Mỗi chuỗi xuất hiện đúng **1 lần**
- Gần như **không trùng nhau** (do alphabet 52 ký tự, không gian chuỗi 10 vị trí cực lớn)

## Ví dụ một dòng

```
aBcDeFgHiJ;kwdmElMUPD;sVlLWOpHBn;mpFygdnCzM;ZaLQdgjcsI;XVKNbZXFFe;CXocbAHwpS;KAcUKGokhY;cNKwwhwUZt;YbcOQBSJMC
```

## Cách tái tạo dữ liệu

Chạy script `gen.py` trong thư mục `data/`:

```bash
cd data
python3 gen.py
```

