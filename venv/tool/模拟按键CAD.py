import xlrd
import pyautogui as pg
import time

pg.PAUSE = 2

def item_math(filepath,filename,sheetname,columnNumber):
    worksheet = xlrd.open_workbook(filepath+'\\'+filename)
    sheet = worksheet.sheet_by_name(sheetname)
    TDN_title = sheet.col_values(0)
    TDN_data_pre = sheet.col_values(columnNumber)
    TDN_data = preprocess(TDN_data_pre)
    
    if columnNumber < sheet.ncols:
        res = dict(zip(TDN_title,TDN_data))
        return(res)
    else:
        return(0) 

def preprocess(lst):
    res = []
    for x in lst:
        x = str(x)
        res.append(x)
    return(res)

filepath = 'G:\\002桥梁监控\\2019年度\\20190115波形钢腹板\\excel'
filename = 'section.xlsx'
sheetname = 'Sheet1'

ColumnNo = 1
p = item_math(filepath,filename,sheetname,ColumnNo)

def nextp(x,y,item):
    pg.typewrite('@'+item[x]+','+ item[y])
    pg.press('enter')


pg.click(500,500)
time.sleep(3)
pg.click(703,975)
pg.typewrite('l')
pg.press('enter')
pg.typewrite('0,0')
pg.press('enter')

list_1 = [('x'+str(i),'y'+str(i)) for i in range(1,23)]
n=0
for x , y in list_1:
    nextp(x,y,p)
    n += 1
    print(n)
