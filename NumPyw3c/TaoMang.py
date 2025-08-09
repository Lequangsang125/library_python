# Đối tượng mảng trong numpy được gọi là ndarray
import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))

# Chúng ta có thể truyền list,tuple,.. vào array() ==> type chuyển thành ndarray
arr = np.array((1,2,3,4,5))
print(arr) 

# Kích thước trong mảng
# 1 chiều trong mảng là 1 cấp độ sâu của mảng
# Mảng lồng nhau : là mảng có các mảng là phần tử của nó

# mảng 0D - Scalar
# là các phần tử trong 1 mảng - mỗi giá trị trong 1 mảng là 1 mảng 0D
arr = np.array(42)
print(arr)

# Mảng 1D 
# Mảng có các phần tử là mảng 0-D được gọi là mảng một chiều hoặc mảng 1-D.
arr1 = np.array([1,2,3,4,5])
print(arr1)

# Mảng 2D
# Một mảng có các phần tủ là mảng 1D đc gọi là mảng 2D
# Biểu diễn ma trận hoặc tenxo bậc 2
arr2 = np.array([[1,2,3],[1,2,3]])

# Mảng 3D
# Một mảng có các phần tử là mảng 2 chiều ( ma trận ) gọi là mảng 3 D
# Chúng thường biểu diễn tenxo bậc 3
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)

# ndim()
# dùng kiểm tra số chiều
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# ndmin()
# Xác định được số chiều của mảng
arr5 = np.array([1,2,3,4],ndmin=5)
print(arr5)
# ữ liệu gốc [1, 2, 3, 4] là mảng 1D có shape (4,).

# NumPy sẽ thêm chiều mới có size = 1 vào phía trước cho đủ 5 chiều:

# makefile
# Sao chép
# Chỉnh sửa
# shape: (1, 1, 1, 1, 4)
# Các chiều 1 này không rỗng — chúng là các “lớp bọc” bao quanh vector [1, 2, 3, 4].