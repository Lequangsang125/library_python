# COPY
# sao chép dữ liệu sang mảng mới tinh
# thay đổi bản soa k ảnh hưởng mảng gốc
# tốn thêm bộ nhớ
# arr.copy()

#VIEW
# Chia sẻ dữ liệu với mảng gốc
# thay đổi ở view mảng gốc cũng bị thay đổi và ngc lại
# tiết kiệm bộ nhớ vì chung dữ liệu
# slicing(arr[1:3]), np.view hoặc 1 số thao tác reshape

# Copy = bản độc lập.
# View = “cửa sổ” nhìn vào mảng gốc.

#============COPY=============
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr) # [42  2  3  4  5]
print(x)   # [1 2 3 4 5]   

#============VIEW=============

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)  # [42  2  3  4  5]
print(x)    # [42  2  3  4  5]

#==============Kiểm tra sở hữu ==============
# base() trả về None nếu mảng đó sở hữu dữ liệu
# Nếu không, base thuộc tính sẽ tham chiếu đến đối tượng gốc
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)