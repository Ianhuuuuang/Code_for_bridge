import xlrd

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
        if type(x) is float:
            if not x%1:
                res.append(int(x))
            else:
                res.append(round(x,2))
        else:
            res.append(x)
    return(res)


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
    cmd_head = '    Y={begin},{begin_y},NO,0,0,NONE,,,,\n'
    cmd_end = '    Y={end},{end_y},NO,0,0,NONE,,,,\n'
    cmd_body = []
    cmd_body.append('    Y={y1},{xy1},NO,0,{ry1},NONE,,,,\n') 
    cmd_body.append('    Y={y2},{xy2},NO,0,{ry2},NONE,,,,\n')
    cmd_body.append('    Y={y3},{xy3},NO,0,{ry3},NONE,,,,\n') 
    cmd_body.append('    Y={y4},{xy4},NO,0,{ry4},NONE,,,,\n')
    cmd_body.append('    Y={y5},{xy5},NO,0,{ry5},NONE,,,,\n')
    cmd_body.append('    Y={y6},{xy6},NO,0,{ry6},NONE,,,,\n')
    dct_y = subdict(arg,List_Pw)
    if not dct_y:
        cmd_mid=''
    else:
        cmd_body = cmd_body[:len(dct_y)//3]
        cmd_mid = ''.join(cmd_body)
    res = cmd_head+cmd_mid+cmd_end
    return(res.format(**arg))

def TDN_Sw(arg):
    List_Sw = ['z1','z2','z3','z4','z5','z6','xz1','xz2','xz3','xz4','xz5','xz6',
    'rz1','rz2','rz3','rz4','rz5','rz6']    
    cmd_head = '    Z={begin},{begin_z},NO,0,0,NONE,,,,\n'
    cmd_end = '    Z={end},{end_z},NO,0,0,NONE,,,,\n'
    cmd_body = []
    cmd_body.append('    Z={z1},{xz1},NO,0,{rz1},NONE,,,,\n') 
    cmd_body.append('    Z={z2},{xz2},NO,0,{rz2},NONE,,,,\n')
    cmd_body.append('    Z={z3},{xz3},NO,0,{rz3},NONE,,,,\n') 
    cmd_body.append('    Z={z4},{xz4},NO,0,{rz4},NONE,,,,\n')
    cmd_body.append('    Z={z5},{xz5},NO,0,{rz5},NONE,,,,\n')
    cmd_body.append('    Z={z6},{xz6},NO,0,{rz6},NONE,,,,\n')
    dct_z = subdict(arg,List_Sw)
    if not dct_z:
        cmd_mid=''
    else:
        cmd_body = cmd_body[:len(dct_z)//3]
        cmd_mid = ''.join(cmd_body)
    res = cmd_head+cmd_mid+cmd_end
    return(res.format(**arg))

filepath = 'E:\\python\\Code_for_bridge\\venv'
filename = '悬浇束钢筋.xlsx'
sheetname = '边跨底板2019'
col_sum = col_No(filepath,filename,sheetname)
txt = open('E:\\python\\Code_for_bridge\\venv\\test.txt','w')
for i in range(1,col_sum):
    item = item_math(filepath,filename,sheetname,i)
    Head = TDN_Head(item)
    Pw = TDN_Pw(item)
    Sw = TDN_Sw(item)
    cmd = Head + Pw + Sw
    print(cmd,file=txt)
txt.close