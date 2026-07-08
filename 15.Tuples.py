# Tuple

my_tuple = (
    "apple",
    "banana",
    "cherry",
)  # so tuples are like lists but they are immutable
# meaning you cannot change them after they are created

print(my_tuple)

user = {(1, 2): [1, 2, 3], "Name": "John", "Age": 30}

print(user[(1, 2)])  # this is how you can use a tuple as a key in a dictionary

# tuple_Methods

print(
    my_tuple.count("apple")
)  # this will count how many times "apple" appears in the tuple

print(my_tuple.index("banana"))  # this will return the index of "banana" in the tuple

print(len(my_tuple))  # this will return the length of the tuple
