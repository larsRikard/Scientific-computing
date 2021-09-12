import math
import numpy as np
import matplotlib.pyplot as plot

def newtons_method(x_initial: float, lower_bound: float = -2, upper_bound: float = 2, iterations: int = 10):
    x = np.zeros(iterations+1)
    x[0] = x_initial
    for n in range(iterations):
        x[n+1] = x[n] - (function(x[n])/diff_function(x[n]))
        if x[n+1] > upper_bound:
            x[n+1] = upper_bound
        elif x[n+1] < lower_bound:
            x[n+1] = lower_bound
    return x


def fixed_point_iteration(x_initial: float = 1, lower_bound: float = -2, upper_bound: float = 2, iterations: int = 10, tolerance_limit: float = 0.05):
    x_n = np.zeros(iterations+1)
    x_n[0] = x_initial
    for i in range(iterations):
        x_n[i+1] = function_fixed_point_form(x_n[i])
    print(f'{x_n = }')
    return x_n

def function_fixed_point_form(x: float) -> float:
    return (math.e**(-x)-x**3)/2

def function(x: float) -> float:
    return (x**3)+2*x-math.e**(-x)

def diff_function(x: float) -> float:
    return 3*(x**2)+2+math.e**(-x)


def main():
    iterations = 10

    # root finder points
    x_seek_array = newtons_method(x_initial=1, iterations=iterations)

    # fixed point points
    fixed_seek_x = fixed_point_iteration(x_initial=1, iterations=iterations)
    fixed_seek_y = np.zeros(len(fixed_seek_x))
    for i in range(len(fixed_seek_y)):
        fixed_seek_y[i] = function(fixed_seek_x[i])

    print(
        f'best fixed value {fixed_seek_x[-1]} = {function_fixed_point_form(fixed_seek_x[-1])}')

    # x-axis
    x_array = np.linspace(-2, 2, 100)

    # y-axis
    function_array = np.zeros(100)
    for i in range(len(function_array)):
        function_array[i] = function(x_array[i])

    # y-axis
    fixed_point_function_array = np.zeros(100)
    for i in range(len(fixed_point_function_array)):
        fixed_point_function_array[i] = function_fixed_point_form(x_array[i])

    # Plotting
    plot.close("all")  # Closes all figures before plotting
    plot.figure(num=1, figsize=(12, 9))

    # Plot function in interval
    plot.subplot(2, 1, 1)

    # line on x axis with y = 0
    plot.plot(x_array, np.zeros(len(x_array)), "k")
     # straight line y=x
    plot.plot(x_array, x_array, "g")
    # function
    plot.plot(x_array, function_array, "b")
    # fixed point function
    plot.plot(x_array, fixed_point_function_array, "m")
    # newtons-method points
    plot.scatter(x_seek_array, np.zeros(len(x_seek_array)), c="y")

    plot.grid()
    plot.xlabel("x")
    plot.ylabel("y")
    plot.legend(["y=0", "y=x", "f(x)", "g(x)", "newton"])

    plot.subplot(2, 1, 2)

    # line on x axis with y = 0
    plot.plot(x_array, np.zeros(len(x_array)), "k")
    # straight line y=x
    plot.plot(x_array, x_array, "g")
    # function
    plot.plot(x_array, function_array, "b")
    # fixed point function
    plot.plot(x_array, fixed_point_function_array, "m")
    # Fixed-point seeker points
    plot.scatter(fixed_seek_x, fixed_seek_y, c="r")

    plot.grid()
    plot.xlabel("x")
    plot.ylabel("y")
    plot.legend(["y=0", "y=x", "f(x)", "g(x)", "fixed point"])

    plot.savefig("plot_fixed_point_iteration.svg")
    plot.show()


if __name__ == "__main__":
    main()
