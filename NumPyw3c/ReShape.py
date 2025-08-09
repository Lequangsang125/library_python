# ĐỊNH HÌNH LẠI MẢNG
# thay đổi hình dạng của mảng
# hình dạng mảng là số lượng phần tử trong mỗi chiều
# ta có thể thêm hoặc bớt kích thước 
# định hình từ 1d sang 2d
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4,3)
print(newarr)

# 1d thành 3d
newarr = arr.reshape(2,3,2)
print(newarr)

# trả về view
