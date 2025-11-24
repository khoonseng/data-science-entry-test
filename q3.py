def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    print("List of values before update", dct)
    if key in dct:
        print("original value of", key, "is", dct.get(key))
    dct[key] = value
    print("List of values after update", dct)
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
update_dictionary({}, "name", "Alice")
# - {"age": 25}, "age", 26
update_dictionary({"age": 25}, "age", 26)