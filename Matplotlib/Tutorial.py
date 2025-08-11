# là thư viện vẽ đồ thị cấp thấp trong python, đóng vai trò là tiện ích trực quan hóa
#Matplotlib chủ yếu được viết bằng python, một số đoạn được viết bằng C, Objective-C và Javascript để tương thích với nền tảng.
import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()