import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,200)

def applyMap(foo,dom):
    return np.asarray(list(map(foo,dom)))


y = applyMap(lambda x: -9.8*x**2+50*x, x)
# print (y)
y_raw = y+5*np.random.rand(x.shape[0])-2.5
mi = 0
ma = 5
sred1 = []
while ma != len(y_raw):
    su = 0
    for i in range(mi, ma):
        su += y_raw[i]
    sred1.append(su / 5)
    mi += 1
    ma += 1

mi = 0
ma = 5
sred = []
while ma != len(sred1):
    su = 0
    for i in range(mi, ma):
        su += sred1[i]
    sred.append(su / 5)
    mi += 1
    ma += 1

plt.plot(x,y_raw,'or', alpha=.5)
plt.plot(x[3:-2],sred1)
plt.plot(x[5:-5],sred)
plt.plot(x,y)
plt.show()
# def plotFoo(f,x):
#     plt.(np.asarray(x), np.array(f(x)))

