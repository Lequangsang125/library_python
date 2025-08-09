# Lập chỉ mục mảng Numpy
# truy cập các phần tử mảng
# lập chỉ mục mảng giống như truy cập vào một phần tử mảng
# Truy cập bằng cách tham chiếu đến số chỉ mục của phần tử đó
# Các chỉ mục trong numpy bắt đầu index = 0 
import numpy as np
arr = np.array([1,2,3,4])
print(arr[0]) 
print(arr[2] + arr[3])

# truy cập mảng 2 chiều
arr = np.array([[1,2,3,4,5], # index 0
                [6,7,8,9,10] # index 1
                ])
print(arr[0,1]) # 2
print(arr[1,4]) #10

# truy cập mảng 3 chiều
arr = np.array([[[1,2,3],[4,5,6]], # index 0
                [[7,8,9],[10,11,12]] # index 1
                ])
print(arr[0,1,2]) 
# index0 => [[1,2,3],[4,5,6]]
# index1 => [4,5,6]
# index2 => 6

#Chỉ số tiêu cực
arr = np.array([[1,2,3,4,5], #index0
                [6,7,8,9,10] # index1
                 ])

print('Last element from 2nd dim: ', arr[1, -1])