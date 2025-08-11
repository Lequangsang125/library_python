import pandas as pd
import matplotlib.pyplot as plt

# Đọc CSV (thêm encoding nếu cần)
df = pd.read_csv("project-mini/data.csv", encoding="utf-8")

# Kiểm tra tên cột chính xác
print(df.columns)

# Chuyển định dạng ngày
df["Day"] = pd.to_datetime(df["Day"])

# Chỉ lấy các quốc gia muốn phân tích
countries = ["Brazil", "Germany", "Japan", "United States"]
df_filtered = df[df["Entity"].isin(countries)]

# Chọn cột chính
col_main = "Cumulative excess deaths per 100,000 people (central estimate)"

# Bỏ NaN
df_filtered = df_filtered.dropna(subset=[col_main])

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df_filtered[df_filtered["Entity"] == country]
    plt.plot(country_data["Day"], country_data[col_main], label=country)

plt.title("Cumulative excess deaths per 100k people")
plt.xlabel("Date")
plt.ylabel("Deaths per 100k")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
