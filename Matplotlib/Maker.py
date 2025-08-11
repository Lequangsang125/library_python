# Đánh giấu matplotlib
# dùng marker()
import matplotlib.pyplot as plt
import numpy as np

ypoins = np.array([3,8,1,10])
plt.plot(ypoins,marker = '1')
plt.show()

#marker|line|color
plt.plot(ypoins,'p:b')
plt.show()

# ms kich thuoc
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()