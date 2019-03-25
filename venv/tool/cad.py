import xlrd
from pyautocad import Autocad, APoint
import time

acad = Autocad(create_if_not_exists = True)
txt = open('D:\\output.txt','w')
def get_coo(filepath,filename,sheetname):
    worksheet = xlrd.open_workbook(filepath+'\\'+filename)
    sheet = worksheet.sheet_by_name(sheetname)
    coo_0 = sheet.col_values(0)
    coo_x = sheet.col_values(1)
    coo_y = sheet.col_values(2)
    coo_z = sheet.col_values(3)  
    res = list(tuple(zip(coo_0,coo_x,coo_y,coo_z)))
    return(res)
bridge = ['陈吕桥','灵钢桥','马云桥','前葛桥','双丰桥','新禹桥','长新河中桥']
bridgeL = [13,39,60,39,39,48,20]
filepath = 'G:\\005桥梁加固\\20190323桥头跳车七座桥线形\\线形整理\\双丰桥'
filename = '双丰桥.xlsx'
sheetname = 'Sheet1'
line_sum = 6

L = sorted(get_coo(filepath,filename,sheetname))
for line in L:
    print(line,file=txt)
L0 = [0,41,82,123,164,205,len(L)]
L4 = [0,49,99,149,198,248,len(L)]
L5 = [0,75,150,225,299,374,len(L)]
L6 = [0,41,82,123,164,205,len(L)]
period = L4
reversID = 1

for i in range(line_sum):
    begin = period[i]+7
    offset_y = i*30
    Start = APoint(reversID*L[begin][1]*2,L[begin][2]*10+offset_y)    
    end = period[i+1]
    coo = []
    for x in range(begin,end):
        tmp = L[x][1],L[x][2]
        coo.append(tmp)
    scoo = sorted(coo)
    for x in range(1,len(scoo)):
        Point1 = APoint(reversID*scoo[x-1][0]*2,scoo[x-1][1]*10+offset_y)
        Point2 = APoint(reversID*scoo[x][0]*2,scoo[x][1]*10+offset_y)
        acad.model.Addline(Point1, Point2)        
    acad.model.AddText('第{0}条线，编号{1}'.format(i+1,L[begin][0]),Start,1)
txt.close()
