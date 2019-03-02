import numpy as np
from PIL import Image
import os

def mkdir(path): 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\") 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path) 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)  
        print(path+' 创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')

def grayconvert(filepath,filename,outpath):
    img = Image.open(filepath+filename)
     # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')
    Img.save("D:\\test.png")    
    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
    threshold = 118
    
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    
    # 图片二值化
    photo = Img.point(table, '1')
    photo.save(outpath+filename)

def rgbConvert(filepath,filename,outpath):



filepath = 'D:\\'
outpath = 'D:\\12\\'
# for i in range(1,237):
#     s = str(i).zfill(3)
#     filename = 'JTG D62-2004公路钢筋混凝土及预应力混凝土桥涵设计规范_页面_'+s+'.png'
#     imgconvert(filepath,filename,outpath)
#     print('第'+ s +'图片完成')
#     
filename = 'test.png'    
imgconvert(filepath,filename,outpath)
#     


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


