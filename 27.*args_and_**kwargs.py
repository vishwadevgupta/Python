# *ARGS AND **KWARGS
# *ARGS :- it is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of positional arguments to a function, and they will be collected into a tuple.
# **KWARGS :- it is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of named arguments to a function, and they will be collected into a dictionary.


# e.g. *args
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_numbers(1, 2, 3, 4, 5))


# e.g. **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=30, city="New York")
