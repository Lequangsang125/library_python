import numpy as np
# TẠO MẢNG NUMPY
# Dùng ndarray 
# Tạo mảng 1 chiều 1 x 1 
x = np.array([1,2,3])

# Tạo mảng 2 chiều 2 x 2
y = np.array([[1,2],
              [3,4]])

# Tạo mảng 3 chiều 3x3
z = np.array([[[1, 2], [3, 4]],
             [[5, 6], [7, 8]]])
print(x)
print(y)
print(z)

# Dùng hàm numpy:
# numpy cung cấp cac phương thức tiện lợi để tạo các mảng được khởi tạo bằng các giá trị cụ thể như 0 và 1
a1_zeros = np.zeros((3,3))
a2_ones = np.ones((4,4))
a3_range = np.arange(0,10,2) # từ 0 đến 10, cách nhau 2 đơn vị

print(a1_zeros)
print(a2_ones)
print(a3_range)

# Lập chỉ mục index
# để truy cập các phần tử trong mảng
# tạo mảng 1 chiều
arr1d = np.array([10,20,30,40,50])

# truy cập phần tử đơn lẻ
print(arr1d[2])

# truy cập tiêu cực âm
print(arr1d[-1])

# Tạo mảng 2 chiều
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(arr2d[1,0]) 

# cắt lát
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:]) # phần tử từ chỉ mục 1 đến 3

## CÔNG THỨC
# arr[Chỉ số hàng, chỉ số cột]
# arr[:] <=> arr[:,:] <=> arr[0:index cuối + 1, 0:index cuối+1]
# <=> arr[0:index cuối + 1,:] <=> arr[:, 0:index cuối+1]

#==================BÀI TẬP ======================

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
#1 lấy hàng thứ 2 dạng mảng 1 chiều
print(arr[1])
#2 lấy hàng thứ 2 dạng mảng 2 chiều
print(arr[1:2])
#3 lấy cột thứ 3 dạng mảng 1 chiều
print(arr[:,2])
#4 lấy cột thứ 3 dạng mảng 2 chiều
print(arr[:,2:3])
#5 lấy phần tử chính giữa - số 5
print(arr[1,1])
#6 lấy subarray:[[5,6],[8,9]]
print(arr[1:,1:])
#7 lấy toàn bộ mảng
print(arr[:])
#8 lấy tất trừ hàng đầu 
print(arr[1:])
#9 lấy tất trừ cột cuối
print(arr[:,:2])
#10 lấy hàng cuối cùng, cột đầu
print(arr[2:,:1])

# Lập chỉ mục nâng cao: 
arr = np.array([10,20,30,40,50,60,70,80,90,100])
indices = np.array([1,3,5])
print('Integer array indexing:',arr[indices])

cond = arr > 0 
print