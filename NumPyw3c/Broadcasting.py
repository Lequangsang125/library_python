# Phát sóng mảng numpy
# cho phép ta thực hiện phép toán số học trên cac mảng có hình dạng khác nhau mà không cần định hình lại chúng
# tự động điều chỉnh mảng nhỏ hơn để phù hợp với hình dạng của mảng lớn bằng cách copy 
import numpy as np

array_2d = np.array([[1,2,3],[4,5,6]])
scalar = 10 
result = array_2d + scalar
print(result)

# Hoạt động của Broadcasting 
#1 kiểm tra kích thước: đảm bảo các mảng có cùng số kích thước hoặc kích thước có thể mở rộng
#2 đệm chiều: nếu mảng có số chiều khác nhau thì mảng nhỏ hơn sẽ được đệm bên trái bằng số 1
#3 tính tương thích về hình dạng: 2 chiều được coi là tương thích nếu chúng bằng nhau hoặc 1 trong 2 chiều bằng 1
# ví dụ
