import xlrd
from pyautocad import Autocad, APoint
import time

acad = Autocad(create_if_not_exists = True)
# acad.model.Addline(p1,p2)

def item_math(filepath,filename,sheetname,columnNumber):
    worksheet = xlrd.open_workbook(filepath+'\\'+filename)
    sheet = worksheet.sheet_by_name(sheetname)
    TDN_title = sheet.col_values(0)
    TDN_data = sheet.col_values(columnNumber)    
    res = dict(zip(TDN_title,TDN_data))
    return(res)

filepath = 'G:\\002桥梁监控\\2019年度\\20190115波形钢腹板\\excel'
filename = 'section.xlsx'
sheetname = 'Sheet1'

ColumnNo = 12
savepath = 'G:\\002桥梁监控\\2019年度\\20190115波形钢腹板\\CAD\\3Parts截面\\20a'
p = item_math(filepath,filename,sheetname,ColumnNo)

key_1 = [('x'+str(i),'y'+str(i)) for i in range(1,24)]
list_1 = [(p[x],p[y]) for x, y in key_1]

coor_x = 0
coor_y = 0
for x, y in list_1:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)


key_2 = [('x'+str(i),'y'+str(i)) for i in range(24,48)]
list_2 = [(p[x],p[y]) for x, y in key_2]
coor_x = p['2x']
coor_y = p['2y']
for x, y in list_2:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)

key_3 = [('x'+str(i),'y'+str(i)) for i in range(48,53)]
list_3 = [(p[x],p[y]) for x, y in key_3]
coor_x = p['3x']
coor_y = p['3y']
for x, y in list_3:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)

key_4 = [('x'+str(i),'y'+str(i)) for i in range(53,58)]
list_4 = [(p[x],p[y]) for x, y in key_4]
coor_x = p['4x']
coor_y = p['4y']
for x, y in list_4:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)

key_5 = [('x'+str(i),'y'+str(i)) for i in range(58,63)]
list_5 = [(p[x],p[y]) for x, y in key_5]
coor_x = p['5x']
coor_y = p['5y']
for x, y in list_5:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)

key_6 = [('x'+str(i),'y'+str(i)) for i in range(63,68)]
list_6 = [(p[x],p[y]) for x, y in key_6]
coor_x = p['6x']
coor_y = p['6y']
for x, y in list_6:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)

key_7 = [('x'+str(i),'y'+str(i)) for i in range(68,73)]
list_7 = [(p[x],p[y]) for x, y in key_7]
coor_x = p['7x']
coor_y = p['7y']
for x, y in list_7:
    p1 = APoint(coor_x, coor_y)
    coor_x += x
    coor_y += y
    p2 = APoint(coor_x, coor_y)
    acad.model.Addline(p1, p2)
    print(p1,p2)

acad.doc.SaveAs(savepath,1)
