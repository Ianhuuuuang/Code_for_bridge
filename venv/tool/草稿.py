import numpy as np
a=np.reshape(np.arange(60),(5,4,3))

b = a[:,:,0]
c = a.swapaxes(0,2)

print(b)
print(c[0])
idx = np.where(a[:,:,0] == 15)
print(np.where(a[:,:,1] <16))
print(np.where(a[:,:,2] < 17))
idx = zip(idx[0],idx[1])
for x,y in idx:
    a[x,y]=[100,100,100]
print(a)