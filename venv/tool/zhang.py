import numpy as np
from PIL import Image

# img = Image.open('D:\\zhang.png')
# img = img.convert('RGBA')
# a = np.asarray(img)
# a.flags.writeable = True

# b = np.where(a[:,:,0]<50,255,0)
# print(sum(b))

# a[:,:,0] = a[:,:,0]+b
# a[:,:,1] = a[:,:,1]+b
# a[:,:,2] = a[:,:,2]+b
# img = Image.fromarray(np.uint8(a))
# img.save("D:\\12\\zhang.png")#保存修改像素点后的图片
img1 = Image.open('D:\\zhang.png')
img1 = img1.convert('RGBA')
img2 = Image.open('D:\\zhang001.png')
img2 = img2.convert('RGBA')
a = np.asarray(img1)
b = np.asarray(img2)
a.flags.writeable = True
b.flags.writeable = True

c = a + b 

img = Image.fromarray(np.uint8(c[:,:,1]))
img.save("D:\\zhang01.png")#保存修改像素点后的图片


   

