# Dữ liệu có định dạng sai
# Để khắc phục có 2 lựa chọn
# 1 xóa các hàng 
# 2 chuyển đổi tất cả các ô trong các cột sang cùng một định dạng

#================Chuyển đổi sang định dạng chính xác ===============
# to_datetime() 
import pandas as pd
df = pd.read_csv('Pandas/data.csv')
df['Date'] = pd.to_datetime(df['Date'],format='mixed')
print(df.to_string())

#Kết quả từ phép chuyển đổi trong ví dụ trên cho chúng ta giá trị NaT, có thể được xử lý như giá trị NULL và chúng ta có thể xóa hàng bằng dropna()phương pháp này.
df.dropna(subset=['Date'], inplace = True)