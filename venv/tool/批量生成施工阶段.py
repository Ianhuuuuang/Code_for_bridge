
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
text = '  {x1},  LZ, Top, 3, , YES\n\
    INPUT,  35500, 1e-005, 0, 1, 17000, 3, 0, 3, 100, -7, -2.75\n\
    INPUT,  35500, 1e-005, 0, 1, 16000, 3, 100, 3, 300, -2.75, -0.92\n\
    INPUT,  35500, 1e-005, 0, 1, 12000, 3, 300, 3, 400, -0.92, 0\n'
txt = open('D:\\res.txt','w')
# L1 = ['x1']
# L2 = 
# for w in range(1,76):
#     L3 = [w + x for x in L2]
#     D = dict(zip(L1, L3))
#     res = text.format(**D)
#     print(res,file=txt)
for i in range(1,76):
  res = text.format(**{'x1':i})
  print(res,file=txt)
txt.close()
print('done')