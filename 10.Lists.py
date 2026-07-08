# Lists

li = [
    "amazon",
    2,
    "facebook",
    4.5,
    True,
]  # Lists are the data type where we can store the multiple
# values of diff data types

print(li)

# List Slicing
# so like strings we can slice the lists too

print(li[1])  # here it will print the second index value of list
print(
    li[0:4:2]
)  # here it will print the lists from first to 3rd index while print every 2nd
# list value

# Unlike strings , Lists are Mutable
# Like we can change the indexes of lists

li[1] = "vishu"

print(li)  # so here it will change the second value of list to whatever given

vi = li

vi[1] = "google"

print(
    vi, li
)  # now here what will happen that both lists become equal and whatever will
# change to vi it will also alter the li. so if we want to assign a list to
# another list we have to use '[:]' so that it should not alter the original list
