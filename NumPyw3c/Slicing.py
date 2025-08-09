# Công thức
# [start:end:step , start:end:step]
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5]) # 2,3,4,5
# bao gồm chỉ mục bắt đầu, không bao gồm chỉ mục kết thúc

# toàn bộ mảng
print(arr[:])

# từ start đến cuối
print(arr[1:])

# từ đầu đến end
print(arr[:3])

# Cắt lát âm
arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1]) #5,6

# Step xác định bước cắt
print(arr[0:6:2])# 1,3,5 

#+++++++++++++++Cắt mảng 2 chiều+++++++++++++++++++++
arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print(arr[1,1:4]) # 7,8,9
print(arr[0:2,2]) #3,8
print(arr[0:2, 1:4]) #[[2,3,4],[7,8,9]]