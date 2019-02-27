import numpy as np
from PIL import Image

def intersect(List_1,List_2):
    res = []
    turple_1 = zip(List_1[0],List_1[1])
    turple_2 = zip(List_2[0],List_2[1])    
    for item in turple_1:
        if item in turple_2:
            res.append(item)
    return res

text = open('D:\\test.txt','w')

img = Image.open('D:\\test005.png')
img = img.convert('RGBA')
a = np.asarray(img)
a.flags.writeable = True
print(a)
print(a.shape)

index_R = np.where(a[:,:,0]>150)
index_G = np.where(a[:,:,1]<220) 
index_B = np.where(a[:,:,2]<220)

# print(a[:,:,0].shape)
# print(a[:,:,1].shape)
# print(a[:,:,2].shape)
# print(a[:,:,3].shape)
# print(index_R)
# print(index_G)
print(index_B)

# print(len(index_R[0]))
# print(len(index_G[0]))
# print(len(index_B[0]))
index = intersect(index_B,index_G)
print(len(index))
for x in index:
    print(x,file=text)
text.close()


count = 0
for x,y in index:
    a[x,y,:] = [255,255,255,255]
    count += 1
img = Image.fromarray(np.uint8(a))
img.save("D:\\12\\test.png")#保存修改像素点后的图片


