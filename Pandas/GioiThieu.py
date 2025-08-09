# Pandas là gì
# Là thư viện python được sử dụng để làm việc với các tập dữ liệu
# Có chức năng phân tích, dọn dẹp, khám phá và thao tác dữ liệu
# Pandas <=> Panel Data, Python Data Analysis 
import pandas 
mydataset = {
    'cars': ['BMW',"Volvo","Ford"],
    'passings':[2,7,3]
}
myvar = pandas.DataFrame(mydataset)

print(myvar)

# tạo tên tắt cho thư viện
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(pd.__version__)
