import math

# Linear interpolation

# part 1.
# if t = 3.2 then i = 3 will satisfy the requirement:
# t_3 <= 3.2 <= t_4


# part 2.
# A mathematical expression of a function of a line between two points: (i, y_i) and (i+1, y_i+1)
# Such function is usually expressed on the form f(x) = ax + b
# a is the average change between the points: a = (y_i+1-y_i)/(i+1-i) = y_i+1-y_i
# b is found by inserting all the known information into the function f(x) = ax + b:
# (i, y_i) => f(i) = (y_i+1-y_i)*i + b => b = y_i - (y_i+1-y_i)*i
# finally giving: f(x) = y_i + (x-i)*(y_i+1-y_i)
# or more generally: f(x,i) = y(i) + (x-i)*(y(i+1)-y(i))


# part 3.
# The "y value" calculated by the user's time value x and i being the floor of x, can be calculated as f(x,i):
# i = 3, x = 3.2:
# -> f(3.2,3) = y(3) + (3.2-3)*(y(3+1)-y(3))
# -> f(3.2,3) = y(3) + (0.2)*(y(4)-y(3))


# part a.
# Implementation of linear interpolation


def lin_interpolate(dataset: list[float], floatIndex: float) -> float:
    """Function that finds a float number between entries of a list with linear interpolation

    Args:
        dataset (list[float]): any list of numbers
        floatIndex (float): a number representing a space between entries in dataset above

    Returns:
        float: linearly interpolated float
    """
    if(floatIndex <= len(dataset)-1 and floatIndex >= 0):
        index_1 = int(math.floor(floatIndex))
        index_2 = index_1+1
        value_1 = dataset[index_1]
        value_2 = dataset[index_2]
        fraction = floatIndex-index_1
        interpolated_number = value_1 + (value_2-value_1)*fraction
        return interpolated_number

# part b.
# Function that prints interpolated values of y at times requested by the user


def find_y(dataset: list[float]) -> None:
    """Function that prints interpolated values of y at times requested by the user

    Args:
        dataset (list[float]): Requires a set of data to perform interpolation on

    Returns:
        [type]: No return
    """
    run = True
    while(run):
        print(dataset)
        val = input(
            f'Enter a pseudo index (float), between 0 and {len(dataset)-1}, and I will return a linearly interpolated point from above dataset:')
        try:
            val = float(val)
            print(val)
            if(val < 0):
                run = False
            elif(val >= 0):
                print(
                    f'The interpolated point is: y = {lin_interpolate(dataset, val)} at x = {val}')
        except:
            print('An exception occurred')

    else:
        print("End of function.")


# part c
y = [4.4, 2.0, 11.0, 21.5, 7.5]
print(lin_interpolate(y, 2.5)) #Result: 16.25
print(lin_interpolate(y, 3.1)) #Result: 20.099999999999998

#Results of these calculcations are the same as with manual calculations.

find_y(y)
