from openpyxl import Workbook
from docx import Document
workbook = Workbook()
booksheet = workbook.active
path = ('G:/001桥梁检测/2018年12月11宿迁录系统/2017年宿迁市国省干线-泗阳县-清理表格版.docx')
doc = Document(path)
r = 0
c = 0
for table in doc.tables:
    r += 1
    for row in table.rows:
        c = 0
        r += 1
        for cell in row.cells:
            c += 1
            booksheet.cell(r, c).value = cell.text
workbook.save('G:/001桥梁检测/2018年12月11宿迁录系统/new.xlsx')
# doc.save('D:/201708291223534270_new.docx')
