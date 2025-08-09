# Bộ bài tập NumPy cơ bản – tổng hợp
# 📌 Yêu cầu: không dùng vòng lặp for nếu có thể, tận dụng tính năng của NumPy.

# 1. Tạo mảng và thao tác cơ bản
# Tạo mảng 1D chứa các số từ 10 đến 50.

# Tìm:

# Giá trị lớn nhất, nhỏ nhất.

# Vị trí (index) của giá trị lớn nhất.

import numpy as np

arr = np.arange(10,51)
print(arr)
print(arr.max())
x = arr.max()
arrmax = np.where(arr==x)
print("arrmax",arrmax)
print(arr.min())


# Tạo mảng 2D 3×4 chứa các số nguyên ngẫu nhiên từ 0 đến 100.
arr = np.random.randint(0,101,size=(3,4))
print(arr)
print(arr.max())
x = arr.max()
arrmax = np.where(arr==x)
print("arrmax",arrmax)
print(arr.min())






# 2. Indexing & slicing
# Cho mảng:

# python
# Sao chép
# Chỉnh sửa
# arr = np.arange(1, 26).reshape(5, 5)
# Lấy hàng 2 (index = 1).

# Lấy cột cuối cùng.

# Lấy sub-matrix gồm các phần tử:

# csharp
# Sao chép
# Chỉnh sửa
# [7, 8]
# [12, 13]
# 3. Broadcasting
# Tạo mảng a = np.array([1, 2, 3]) và cộng với số 10.

# Tạo mảng b shape (3, 3) chứa toàn số 5, cộng a vào b.

# 4. Ufunc & toán học
# Cho mảng:

# python
# Sao chép
# Chỉnh sửa
# arr = np.linspace(0, np.pi, 5)
# Tính sin(arr), cos(arr).

# Tính tổng của sin^2 + cos^2 (kiểm tra ≈ 1).

# 5. Mask & lọc dữ liệu
# Cho mảng ngẫu nhiên 1D 20 phần tử từ 0–50.

# Lọc ra các giá trị > 25.

# Gán các giá trị < 10 thành 0.

# 6. Thao tác hình dạng
# Cho mảng np.arange(12), đổi thành shape (3, 4) rồi hoán vị hàng ↔ cột (transpose).

# 7. Bài tập tổng hợp
# Sinh mảng 6×6 chứa số nguyên ngẫu nhiên từ 1–20.

# Tính tổng từng hàng.

# Tìm hàng có tổng lớn nhất.

# Chuẩn hóa mảng (đưa về giá trị từ 0 đến 1).