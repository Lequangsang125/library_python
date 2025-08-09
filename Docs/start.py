# | Thuộc tính     | Ý nghĩa                                                                                                            | Ví dụ                            |
# | -------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
# | **`ndim`**     | Số lượng trục (số chiều) của mảng.                                                                                 | 2D array → `ndim = 2`            |
# | **`shape`**    | Bộ tuple biểu thị kích thước mảng theo từng chiều. Chiều dài của `shape` = `ndim`.                                 | Ma trận 3×4 → `shape = (3, 4)`   |
# | **`size`**     | Tổng số phần tử trong mảng = tích các giá trị trong `shape`.                                                       | `shape = (3, 4)` → `size = 12`   |
# | **`dtype`**    | Kiểu dữ liệu của các phần tử. Có thể dùng kiểu chuẩn của Python hoặc kiểu riêng của NumPy (`int32`, `float64`...). | `dtype = numpy.float64`          |
# | **`itemsize`** | Số byte mỗi phần tử. Bằng `dtype.itemsize`.                                                                        | `float64` → `itemsize = 8` bytes |
# | **`data`**     | Bộ đệm chứa dữ liệu thực tế. Thường không dùng trực tiếp, mà truy cập qua indexing.                                | Ít sử dụng trực tiếp             |
import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr.ndim) # 1 ( chiều )
print(arr.shape) # (6,)
print(arr.size) # 6 
print(arr.dtype) # int64
print(arr.itemsize) # 8 bype


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.ndim) # 2 ( chiều)
print(arr.shape) # (3,3)
print(arr.size) # 9 
print(arr.dtype) # int64
print(arr.itemsize) # 8 bype


arr = np.array([[[1,2,3]]])
print(arr.ndim) # 3 ( chiều)
print(arr.shape) # (1,1,3)
print(arr.size) # 3 
print(arr.dtype) # int64
print(arr.itemsize) # 8 bype


