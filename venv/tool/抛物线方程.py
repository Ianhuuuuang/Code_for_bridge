import math
def Gen_attr(t,h):
    '''
    t -- 1/2 弦长
    h -- 顶点y坐标
    '''
    a = h/t**2
    b = h
    return(-a,b)

print(Gen_attr(6090,55))