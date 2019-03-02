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

img1 = Image.open('D:\\test203.png')
img1 = img1.convert('RGBA')
a1 = np.asarray(img1)
a1.flags.writeable = True

img2 = Image.open('D:\\test201.png')
img2 = img2.convert('RGBA')
a2 = np.asarray(img2)
a2.flags.writeable = True


# a1[:,:,2] = 100
# a1[:,:,2] = 0
# a[:,:,3] = 255
# a3 = np.where(a1[:,:,0]>176,255,0)
a3 = a1[:,:,0] - a2[:,:,0]
a4 = np.where(a3==255,255,0)
a5 = a1[:,:,0] - a4

img = Image.fromarray(np.uint8(a5))
img.save("D:\\12\\test.png")#保存修改像素点后的图片


