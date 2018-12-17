import os
base = r'G:\001桥梁检测\2018年12月11宿迁录系统\泗洪\病害照片'+'/' #新建文件夹的路径
for i in range(1,33):
    file_name = base+str(i) #以年份时间为文件夹名称
    os.mkdir(file_name)