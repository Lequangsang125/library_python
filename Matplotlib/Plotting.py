# Vẽ các điểm x và y
# hàm plot() được dùng để vẽ các điểm trong sơ đồ
# plot() sẽ vẽ một đường thẳng từ điểm này đến điểm khác
# tham số 1 là 1 mảng chứa các điểm trên trục x
# tham số 2 là 1 mảng chứa các điểm trên trục y 
import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints)
plt.show()

# vẽ không có đường thẳng 
plt.plot(xpoints,ypoints,'o')
plt.show()

# Nhiều điểm
#Vẽ một đường thẳng trong sơ đồ từ vị trí (1, 3) đến (2, 8) rồi đến (6, 1) và cuối cùng đến vị trí (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Điểm x mặc định
# nếu ta không chỉ định các điểm trên trục x, ta sẽ nhận giá trị mặc định là 0,1,2,3, tùy thuộc vào y
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])

plt.plot(ypoints)
plt.show()