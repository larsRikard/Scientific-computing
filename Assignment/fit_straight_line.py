import math
import numpy as np
import matplotlib.pyplot as plt

# Linear regression


def error_sum_points_and_line(dataset: list[float], a: float, b: float) -> float:
    """sums the square of error between points in a list and a linear function.
    Assumes that x increases by 1 per value of y.

    Args:
        dataset (list[float]): list of datapoints.
        a (float): coefficient of a straight line function.
        b (float): constant part of a straight line function.

    Returns:
        float: sum of squared error.
    """
    error = 0
    for num, y in enumerate(dataset):
        f_x = a*num+b
        error += (f_x-y)**2
    return error




def brute_force_regression(dataset: dict[list[float], list[float]]) -> dict[float, float]:
    """Takes measurements and tries to find a usable linear regression by minimizing the error

    Args:
        dataset (dict[list[float], list[float]]): Takes a dictionary with lists of measurements of x and y values

    Returns:
        dict[float, float]: returns a dictionary with a and b values of a linear function a*x+b
    """
    best_error = float("inf")
    previous_error = float("inf")
    best_a = 0
    best_b = 0
    a = 0
    b = 0

    for x in range(103, -100, -1):
        if(best_error and previous_error and previous_error > best_error):
            a = best_a + x
        else:
            a = best_a - x
        error = error_sum_points_and_line(dataset["y"], a, b)

        if(best_error and error < best_error):
            best_error = error
            print(best_error)

            best_a = a
            print(best_a)
        previous_error = error

    for x in range(100, -100, -1):
        if(best_error and previous_error and previous_error > best_error):
            b = best_b + x
        else:
            b = best_b - x
        error = error_sum_points_and_line(dataset["y"], a, b)
        if(best_error and error < best_error):
            best_error = error
            best_b = b
        previous_error = error

    return({
        "a": best_a,
        "b": best_b
    })


def user_interaction(dataset: dict[list[float], list[float]]) -> None:
    """Takes a dictionary of datapoints, queries the user for values of a and b to create a linear function, and prints the datapoints and the function to a plot.

    Args:
        dataset (dict[list[float], list[float]]): Takes a dictionary with lists of measurements of x and y values
    """
    run = True
    while(run):
        print(f'Enter values of a and b for the function f(x) = a*x + b to calculate the summed square of error compared to the dataset.')
        print(f'dataset: {dataset["y"]}')

        a = input("a: ")
        b = input("b: ")
        print(
            f'Sum of squared error: {error_sum_points_and_line(dataset["y"],float(a),float(b))}')

        test = list(map(lambda x: float(a)*x+float(b), dataset["x"]))
        print(test)

        figure = plt.figure()
        ax = figure.add_subplot(1, 1, 1)
        ax.scatter(dataset["x"], dataset["y"],
                   color='tab:blue', label='Measurements')
        ax.plot(dataset["x"], test, color='tab:orange',
                label='Regression attempt')
        ax.legend()
        plt.show()

        cont = input("Continue [Y/N]?\n")
        if(cont.lower() == "n"):
            run = False


y = [0.5, 2.0, 1.0, 1.5, 7.5]
x = list(np.arange(0, len(y), 1))

dataset = {
    "y": y,
    "x": x
}

print(f'Total error: {error_sum_points_and_line(dataset["y"], 2, 3)}')

forced_regression = brute_force_regression(dataset)

print(
    f'Attempt to brute force regression gives a: {forced_regression["a"]} and b: {forced_regression["b"]}')

user_interaction(dataset)
