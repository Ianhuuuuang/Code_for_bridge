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

filepath = 'D:\\'
temppath = 'D:\\荷载试验\\tmp\\'
outpath = 'D:\\荷载试验\\done\\'
mkdir(temppath)
mkdir(outpath)
for i in range(1,2):
    s = str(i).zfill(2)
    # filename = 'JTGT J21-01-2015公路桥梁荷载试验规程 _页面_'+s+'.png'
    filename = 'zhang.png'
    grayConvert(filepath,filename,temppath)
    tmp = Image.open(temppath+filename)
    tmp = tmp.convert('RGBA')
    tmp = np.asarray(tmp)
    tmp.flags.writeable = True

    img = Image.open(filepath+filename)
    img = img.convert('RGBA')
    img = np.asarray(img)
    img.flags.writeable = True

    a1 = np.where(img[:,:,0]>178,255,0)

    a3 = a1 - tmp[:,:,0]
    a4 = np.where(a3==255,255,0)
    a5 = a1 - a4
    a5[:,0:270] = 255
    a5[:,2250:] = 255

    head = a5[:,0:130]
    body = a5[:,131:2380]
    bot = a5[:,2381:]
    newhead = np.hstack((head,bot))
    if not i%2:
        res = np.hstack((body,newhead))   
    else:
        res = np.hstack((newhead,body))

    img = Image.fromarray(np.uint8(res))
    img.save(outpath + filename)#保存修改像素点后的图片
    print('第'+ s +'图片完成')  


