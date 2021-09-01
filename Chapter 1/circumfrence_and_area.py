#Circumfrence and area of a circle

import math

radius = 3;

def circumfrence (radius: float) -> float:
    return 2*math.pi*radius

def area (radius: float) -> float:
    return math.pi*radius**2

#String interpolation
print(f'A circle with a {radius = } has a circumfrence of {circumfrence(radius)} and an area of {area(radius)}');