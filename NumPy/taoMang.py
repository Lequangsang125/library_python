# Các cách khác nhau để tạo mảng Numpy trong python
# truyền list hoặc tuple vào numpy.array(). tạo mảng 1 chiều
import numpy as np

my_list = [1,2,3,4,5]
numpy_array = np.array(my_list)
print(numpy_array)

# Tạo mảng bằng thuật toán tạo số ngẫu nhiên

random_array = np.random.rand(2, 3)
normal_array = np.random.randn(2, 2)
randint_array = np.random.randint(1, 10, size=(2, 3))  

print(random_array)
print(normal_array)
print(randint_array)

# Tạo mảng bằng cách dùng các hàm tạo ma trận
identity_matrix = np.eye(3)
diagonal_array = np.diag([1, 2, 3])
zeros_like_array = np.zeros_like(diagonal_array)
ones_like_array = np.ones_like(diagonal_array)

print(identity_matrix)
print(diagonal_array)
print(zeros_like_array)
print(ones_like_array)