# Hình dạng của mảng
# là số lượng phần tử trong mỗi chiều
import numpy as np
arr = np.array([[1,2,3,4],
                [5,6,7,8]])
print(arr.shape) #(2,4) chiều 1 có 2 phần tử, chiều 2 có 4 phần tử


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
# chiều thứ 5 có 4 phần tử