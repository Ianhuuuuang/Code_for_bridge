import numpy as np
a=np.reshape(np.arange(60),(5,4,3))

b = a[:,:,0]
c = a.swapaxes(0,2)

print(b)
print(c[0])
