def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if isNumeric(num) and isNumeric(divisor):
        if num % divisor == 0:
            print(num, "is divisible by", divisor)
            return True
        else:
            print(num, "is not divisible by", divisor)
            return False
    else:
        print("arguments provided are not numeric")
        return False

#function to check if value is numeric (integer or float)
def isNumeric(val):
    return isinstance(val, (int, float))

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
check_divisibility(10, 2)
# - 7, 3
check_divisibility(7, 3)