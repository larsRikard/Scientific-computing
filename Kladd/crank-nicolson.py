from matplotlib import pyplot as plt
import numpy as np

start = 0
end = 4
dt = 0.25
steps = int((end-start)/dt)
timeline = np.linspace(start, end, steps+1)
y_CN = np.zeros(steps+1)
y_CN[0] = 1/2


def function(y_new, y_old, t):
    return (dt/2)*y_new**2+(1-dt/2)*y_new-(y_old*(1+dt/2)-(dt/2)*y_old**2)

def diff_function(y_new, y_old, t):
    return dt*y_new+(1-dt/2)

def newtons_method(x_initial: float = 2, y_old: float = 1/2, t: float = 0, lower_bound: float = -9999, upper_bound: float = 9999, iterations: int = 20):
    x = np.zeros(iterations+1)
    x[0] = x_initial
    for n in range(iterations):
        x[n+1] = x[n] - (function(x[n],y_old,t)/diff_function(x[n],y_old,t))
        if x[n+1] > upper_bound:
            x[n+1] = upper_bound
        elif x[n+1] < lower_bound:
            x[n+1] = lower_bound
    return x

#Crank it
for n in range(steps):
    why = newtons_method(y_CN[n], y_CN[n], timeline[n+1])
    print(f'{why[-1] = }')
    y_CN[n+1] = y_CN[n]+dt*(why[-1]-(why[-1]**2))
    print(f'{y_CN[n+1]= }')
    


fig = plt.figure()
l1 = plt.plot(timeline, y_CN)
fig.legend((l1), ('CN'))
plt.xlabel('time')

plt.show()