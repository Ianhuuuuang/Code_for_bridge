import numpy as np
from PIL import Image

def intersect(List_1,List_2,List_3):
    res = []
    turple_R = zip(List_1[0],List_1[1])
    turple_G = zip(List_2[0],List_2[1])
    turple_B = zip(List_3[0],List_3[1])
    for item in turple_R:
        if item in turple_G and item in turple_B:
            res.append(item)
    return res


text = open('D:\\test.txt','w')

img = Image.open('D:\\test004.png')
img = img.convert('RGBA')
a = np.asarray(img)
a.flags.writeable = True
print(a)
print(a.shape)

index_R = np.where(a[:,:,0]>150)
index_G = np.where(a[:,:,1]<155) 
index_B = np.where(a[:,:,2]<155)
print(a[:,:,0].shape)
print(a[:,:,1].shape)
print(a[:,:,2].shape)
print(a[:,:,3].shape)
print(index_R)
print(index_G)
print(index_B)
print(len(index_R[0]))
print(len(index_G[0]))
print(len(index_B[0]))
index = intersect(index_R,index_G,index_B)
print(len(index))
for x in index:
    print(x,file=text)
text.close()
for x,y in index:
    a[x,y,:] = [255,255,255,255]


img = Image.fromarray(np.uint8(a))
img.save("D:\\12\\test.png")#保存修改像素点后的图片


