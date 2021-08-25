import math
import numpy as np
import matplotlib.pyplot as plt

# Linear interpolation

# part 1.
# if t = 3.2 then i = 3 will satisfy the requirement:
# t_3 <= 3.2 <= t_4

# part 2.
# A mathematical expression of a line between two points:
# a = i
# b = i + 1
# -> y(x) = f(a) + x*(f(b)-f(a))/(b-a)

y = [4.4,2.0,11.0,21.5,7.5]
t = np.linspace(0, 4, 5)

# part 1.


def lin_interpolate(dataset: list[float], floatIndex: float) -> float:
    """Function that finds a float number between entries of a list with linear interpolation

    Args:
        dataset (list[float]): any list of numbers
        floatIndex (float): a number representing a space between entries in dataset above

    Returns:
        float: linearly interpolated float
    """
    if(floatIndex < len(dataset) and floatIndex > 0):
        index1 = int(math.floor(floatIndex))
        index2 = index1+1
        value1 = dataset[index1]
        value2 = dataset[index2]
        fraction = floatIndex-index1
        interpolatedNumber = value1 + (value2-value1)*fraction
        return interpolatedNumber


print(lin_interpolate(y, 3.1))
