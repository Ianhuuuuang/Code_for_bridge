import xlrd

def item_math(filepath,filename,sheetname,columnNumber):
    worksheet = xlrd.open_workbook(filepath+'\\'+filename)
    sheet = worksheet.sheet_by_name(sheetname)
    TDN_title = sheet.col_values(0)
    TDN_data = sheet.col_values(columnNumber)
    if columnNumber < sheet.ncols:
        res = dict(zip(TDN_title,TDN_data))
        res['起始单元编号'] = int(res['起始单元编号'])
        res['结束单元编号'] = int(res['结束单元编号'])
        res['插入点单元号'] = int(res['插入点单元号'])
        res['钢束相对位置'] = int(res['钢束相对位置'])
    else:
        return(0) 

def subdict(dct,keys):
    return dict([(key,dct.get(key)) for key in keys if dct[key]!=''])

def col_No(filepath,filename,sheetname):
    worksheet = xlrd.open_workbook(filepath+'\\'+filename)
    sheet = worksheet.sheet_by_name(sheetname)
    return(sheet.ncols)

def TDN_Head(arg):      
    cmd = 'NAME={name},{钢束特性},{起始单元编号}to{结束单元编号},0,0,ROUND,2D\n\
               {钢束组},USER,0,0,YES,1\n\
               ELEMENT,{单元插入端点},{插入点单元号},{插入方向}\n\
               0,YES,0,0\n'
    res = cmd.format(**arg)
    return(res)

def TDN_Pw(arg):
    List_Pw = ['y1','y2','y3','y4','y5','y6','xy1','xy2','xy3','xy4','xy5','xy6',
    'ry1','ry2','ry3','ry4','ry5','ry6']    
    cmd_head = 'Y={begin},{begin_y},NO,0,0,NONE,,,,\n'
    cmd_end = 'Y={end},{end_y},NO,0,0,NONE,,,,\n'
    cmd_body = []
    cmd_body.append('Y={y1},{xy1},NO,0,{ry1},NONE,,,,\n') 
    cmd_body.append('Y={y2},{xy2},NO,0,{ry2},NONE,,,,\n')
    cmd_body.append('Y={y3},{xy3},NO,0,{ry3},NONE,,,,\n') 
    cmd_body.append('Y={y4},{xy4},NO,0,{ry4},NONE,,,,\n')
    cmd_body.append('Y={y5},{xy5},NO,0,{ry5},NONE,,,,\n')
    cmd_body.append('Y={y6},{xy6},NO,0,{ry6},NONE,,,,\n')
    dct_y = subdict(arg,List_Pw)
    if not dct_y:
        cmd_mid=''
    else:
        cmd_body = cmd_body[:len(dct_y)//3]
        cmd_mid = ''.join(cmd_body)
    res = cmd_head+cmd_mid+cmd_end
    return(res)

def TDN_Sw(arg):
    cmd_head = 'Z={begin},{begin_z},NO,0,0,NONE,,,,\n'
    cmd_end = 'Z={end},{end_z},NO,0,0,NONE,,,,\n'
    cmd_body = 'Z={},{},NO,0,{},NONE,,,,\n'


    return(cmd)

filepath = 'G:\\002桥梁监控\\2019年度\\20190115波形钢腹板'
filename = '悬浇束钢筋2019.xlsx'
sheetname = '边跨底板2019'
col_sum = col_No(filepath,filename,sheetname)

for i in range(1,col_sum):
    item = item_math(filename,filepath,sheetname,i)
    Head = ''
    Pw = ''
    Sw = ''
    cmd = Head + Pw + Sw