def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    if isNumeric(x) and isNumeric(y):
        print("Variables are numeric and will apply swap")
        print("Value of 1st variable before swap: ", x)
        print("Value of 2nd variable before swap: ", y)
        tempVar = x
        x = y
        y = tempVar
        print("Value of 1st variable after swap: ", x)
        print("Value of 2nd variable after swap: ", y)
    else:
        print("Variables are not numeric and values are not swapped")
        return -1
    
#function to check if value is numeric (integer or float)
def isNumeric(val):
    return isinstance(val, (int, float))


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
swap("Apple", 10)
# - 9, 17
swap(9.0, 17.2)