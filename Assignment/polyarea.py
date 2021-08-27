

# Shoelace algorithm
def polyarea(x: list[float], y: list[float]) -> float:
    
    if(len(x) == len(y)):
        area = 0
        for i in range(len(x)):
            index = i
            index_plus_one = i+1 < len(y) and i+1 or 0
            area += x[index]*y[index_plus_one]
            area -= y[index]*x[index_plus_one]
        area = (1/2)*abs(area)
        return area
    else:
        print("inputs are required to be of the same length.")


""" x = [1,3,4,3.5,2]
y = [1,1.1,2.45,5,4] """

# Square with area of 25 -> function gives expected output
""" x = [0,5,5,0]
y = [0,0,5,5] """
# Triangle with area of 12.5 -> function gives expected output
""" x = [0,5,5]
y = [0,0,5] """

# quadrilateral with area of 57 -> function gives expected output
""" x = [2, 11, 11, 4]
y = [2, 2, 8, 10]
 """
# polygon of five vertices with an area of 30 ->  function gives expected output
x = [3, 5, 9, 12, 5]
y = [4, 6, 5, 8, 11]

print(polyarea(x, y))
