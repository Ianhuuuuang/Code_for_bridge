import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns#添加Seaborn模块

np.random.seed(sum(map(ord,"aesthetics")))
#首先定义一个函数用来画正弦函数，可帮助了解可以控制的不同风格参数
def sinplot(flip=1):
    x=np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*0.5)*(7-i)*flip)
sns.set_style("whitegrid")
sinplot()
plt.show()
