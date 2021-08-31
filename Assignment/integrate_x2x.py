from matplotlib.pyplot import step
import numpy as np

# integrate x**x from 0 to 4 with four decimal precision

# middlepoint method

def numeric_integration_middlepoint(integrand: str, step_amount: int, start: float, stop: float) -> float:
    """Calculates definite integral of x**x from amount of steps (resolution), start and stop values.

    Args:
        integrand (str): UNUSED (string representation of integrand)
        step_amount (int): Amounts of steps or slices to divide the function into
        start (float): start value of definite integral
        stop (float): stop value of definite integral

    Returns:
        float: numeric result of integration
    """

    steps = np.linspace(start, stop, step_amount)
    half_step = (steps[1]-steps[0])/2
    definite_integral = 0;
    for i in range(len(steps)-1):
        x = steps[i]+half_step
        definite_integral += (x**x)*(2*half_step)
    return definite_integral

print(f'{numeric_integration_middlepoint("x**x", 100_000_000, 0, 4) = }')
