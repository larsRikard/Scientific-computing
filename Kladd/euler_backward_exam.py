from matplotlib import pyplot as plt
import numpy as np

start = 0
end = 4
dt = 0.1
steps = int((end-start)/dt)
timeline = np.linspace(start, end, steps+1)
y_BE = np.zeros(steps+1)
y_BE[0] = 1/2

def function(x, y_old, t):
    return x-(dt*t*x**3)+dt*x-y_old

def diff_function(x, y_old, t):
    return 1-(dt*t*3*x**2)+dt

def newtons_method(x_initial: float = 2, y_old: float = 1/2, t: float = 0, lower_bound: float = -2000, upper_bound: float = 2000, iterations: int = 20):
    x = np.zeros(iterations+1)
    x[0] = x_initial
    for n in range(iterations):
        x[n+1] = x[n] - (function(x[n],y_old,t)/diff_function(x[n],y_old,t))
        if x[n+1] > upper_bound:
            x[n+1] = upper_bound
        elif x[n+1] < lower_bound:
            x[n+1] = lower_bound
    return x

#Euler backward
for n in range(steps):
    x = newtons_method(y_BE[n], y_BE[n], timeline[n+1])
    y_BE[n+1] = x[-1]


fig = plt.figure()
l1= plt.plot(timeline, y_BE)
fig.legend((l1), ('BE'))
plt.xlabel('time')

plt.show()