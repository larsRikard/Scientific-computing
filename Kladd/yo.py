import numpy as np
iterations = 10

x = np.zeros(iterations)
x[0] = 3

for i in range(1,iterations):
    x[i] = x[i-1]-((3*(x[i-1]-2)**2-1)/(6*(x[i-1]-2)))

print(f'{x = }')
