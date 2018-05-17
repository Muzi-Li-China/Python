import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

plt.rcParams['font.sans-serif'] = ['SimHei']            #显示中文
plt.figure(figsize=(13,6))                              #创建图例

month = ['%d月'%i for i in range(1,13)]                  #x轴,月份
plan = np.random.randint(1000,size=12)                  #每月计划数据
fact = np.random.randint(1000,size=12)                  #每月实际数据
dif = fact - plan                                       #实际与计划的差异
T = [np.abs(x-y)/2+min(x,y) for x,y in zip(plan,fact)]  #数字标签点
X = np.arange(12)                                         #x轴坐标
xnew = np.linspace(X.min(), X.max(), 200)                 #平滑x轴数据
plan_new = spline(X, plan, xnew)                          #平滑计划数据
fact_new = spline(X, fact, xnew)                          #平滑实际数据

plt.plot(xnew,plan_new,label = '计划')                   #计划线
plt.plot(xnew,fact_new,label = '实际')                   #实际线
plt.plot([X, X], [plan, fact], 'c:')                    #差异线

'''
批量添加数字标注
z:添加的text；
xy:在图中的点
xycoords:点坐标轴系统{data:使用的坐标系统被注释的对象（默认）}
xytext:text的坐标
'''
for x,y,z in zip(X,T,dif):
    plt.annotate(z, xy=(x, y), xycoords='data', xytext=(10,0),
                 textcoords='offset points', fontsize=10,
                 arrowprops=dict(arrowstyle='->',
                                 connectionstyle="arc3,rad=.2"))

plt.xticks(X, month)     #修改x轴显示
plt.legend(loc='best')   #显示图标
plt.show()               #显示图例
