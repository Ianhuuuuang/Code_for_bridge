from PIL import Image
def imgconvert(filepath,filename,outpath):
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
