# Xem tổng quan 10 hàng đầu bằng head
import pandas as pd
df = pd.read_csv('Pandas/data.csv')
print(df.head(10))

# xem hàng cuối tail
import pandas as pd
arr = pd.read_csv('Pandas/data.csv')
print(arr.tail(10))

# xem info tệp 
print(df.info())