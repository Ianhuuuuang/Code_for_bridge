# coding=utf-8
import docx

doc = docx.Document('D/tmp.docx')
for table in doc.tables:  # 遍历所有表格
    print('----table------')
    for row in table.rows:  # 遍历表格的所有行
        # row_str = '\t'.join([cell.text for cell in row.cells])  # 一行数据
        # print row_str
        for cell in row.cells:
            print(cell.text, '\t')