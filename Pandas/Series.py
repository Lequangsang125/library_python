# Series giống như một cột trong bảng
# đây là mảng 1 chiều chứa dữ liệu của bất kỳ kiểu nào
import pandas as pd
a = [1,7,2]

myvar = pd.Series(a)

print(myvar)

# label - gán index cho phần tử của mảng 
import pandas as pd
a = [1,7,2]
myvar = pd.Series(a, index = ['x','y','z'])
print(myvar)
print(myvar["y"]) #7

# Đối tượng key:value dạng chuỗi
# cách key sẽ thành label - index
import pandas as pd
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories)
print(myvar)
myvar = pd.Series(calories, index = ['day1','day2'])
print(myvar)

#dataframe
#các tập dữ liệu thường là bảng đa chiều = dataframee
# series giống 1 cột, dataframe là toàn bộ mảng
import pandas as pd 
data = {
    "calories":[420,20,10],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)