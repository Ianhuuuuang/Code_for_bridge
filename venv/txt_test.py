import  os

def file_name(file_dir):  # 读取目录下固定后缀文件名的文件完整路径名
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    return L

fn = file_name('D:/js') # fn是一个列表，读取其中第i个元素用fn（[i-1]）
for i in range(0,len(fn)):
    s_head = open(fn[i], 'r+')
    s_end = open(fn[i], 'r+')
    inser = open('D:/test_r.txt', 'r+')
    head = s_head.readlines(0)[0:8]     #[0:8]代表第1行到第7行 如果没有行就改成任意两个数字
    insert = inser.readlines(0)         #替换部分的内容，注意txt中最后一行加一个回车
    end = s_end.readlines(0)[15:16]     #[15:16]代表第15行到15行 如果没有行就改成任意相同两个数字
    head.extend(insert)
    head.extend(end)
    s_head.seek(0)
    s_end.truncate()
    for s in head:
        s_head.writelines(s)
print(fn[i])
print(len(fn))
