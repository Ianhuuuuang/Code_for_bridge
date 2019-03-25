import numpy as np
Load = [130,70,120,120,60]
wheelBase = [400,1000,140,400]

L = np.linspace(0,1140,100000)
ans = 0
Beam = 1250.7
for x in L:
    x1 = x
    x0 = x1 + wheelBase[0]
    x2 = x1 - wheelBase[1]
    x3 = x2 - wheelBase[2]
    x4 = x3 - wheelBase[3]
    if x2 < 0:
        FY1 = ((Beam+x4)*Load[4]+(Beam+x3)*Load[3]+(Beam+x2)*Load[2])/Beam
        FY2 = ((Beam-x1)*Load[1]+(Beam-x0)*Load[0])/Beam        
    elif x3 < 0:
        FY1 = ((Beam+x4)*Load[4]+(Beam+x3)*Load[3])/Beam
        FY2 = ((Beam-x2)*Load[2]+(Beam-x1)*Load[1]+(Beam-x0)*Load[0])/Beam
    else:
        FY1 = ((Beam+x4)*Load[4])/Beam
        FY2 = ((Beam-x3)*Load[3]+(Beam-x2)*Load[2]+(Beam-x1)*Load[1]+(Beam-x0)*Load[0])/Beam
    FY = FY1 + FY2
    if FY > ans:
        ans = FY
        res = FY,x
    else:
        pass    
print(res)