# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(21191.002,21319.002)
# y=-0.00866*(21255.002-x)**2+35.478
# plt.plot(x,y)
# plt.show()
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
 
mpl.rcParams['legend.fontsize'] = 10
 
fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
 
plt.show()
