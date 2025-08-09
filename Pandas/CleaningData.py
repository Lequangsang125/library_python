# Dữ liệu xấu
# các ô trống
# Dữ liệu ở định dạng sai
# Dữ liệu sai
# Bản sao

# Dọn dẹp các ô trống
# ô trống cung cấp kết quả sai khi phân tích dữ liệu
# XÓA HÀNG 
import pandas as pd
df = pd.read_csv("Pandas/data.csv")
new_df = df.dropna() # trả về data frame mới mà k ảnh hưởng gốc
df.dropna(inplace = True) # inplace thay đổi dataFrame gốc
print(new_df.to_string())

# CHÈN GIÁ TRỊ MỚI
import pandas as pd
df = pd.read_csv('Pandas/data.csv')

df.fillna(130, inplace = True) # thay thế null bằng số 130

# Chỉ thay thế cho các cột được chỉ định
df.fillna({"Calories":130}, inplace=True)

# Thay thế bằng trung bình, trung vị hoặc mode
# mean() trung bình
# Cộng tất cả giá trị trong cột, rồi chia cho số lượng giá trị(bỏ qua giá trị trống)

import pandas as pd
df = pd.read_csv('Pandas/data.csv')

x = df["Calories"].mean()

df.fillna({"Calories":x}, inplace=True)

# median() trung vị
# sắp xếp các giá trị theo thứ tự tăng dần 
# lấy giá trị ở giữa , nếu số lượng giá trị là chẵn
# lấy trung bình của hai giá trị giữa
#Ví dụ: [100, NaN, 200, 400] → Sắp xếp [100, 200, 400] → Median = 200.
df = pd.read_csv('Pandas/data.csv')

x = df['Calories'].median()

df.fillna({"Calories":x},inplace = True)
#Trung vị = giá trị ở giữa, sau khi bạn đã sắp xếp tất cả các giá trị theo thứ tự tăng dần.

# TÍNH MODE VÀ THAY THẾ BẤT KỲ GIÁ TRỊ TRỐNG NÀO BẰNG GIÁ TRỊ NÀY
df = pd.read_csv('Pandas/data.csv')
x = df['Calories'].mode()[0]
df.fillna({"Calories":x}, inplace = True)
#Mode = giá trị xuất hiện thường xuyên nhất.
