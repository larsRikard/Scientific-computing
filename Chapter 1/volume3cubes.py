import numpy as np
import matplotlib.pyplot as plt

#Volume of three cubes

l = np.linspace(1,3,3);

print(l);

def volumes(lengths: list[float]) -> list[float]:
    v = [];
    for length in lengths:
       v.append(length**3)
    return v;

print(volumes(l))

figure = plt.figure();
ax = figure.add_subplot(1,1,1)
ax.plot(l, l, color='tab:blue', label='length')
ax.plot(l, volumes(l), color='tab:orange', label='volume')
ax.legend()

plt.show();