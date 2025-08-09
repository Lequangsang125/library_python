# Lặp lại có nghĩa là duyệt qua từng phần tử một
# Khi xử lý mảng đa chiều, ta có thể thực hiện bằng for 
# Nếu ta lặp trên mảng 1 chiều, nó sẽ duyệt qua từng phần tử 1
import numpy as np
arr = np.array([1,2,3])

for x in arr:
    print(x)

# Lặp mảng 2 chiều
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

# lặp mảng 3 chiều
# trong mảng 3 chiều nó sẽ duyệt qua tất cả các mảng 2 chiều
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

# tránh lồng for dùng nditer
for x in np.nditer(arr):
    print(x)