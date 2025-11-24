def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    print("List of values before replace ", lst)
    for index in range(len(lst)):
        if lst[index] == find_val:
            lst[index] = replace_val
    print("List of values after replace ", lst)
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
find_and_replace(list((1, 2, 3, 4, 2, 2)), 2, 5)
# - ["apple", "banana", "apple"], "apple", "orange"
find_and_replace(list(("apple", "banana", "apple")), "apple", "orange")