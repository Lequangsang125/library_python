import numpy as np

# tạo mảng 
a = np.array([2,3,4])
print(a)

# tạo kiểu cho mảng
a = np.array([2,3,4],dtype=complex)
print(a)

# tạo mảng toàn số 0
a = np.zeros((3,3))
print(a)

# tạo mảng toàn số 1
a = np.ones((3,3))
print(a)

# tạo mảng có nội dung ngẫu nhiên phụ thuộc vào bộ nhớ
a = np.empty((3,3))
print(a)

# tạo chuỗi số 
# arange(bắt đầu, kết thúc, bước nhảy)
a = np.arange(1,10,3)
print(a) # 1,4,7

# MẢNG IN
#Nếu mảng quá lớn để in, NumPy sẽ tự động bỏ qua phần trung tâm của mảng và chỉ in các góc:
#Để vô hiệu hóa hành vi này và buộc NumPy in toàn bộ mảng, bạn có thể thay đổi tùy chọn in bằng cách sử dụng set_printoptions.

# Toán tử số học
a = np.array([20,30,40,50])
b = np.arange(4) # 0,1,2,3
print(a-b) # 20, 29,38,47
print(b**2) # 0,1,4,9

# tích phần tử với tích ma trận
print(a@b)
print(a.dot(b))