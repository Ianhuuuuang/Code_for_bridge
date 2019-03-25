
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
text = '     SECT={x1}, YES, NO, NO\n\
        NO, , , , YES, 0.5, 90, 0.0024129, 452, 0.6, NO, , , , YES, 0.15, 0.0012066, NO, , \n'
txt = open('D:\\res1.txt','w')
# L1 = ['x1']
# L2 = 
# for w in range(1,76):
#     L3 = [w + x for x in L2]
#     D = dict(zip(L1, L3))
#     res = text.format(**D)
#     print(res,file=txt)
for i in range(68,103):
  res = text.format(**{'x1':i})
  print(res,file=txt)
txt.close()
print('done')