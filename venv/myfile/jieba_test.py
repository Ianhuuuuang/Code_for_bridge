import jieba
seg_list=jieba.cut("1#T梁左侧腹板，距1#墩3m处")
print(",".join(seg_list))