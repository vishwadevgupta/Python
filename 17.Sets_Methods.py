# Sets_Methods

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(
    set1.difference(set2)
)  # it will give the diffrence of set1 by comparing with set2.

print(set1.discard(3))  # it will remove the element 3 from set1.

print(
    set1.diffrence_update(set2)
)  # it will remove the elements from set1 which are present in set2.

print(set1.intersection(set2))  # it will give the common elements of set1 and set2.
print(set1 & set2)  # it will give the common elements of set1 and set2.

print(set1.isdisjoint(set2))  # it will check if set1 and set2 have no common elements.

print(
    set1.issubset(set2)
)  # it will check if set1 is a subset of set2. here subset means all the elements of set1 are present in set2.

print(
    set1.issuperset(set2)
)  # it will check if set1 is a superset of set2. here superset means all the elements of set2 are present in set1.

print(
    set1.union(set2)
)  # it will give the union of set1 and set2. here union means all the elements of set1 and set2 without any duplicates.
print(set1 | set2)  # it will give the union of set1 and set2.
