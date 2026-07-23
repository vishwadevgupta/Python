# HIGHEST EVEN FUCNTION


def high_even(li):
    high = 0
    for num in li:
        if num % 2 == 0 and num > high:
            high = num
    return high


print(high_even([1, 2, 4, 3, 8, 6]))


# if we have negative numbers in the list.


def high_even(li):
    high = None
    for num in li:
        if num % 2 == 0:
            if high is None or num > high:
                high = num
    return high


print(high_even([1, 2, 4, 3, 8, 6]))
