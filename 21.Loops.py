# LOOPS

for item in 'Hello World':
    print(item) #Here we are iterating through each character in the string 'Hello World' and printing it one by one.

for item in [1,2,3] :
    print(item) #Here we are iterating through each element in the list [1,2,3] and printing it one by one.

for item in [1,2,3]:
    for x in 'Hello':
        print(item, x) #Here we are using nested loops. The outer loop iterates through the list [1,2,3] and the inner loop iterates through each character in the string 'Hello'. For each iteration of the outer loop, the inner loop runs completely, printing the current item from the list along with each character from the string.

# Iterating through Dictionaries

user = {
    'name': 'John', 
    'age': 25,
    'is_boy': True
}

for item in user:
    print(item) #Here we are iterating through the keys of the dictionary 'user' and printing each key one by one.

for item in user.items():
    print(item) #Here we are iterating through the items of the dictionary 'user' and printing each key-value pair as a tuple.

for item in user.keys():
    print(item) #Here we are iterating through the keys of the dictionary 'user' using the .keys() method and printing each key one by one.

for item in user.values():
    print(item) #Here we are iterating through the values of the dictionary 'user' using the .values() method and printing each value one by one.

for key, value in user.items():
    print(key, value) #Here we are using tuple unpacking to iterate through the items of the dictionary 'user'. For each key-value pair, we print the key and its corresponding value.
    