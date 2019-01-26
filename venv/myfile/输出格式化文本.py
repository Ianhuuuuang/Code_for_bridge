s = open(r'G:/002桥梁监控/2019年度/梯度升温.txt','w')

for i in range(1,76):
    print('  %d, LZ, Top, 3, , NO\n\
    ELEMENT,  0, 0,  17000,  0, 14,  100, 5.5\n\
    ELEMENT,  0, 0,  16000,  100, 5.5,  300, 1.83\n \
    ELEMENT,  0, 0,  12000,  300, 1.83,  400, 0\n'%(i),file=s)

s.close()