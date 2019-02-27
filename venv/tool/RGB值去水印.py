from PIL import Image
import numpy as np

img = Image.open("D:\\test.png")#读取系统的内照片
img = img.convert('RGBA') #将图片转化为RGBA数值
pixdata = img.load() #得到图片RGBA数值矩阵
total = 1250*1444
count = 0
for i in range(660,1910):#遍历所有长度的点
    for j in range(1000,2440):#遍历所有宽度的点        
        #if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
        if (pixdata[i,j][0]>=200 and pixdata[i,j][1]<160 and pixdata[i,j][2]<160):  
            pixdata[i,j] = (255,255,255,255)#则这些像素点的颜色改成白色
        count += 1
        ans = round(count/total*10,4)
        print('已完成：'+str(ans)+'%')
img.save("D:\\12\\test.png")#保存修改像素点后的图片

