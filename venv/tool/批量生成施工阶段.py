
# text = '  NAME={x1}#顶{x2}#底, 4, YES, NO, NO, 5\n\
#   ALOAD=底板湿重{x5}, FIRST, 顶板湿重{x6}, FIRST\n\
#   \n\
#   NAME={x8}f, 3, YES, NO, NO, 5\n\
#   AELEM=块段{x9}(f), 0\n\
#   \n\
#   NAME={x10}#块张拉, 2, YES, NO, NO, 5\n\
#   AELEM=块段{x11}, 7, 块段{x12}(f+d), 7\n\
#   DELEM=块段{x13}(f+d), 100, 块段{x14}(f), 100\n\
#   ALOAD={x15}#块钢束张拉, FIRST\n\
#   DLOAD=顶板湿重{x16}, FIRST, 底板湿重{x17}, FIRST\n\
#   \n\
#   NAME={x18}#挂篮, 1, YES, NO, NO, 5\n\
#   ALOAD={x19}#块施工挂篮, FIRST\n\
#   DLOAD={x20}#块施工挂篮, FIRST\n'
text = '  NAME={x1}#块张拉前, 1, YES, NO, NO, 5\n\
  ALOAD={x2}#块施工挂篮张拉时, FIRST\n\
  AELEM=块段{x3}, 7, 块段{x4}(f+d), 7\n\
  DELEM=块段{x5}(f+d), 100, 块段{x6}(f), 100\n\
  DLOAD=顶板湿重{x7}, FIRST, 底板湿重{x8}, FIRST\n\
  NAME={x9}#块张拉后, 1, YES, NO, NO, 5\n\
  ALOAD={x10}#块钢束张拉, FIRST\n\
  NAME={x11}#挂篮, 1, YES, NO, NO, 5\n\
  ALOAD={x12}#块施工挂篮, FIRST\n\
  DLOAD={x13}#块施工挂篮, FIRST\n\
  DLOAD={x14}#块施工挂篮张拉时, FIRST\n'
txt = open('D:\\res.txt','w')
L1 = [('x'+ str(i)) for i in range(1,15)]
L2 = [1,2,1,2,1,2,1,2,1,1,3,3,2,2]
for w in range(1,16):
    L3 = [w + x for x in L2]
    D = dict(zip(L1, L3))
    res = text.format(**D)
    print(res,file=txt)
txt.close()
print('done')