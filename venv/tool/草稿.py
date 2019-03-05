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

def grayConvert(filepath,filename,outpath):
    img = Image.open(filepath+filename)
     # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = img.convert('L')     
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

filepath = 'G:\\006其他\\检师公共基础\\'
temppath = 'D:\\12345\\tmp\\'
outpath = 'G:\\006其他\\检师公共基础\\done\\'
mkdir(temppath)
mkdir(outpath)
for i in range(23,24):
    s = str(i).zfill(3)
    filename = '2018公路水运工程试验检测考试用书《公共基础》PDF_页面_'+s+'.png'
    
    img = Image.open(filepath+filename)
    img = img.convert('RGBA')
    img = np.asarray(img)
    img.flags.writeable = True

    # a1 = np.where(img[:,:,0]==255,199,0)
    # # a2 = np.where(img[:,:,1]==255,237,0)
    # a3 = np.where(img[:,:,2]==255,204,0)
    
    # img[:,:,0] = a1
    # img[:,:,1] = a2
    # img[:,:,2] = a3
    # img[:,:,3] = 255

    img = img[445:,315:,:]

    img = Image.fromarray(np.uint8(img))
    img.save(outpath + filename)#保存修改像素点后的图片
    print('第'+ s +'图片完成')  


