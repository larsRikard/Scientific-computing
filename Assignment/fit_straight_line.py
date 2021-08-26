import math
import numpy as np
import matplotlib.pyplot as plt

# Linear regression


def error_sum_points_and_line(dataset: list[float], a: float, b: float) -> float:
    """sums the square of error between points in a list and a linear function

    Args:
        dataset (list[float]): list of datapoints
        a (float): coefficient of a straight line function
        b (float): constant part of a straight line function

    Returns:
        float: [description]
    """
    error = 0
    for num, y in enumerate(dataset):
        f_x = a*num+b
        error += (f_x-y)**2
    return error


def method_of_least_squares():
    return None


def brute_force_regression(dataset: dict[list[float], list[float]]) -> dict[float, float]:
    best_error = float("inf")
    previous_error = float("inf")
    previous_a = 0
    previous_b = 0
    a = 0
    b = 0

    for x in range(100, 0, -1):
        previous_a = a
        if(best_error and previous_error and previous_error > best_error):
            a -= x
            error = error_sum_points_and_line(dataset["y"], a, b)
        else:
            a += x
            error = error_sum_points_and_line(dataset["y"], a, b)
        if(best_error and error < best_error):
            best_error = error
        previous_error = error
    return({
        "a": a,
        "b": b
    })


def user_interaction(dataset: dict[list[float], list[float]]) -> None:
    run = True
    while(run):
        print(f'Enter values of a and b for the function f(x) = a*x + b to calculate the summed square of error compared to the dataset.')
        print(f'dataset: {dataset["y"]}')
        print(type(dataset["x"]))

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
                label='User submitted function')
        ax.legend()
        plt.show()

        cont = input("Continue [Y/N]?\n")
        if(cont.lower() == "n"):
            run = False


y = [4.4, 2.0, 11.0, 21.5, 7.5]
x = list(np.arange(0, len(y), 1))

dataset = {
    "y": y,
    "x": x
}

print(f'Total error: {error_sum_points_and_line(dataset["y"], 2, 3)}')

forced_regression = brute_force_regression(dataset)

print(f'Attempt to brute force regression gives a: {forced_regression["a"]} and b: {forced_regression["b"]}')

user_interaction(dataset)
