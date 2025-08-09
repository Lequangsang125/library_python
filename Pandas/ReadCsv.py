# Đọc tệp csv
# tệp csv lưu được các tập dữ liệu lớn 
# tệp csv chứa văn bản thuần túy và là định dạng phổ biến
import pandas as pd
df = pd.read_csv('Pandas/data.csv')
print(df.to_string())
# dùng to_string() để in toàn bộ DataFrame

# nếu không dùng to_string() thì nó chỉ in 5 hàng đầu và cuối
df = pd.read_csv('Pandas/data.csv')
print(df) 

# trả về số hàng tối đa
print(pd.options.display.max_rows) 
# 60 hàng, nếu lớn hơn 60 hàng thì nó chỉ in 5 hàng đầu và cuối

#tăng số lượng hàng tối đa
pd.options.display.max_rows = 9999
df = pd.read_csv('Pandas/data.csv')
print(df)