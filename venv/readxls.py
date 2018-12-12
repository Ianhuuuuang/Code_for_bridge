import xlrd
import pyautogui as pg
import time
import pyperclip as pl
path = r'G:\001桥梁检测\2018年12月11宿迁录系统'
file = '病害表格.xlsx'
sheetname='9'
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
time.sleep(2)
for i in range(126, 130):
    print(i+1)
    pg.click(340, 268, button='left')
    time.sleep(0.5)
    pg.click(536, 330)
    info1 = sheet.cell(i,0).value
    pg.typewrite(info1)
    #pg.typewrite(str(int(info1)))
    time.sleep(1)
    pg.click(760, 328)
    pg.press('down',presses=2)
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1)
    pg.click(977, 327)
    time.sleep(1)
    pg.press('down',presses=2)
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1)
    pg.press('tab')
    info2 = sheet.cell(i, 1).value
    pl.copy(info2)
    pg.hotkey('ctrlleft','v')
    time.sleep(0.5)
    pg.press('tab')
    info3 = sheet.cell(i, 3).value
    pl.copy(info3)
    pg.hotkey('ctrlleft','v')
    time.sleep(0.5)
    pg.press('tab')
    info4 = sheet.cell(i, 2).value
    pl.copy(info4)
    pg.hotkey('ctrlleft','v')
    info5 = sheet.cell(i, 4).value
    if info5!='/':
        pg.click(1765, 329)
        time.sleep(1)
        pg.click(891, 562)
        time.sleep(0.5)
        pl.copy(str(int(info5))+'.jpg')
        time.sleep(1)
        pg.hotkey('ctrlleft', 'v')
        pg.click(1243, 672)
        time.sleep(0.5)
        pg.click(1068, 708)
        time.sleep(10)
        pg.click(483, 271)
        time.sleep(5)
    else:
        time.sleep(1)
        pg.click(483, 271)
        time.sleep(5)
