# Là cấu trúc dữ liệu 2 chiều, giống như mảng 2 chiều hoặc bảng có các hàng và cột
import pandas as pd
data = {
    'calories': [ 420, 380, 390],
    "duration": [ 50,40,45]
}
df = pd.DataFrame(data)
print(df)

# xác định vị trí hàng 
# dùng loc để trả về 1 hoặc nhiều hàng được chỉ định
print(df.loc[0])
#Lưu ý: Ví dụ này trả về Pandas Series .

#Trả về hàng 0 và 1:
print(df.loc[[0, 1]])
#Lưu ý: Khi sử dụng [], kết quả sẽ là Pandas DataFrame .

# Chỉ mục được đặt tên
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#Tải tệp vào DataFrame
#Nếu tập dữ liệu của bạn được lưu trữ trong một tệp, Pandas có thể tải chúng vào DataFrame.
import pandas as pd
df = pd.read_csv('data.csv')
print(df)