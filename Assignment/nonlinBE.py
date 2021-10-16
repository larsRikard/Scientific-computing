from matplotlib import pyplot as plt
import numpy as np

start = 0
end = 4
dt = 0.25
resolution = int((end-start)/dt)
timeline = np.linspace(start, end, resolution+1)
y_BE = np.zeros(resolution+1)
y_BE[0] = 1/2
y_FE = np.zeros(resolution+1)
y_FE[0] = 1/2
y_Analytical = np.zeros(resolution+1)
y_Analytical[0] = 1/2


def analytic_function(t):
    return np.sqrt(2)/(np.sqrt(7*(np.exp(2*t))+2*t+1))

def function(y_new, y_old, t):
    return y_new - (y_old + dt*(t*(y_new**3) - y_new))

def diff_function(y_new, y_old, t):
    return 1 - (y_old + dt*(3*t*(y_new**2)-1))

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

for n in range(resolution):
    why = newtons_method(y_BE[n], y_BE[n], timeline[n+1])
    y_BE[n+1] = y_BE[n]+dt*(timeline[n+1]*(why[-1]**3)-why[-1])

for n in range(resolution):
    y_FE[n+1] = y_FE[n]+dt*(timeline[n]*(y_FE[n]**3)-y_FE[n])

for n in range(resolution):
    y_Analytical[n+1] = analytic_function(timeline[n+1])

fig = plt.figure()
l1, l2, l3 = plt.plot(timeline, y_BE, timeline, y_FE, timeline, y_Analytical)
fig.legend((l1, l2, l3), ('BE', 'FE', 'Analytical'))
plt.xlabel('time')

plt.show()