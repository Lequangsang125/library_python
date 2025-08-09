#Numpy được sử dụng để xử lý  các mảng và ma trận đa chiều lớn
# cung cấp các hàm cho đại số tuyến tinh và tạo số ngẫu nhiên,quan trọng với khoa học dữ liệu và học máy
# CÁC LOẠI MẢNG
# 1 mảng 1 chiều
import numpy as np
list_1 = [ 1, 2, 3, 4]
sample_array = np.array(list_1)
print("list_1 in python :", list_1)
print("Numpy Array in python",sample_array)
print(type(list_1))
print(type(sample_array))

# Mảng 2 chiều 
# Lưu trữ dữ liệu theo nhiều chiều, hàng và cột, nó là mảng của các mảng
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = [9,10,11,12]

sample_array = np.array([list_1,
                         list_2,
                         list_3])
print("Mảng đa chiều trong python",
      sample_array)

# Các tham số của một mảng numpy
# 1) Axis: trục của mảng mô tả thứ tự lập chỉ mục trong mảng
# Axis 0 = 1 chiều
# Axis 1 = 2 chiều
# Axis 2 = 3 chiều

# 2) shape Hình dạng: số lượng phần tử dọc theo mỗi trục và được trả về dưới dạng 1 tuple
sample_array = np.array([[0,4,2],
                         [3,4,5],
                         [23,4,5],
                         [2,34,5],
                         [5,6,7]])
print("Hình dạng của mảng", sample_array.shape) # (5,3)

#3 đối tượng kiểu dữ liệu (dtype)
#numpy.dtype: mô tả cách các byte trong khối bộ nhớ có kích thước cố định tương ứng một một mục mảng được diễn giải
sample_array_1 = np.array([[0,4,2]])
sample_array_2 = np.array([0.2,0.4,2.4])
print('kiểu dữ liệu của mảng 1', sample_array_1.dtype)
print('kiểu dữ liệu của mảng 2', sample_array_2.dtype)

#Các cách khác nhau để tạo mảng numpy
# 1) numpy.array(): Đối tượng mảng Numpy đượcc gọi là ndarray
# cú pháp numpy.array(tham số)
arr = np.array([3,4,5,5])
print("mảng:",arr)

# 2) numpy.fromiter()
# tạo mảng một chiều mới từ một đối tượng có thể lặp lại
# Cú pháp numpy.fromiter(iterable, dtype ,count = -1)
var = 'lequangsang'
arr = np.fromiter(var,dtype = 'U2')
print('Fromiter() array',arr)

# 3) numpy.arange()
# trả về các giá trị cách đều nhau trong 1 khoảng nhất điijnh
# Cú pháp: numpy.arange(Bắt đầu, dừng,bước,kiểu dữ liệu = k có)
np.arange(1,20,2,
          dtype = np.float32)

#4) numpy.linspace()
# trả về các số cách đều nhau trong khoảng giữa hai giới hạn được chỉ định
#Cú pháp: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
np.linspace(3.5,10,3,
            dtype = np.int32)

#5) numpy.empty()
# tạo 1 mảng mới có hình dạng và kiểu dữ liệu cho trước mà không khởi tạo giá trị
# Cú pháp: numpy.empty(hình dạng, kiểu dữ liệu = float, thứ tự = 'C')
np.empty([4,3],
         dtype = np.int32,
         order = 'f')

#6) numpy.ones()
# dùng để lấy 1 mảng mới có hình dạng và kiểu nhất định được điền bằng số 1
#Cú pháp: numpy.ones(hình dạng, kiểu dữ liệu = Không có, thứ tự = 'C')
np.ones([4,3],
        dtype = np.int32,
        order = 'f')

#7) numpy.zeros()
# dùng để lấy 1 mảng mới có hình dạng và kiểu dữ liệu nhất định được điền bằng số 0
#Cú pháp: numpy.ones(hình dạng, dtype=Không có)
np.zeros([4,3],
         dtype = np.int32,
         order = 'f')
