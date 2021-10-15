import numpy as np

start = 0
end = 4
dt = 0.1
resolution = (end-start)/dt
t = np.linspace(start, end, resolution)
y = np.zeros(resolution+1)
y[0] = 1/2


def function(y_new, y_old, n):
    return y_new - (y_old + dt*(n*(y_new**3) - y_new))

def diff_function(y_new, y_old, n):
    return 1 - (y_old + dt*(3*n*(y_new**2)-1))



def newtons_method(x_initial: float, lower_bound: float = -2000, upper_bound: float = 2000, iterations: int = 20):
    x = np.zeros(iterations+1)
    x[0] = x_initial
    for n in range(iterations):
        x[n+1] = x[n] - (function(x[n])/diff_function(x[n]))
        if x[n+1] > upper_bound:
            x[n+1] = upper_bound
        elif x[n+1] < lower_bound:
            x[n+1] = lower_bound
    return x

print(f'{newtons_method(y[0])}')
    
