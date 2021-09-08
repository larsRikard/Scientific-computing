import math
import numpy as np
import matplotlib.pyplot as plot

def newtons_method(x_n: float):
    x_n_plus_1 = x_n -(custom_function(x_n)/diff_custom_function(x_n))
    if x_n_plus_1 > 2:
        x_n_plus_1 = 2
    elif x_n_plus_1 < -2:
        x_n_plus_1 = -2
    return x_n_plus_1

def custom_function(x:float) -> float:
    return (x**3)+2*x-math.e**(-x)

def diff_custom_function(x:float) -> float:
    return 3*(x**2)+2+math.e**(-x)

def main():
    iterations = 10
    x_seek_array = np.zeros(iterations)
    x_seek_array[0] = 1

    for i in range(iterations-1):
        x_seek_array[i+1] = newtons_method(x_seek_array[i])
    print(f'{x_seek_array = }')


    x_array = np.linspace(-2,2,100)
    y_array = np.zeros(100)
    for i in range(len(y_array)):
        y_array[i] = custom_function(x_array[i])

    # Plotting
    plot.close("all")  # Closes all figures before plotting
    plot.figure(num=1, figsize=(12, 9))

    # Plot function in interval
    plot.subplot(2, 1, 1)
    plot.plot(x_array, y_array, "b")
    plot.scatter(x_seek_array,np.zeros(len(x_seek_array)))
    plot.grid()
    plot.xlabel("x")
    plot.ylabel("f(x)")


    plot.savefig("plot_heat_tank.svg")
    plot.show()

if __name__ == "__main__":
    main()
