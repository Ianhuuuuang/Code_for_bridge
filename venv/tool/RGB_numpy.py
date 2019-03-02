import numpy as np
from PIL import Image

def intersect(List_1,List_2,list_3):
    res = []
    turple_1 = set(zip(List_1[0],List_1[1]))
    turple_2 = set(zip(List_2[0],List_2[1])) 
    turple_3 = set(zip(list_3[0],list_3[1])) 
    res = turple_1&turple_2&turple_3
    return list(res)

text = open('D:\\test.txt','w')

img = Image.open('D:\\test.png')
img = img.convert('RGBA')
a = np.asarray(img)
a.flags.writeable = True
print(a)
print(a.shape)

index_R = np.where(a[:,:,0]>200)
index_G = np.where(a[:,:,1]<160) 
index_B = np.where(a[:,:,2]<160)

# print(a[:,:,0].shape)
# print(a[:,:,1].shape)
# print(a[:,:,2].shape)
# print(a[:,:,3].shape)
# print(index_R)
# print(index_G)
# print(len(index_R[0]))
# print(len(index_G[0]))
# print(len(index_B[0]))
index = intersect(index_B,index_G,index_R)
count = 0
total = len(index)
print(total)
for x,y in index:
    a[x,y,:] = [255,255,255,255]
    count += 1
    print(round(count/total*100,3))
img = Image.fromarray(np.uint8(a))
img.save("D:\\12\\test.png")#保存修改像素点后的图片


