# Mock Data cho bài tập đếm chuỗi trùng

## Mục đích

Bài tập cho học sinh viết chương trình đọc các file `.dat` và tìm **chuỗi xuất hiện nhiều nhất** (top-10), có phân biệt hoặc không phân biệt chữ hoa/thường (case-sensitive / case-insensitive).

## Cấu trúc thư mục

```
data/
├── da1.dat
├── da2.dat
├── da3.dat
├── da4.dat
├── da5.dat
├── da6.dat
├── da7.dat
├── da8.dat
├── da9.dat
└── da10.dat
```

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

Trong mỗi file có **10 chuỗi** xuất hiện lặp lại với số lần khác nhau. **Cùng 10 chuỗi này xuất hiện trong cả 10 file** (cùng pattern, cùng count):

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

## Hướng dẫn đọc file (C#)

```csharp
var counts = new Dictionary<string, int>();

foreach (var file in Directory.EnumerateFiles("data", "da*.dat"))
{
    foreach (var line in File.ReadLines(file))
    {
        foreach (var token in line.Split(';'))
        {
            // Case-insensitive: dùng token.ToLower() làm key
            counts.TryGetValue(token, out int c);
            counts[token] = c + 1;
        }
    }
}

// Lấy top-10
var top10 = counts.OrderByDescending(x => x.Value).Take(10);
```

## Gợi ý bài tập

1. **Tìm top-10 trong 1 file** — đếm trên file `da1.dat`, kết quả count = 500, 450, 400, ..., 50.
2. **Tìm top-10 trong toàn bộ 10 file** — đếm gộp, kết quả count = 5,000, 4,500, ..., 500.
3. **So sánh case-sensitive vs case-insensitive** — đếm 2 cách, so sánh kết quả.

## Cách tái tạo dữ liệu

Chạy script `gen.py` trong thư mục `data/`:

```bash
cd data
python3 gen.py
```

Script dùng seed `42`, chạy lại sẽ ra dữ liệu giống hệt.