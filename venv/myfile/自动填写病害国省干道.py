import xlrd
import pyautogui as pg
import time
import pyperclip as pl
import os
def merge(str1,str2):  # 合并两个单元格内容
    str1 = str1.replace('第','')
    str1 = str1.replace('孔', '')
    str1 = str1.strip()
    str2 = str2.strip()
    str2 = str2[:-1]
    r = str1+'-'+str2
    return r
def find_string(s,t):
    try:
        s.index(t)
        return True
    except(ValueError): 
        return False
path = r'G:\001桥梁检测\2018年12月11宿迁录系统\泗洪'
file = '病害表格py.xlsm'
sheetname='Sheet'
#打开文件
data = xlrd.open_workbook(path + '/' +file)
#path + '/' +file 是文件的完整路径
#获取表格数目
# nums = len(data.sheets())
# for i in range(nums):
#根据sheet顺序打开sheet
# sheet1 = data.sheets()[i]
#根据sheet名称获取
sheet = data.sheet_by_name(sheetname)
#获取sheet（工作表）行（row）、列（col）数
# nrows = sheet2.nrows   #行
# ncols = sheet2.ncols   #列
# print(nrows,ncols)
#循环行列表数据
# for i in range(nrows):
#     print(sheet2.row_values(i))
#获取单元格数据
#1.cell（单元格）获取
#2.使用行列索引
# cell_A2 = sheet2.row(0)[1].value
# print(cell_A2)
time.sleep(5)
pg.click(90,257)
time.sleep(1)
coo1 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\上部.png',grayscale=True)
os.system('cls')
print('***********************10%************************')
coo2 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\一般.png',grayscale=True)
os.system('cls')
print('***********************20%************************')
coo3 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\支座.png',grayscale=True)
os.system('cls')
print('***********************30%************************')
coo4 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\护坡.png',grayscale=True)
os.system('cls')
print('***********************40%************************')
coo5 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\桥墩.png',grayscale=True)
os.system('cls')
print('***********************50%************************')
coo6 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\桥台.png',grayscale=True)
os.system('cls')
print('***********************60%************************')
coo7 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\桥面.png',grayscale=True)
os.system('cls')
print('***********************70%************************')
coo8 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\伸缩缝.png',grayscale=True)
os.system('cls')
print('***********************80%************************')
coo9 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\护栏.png',grayscale=True)
os.system('cls')
print('***********************90%************************')
coo10 = pg.locateCenterOnScreen(r'D:\vscodefile\图片\排水.png',grayscale=True)
os.system('cls')
print('***********************100%************************')
print('Start')
time.sleep(1)
#-----------------------------------填写数据起始-------------------------------------
begin=1120
end=1208
#-----------------------------------------------------------------------------------
for i in range(begin, end):    
    part=sheet.cell(i, 4).value
    # exPart='起始'
    # if exPart!=part:
    if find_string(part,'上部'):     
        pg.click(coo1[0], coo1[1])
    elif find_string(part,'箱室'):        
        pg.click(coo1[0], coo1[1])
    elif find_string(part,'一般'):        
        pg.click(coo2[0], coo2[1])
    elif find_string(part,'支座'):        
        pg.click(coo3[0], coo3[1])
    elif find_string(part,'护坡'):        
        pg.click(coo4[0], coo4[1])
    elif find_string(part,'桥墩'):        
        pg.click(coo5[0], coo5[1])
    elif find_string(part,'桥台'):        
        pg.click(coo6[0], coo6[1])
    elif find_string(part,'桥面'):        
        pg.click(coo7[0], coo7[1])
    elif find_string(part,'伸缩缝'):        
        pg.click(coo8[0], coo8[1])
    elif find_string(part,'护栏'):        
        pg.click(coo9[0], coo9[1])
    elif find_string(part,'排水'):        
        pg.click(coo10[0], coo10[1])
    else:
        pass
    # else:
    #     pass
    time.sleep(2)
    print(str(int(i+1))+'/'+str(int(end)))
    info8 = sheet.cell(i, 8).value
    info9 = sheet.cell(i, 9).value
    pg.moveTo(340, 268,duration=0.25)
    pg.click()
    time.sleep(0.5)
    pg.moveTo(536, 330,duration=0.25)
    pg.click()
    # info1_1 = sheet.cell(i,0).value
    # info1_2 = sheet.cell(i, 1).value
    # info1 = merge(info1_1, info1_2)
    info1 = sheet.cell(i, 1).value
    pl.copy(info1)
    time.sleep(0.5)
    pg.hotkey('ctrlleft', 'v')
    #pg.typewrite(str(int(info1)))
    time.sleep(1)
    pg.moveTo(760, 328,duration=0.25)
    pg.click()
    time.sleep(0.5)
    pg.press('down',presses=int(info8))
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1)
    pg.moveTo(977, 327,duration=0.25)
    pg.click()
    time.sleep(0.5)
    pg.press('down',presses=int(info9))
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('tab')
    if sheet.cell(i,4).value=='箱梁':
        info3 = sheet.cell(i, 2).value+sheet.cell(i, 4).value+sheet.cell(i, 3).value
    else:
        info3 = sheet.cell(i, 2).value+sheet.cell(i, 3).value
    pl.copy(info3)
    pg.hotkey('ctrlleft','v')
    time.sleep(0.5)
    pg.press('tab')
    info5 = sheet.cell(i, 5).value
    pl.copy(info5)
    pg.hotkey('ctrlleft','v')
    time.sleep(0.5)
    pg.press('tab')
    info6 = sheet.cell(i, 6).value
    pl.copy(info6)
    pg.hotkey('ctrlleft','v')
    info7 = sheet.cell(i, 7).value
    time.sleep(0.5)
    if info7!='/':
        pg.moveTo(1765, 329,duration=0.25)
        pg.click()
        time.sleep(1)
        pg.moveTo(891, 562,duration=0.25)
        pg.click()
        time.sleep(0.5)
        imageName = str(0)+str(int(info7))+'.jpg'
        pl.copy(imageName)
        time.sleep(1)
        pg.hotkey('ctrlleft', 'v')        
        pg.moveTo(1243, 672,duration=0.25)
        pg.click()
        time.sleep(0.5)
        pg.moveTo(1068, 708,duration=0.25)
        pg.click()
        time.sleep(5)
        pg.moveTo(483, 271,duration=0.25)
        pg.click()
        time.sleep(10)
    else:
        time.sleep(1)
        pg.moveTo(483, 271,duration=0.25)
        pg.click()
        time.sleep(10)
print('done')
