# Sets
# Sets are unordered collections of unique elements.
# They are useful for storing data that should not contain duplicates.

my_set = {1, 2, 3, 4, 5, 5, 6, 6}

print(
    my_set
)  # here it will print {1, 2, 3, 4, 5, 6} because sets do not allow duplicates.

print(
    my_set[1]
)  # this will give an error because sets are unordered and do not support indexing.

print(3 in my_set)  # this will print True because 3 is present in the set.

print(len(my_set))  # this will print 6 because there are 6 unique elements in the set.

list = [1, 2, 3, 4, 5, 5, 6, 6]

print(
    set(list)
)  # here it will print {1, 2, 3, 4, 5, 6} because sets do not allow duplicates.
