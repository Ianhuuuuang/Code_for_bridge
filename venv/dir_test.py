# import re
# a = re.match('^[\u4e00-\u9fa5|，。；？]+\?$', '你好哈人日你，妈我。我？；们我為啥說在張志這?')
# a.groups()
# str1 = 'abcdefghijk'
# it = str1[::-1]
# print(it)
def subdict(dct,keys):
    return dict([(key,dct.get(key)) for key in keys if dct[key]])

# dic = {'sign':1,'node':'end','time':''}
# res = subdict(dic,['sign','node','time'])
# res = len(dic)
# print(res)
# import xlrd
# filepath = 'G:\\002桥梁监控\\2019年度\\20190115波形钢腹板'
# filename = '悬浇束钢筋2019.xlsx'
# sheetname = '边跨底板2019'
# List_Pw = ['y1','y2','y3','y4','y5','y6','xy1','xy2','xy3','xy4','xy5','xy6',
# 'ry1','ry2','ry3','ry4','ry5','ry6']
# worksheet = xlrd.open_workbook(filepath+'\\'+filename)
# sheet = worksheet.sheet_by_name(sheetname)
# TDN_title = sheet.col_values(0)
# TDN_data = sheet.col_values(2)
# res = dict(zip(TDN_title,TDN_data))
# ans = subdict(res,List_Pw)
# print(ans)

L = 12//4
print(L)