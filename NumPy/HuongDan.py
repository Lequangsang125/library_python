# NUMPY
# Thư viện python dành cho tính toán khoa học
# Hỗ trợ mảng và ma trận đa chiều lớn cùng với 1 tập hợp các hàm toán học để thao tác trên mảng
# Giới thiệu đối tượng ndarray (mảng n chiều)
# Cho phép lưu trữ và thao tác các tập dữ liệu lớn một cách hiệu quả về mặt bộ nhớ
# KHông giống list của python, numpy đồng nhất và nhanh hơn
# Sự thật quan trọng:
#1 các phép toán vecto hóa: Nhanh hơn list vì sử dụng các hàm dựa trên C được tối ưu hóa
#2 tính năng Broadcasting : Cho phép thực hiện các thao tác giữa các mảng có hình dạng khác nhau mà không cần vòng lặp rõ ràng gọi là phát sóng
# USED FOR:
'''
1 tạo và thao tác mảng
2 thực hiện phép toán theo từng phần tử và ma trận
3 tạo số ngẫu nhiên và tính toán thống kê
4 thực hiện các phép toán đại số tuyến tính
5 làm việc với phép biển đổi Fourier
6 Xử lý các giá trị bị thiếu một các hiệu quả trong tập dữ liệu
'''

# NÊN HỌC VÌ
'''
1 tăng tốc phép toán đơn gián trên các nhóm số lớn
2 phù hợp xử lý mảng, nên không cần dùng vòng lặp
3 chức năng sẵn có cho thống kê, đại số và số ngẫu nhiên
4 thư viện Pandas, Scipy, TensorFlow và nhiều thư viện khác xây dựng dựa trên Numpy
5 Numpy dùng ít bộ nhớ và lưu trữ dữ liệu hiệu quả hơn, quan trọng khi làm việc nhiều dữ liệu
'''