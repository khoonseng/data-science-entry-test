def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    #use OOTB slice method referenced from w3schools
    s = s[::-1]
    print(s)
    return s


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
string_reverse("Hello World")
# - "Python"
string_reverse("Python")