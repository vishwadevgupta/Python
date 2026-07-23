#FUNCTIONS
# the functions are generally used to perform specific tasks and can be reused throughout the code. They help in organizing the code and making it more readable and maintainable.

def add_numbers():
    a = 5
    b = 10
    print ("The sum of", a, "and", b, "is:", a + b)

add_numbers() # here we are calling the function to execute it and print the sum of 5 and 10.

# ARGUMENTS AND PARAMETERS

def add_numbers(a,b): #here we are defining a function called add_numbers that takes two parameters a and b.
    print ("The sum of", a, "and", b, "is:", a + b)

add_numbers(5, 10) # here are are passing the values 5 and 10 as arguments to the function add_numbers.

# Default Parameters

def add_numbers(a=5,b=10): #here we are defining a function called add_numbers that takes two parameters a and b with default values of 5 and 10.
    print ("The sum of", a, "and", b, "is:", a + b) 

# Positional Arguments
add_numbers(5, 10) # here we are passing the values 5 and 10 as positional arguments to the function add_numbers.

#Keyword Arguments
add_numbers(b=10, a=5) # here we are passing the values 5 and 10 as keyword arguments to the function add_numbers.

add_numbers(5) # here we are passing the value 5 as a positional argument to the function add_numbers. The default value of b will be used.

# RETURN 

def multiply_numbers(a,b): #here we are defining a function called multiply_numbers that takes two parameters a and b.
    return a * b # here we are returning the product of a and b.

print(multiply_numbers(5, 10)) # here we are calling the function multiply_numbers and passing the values 5 and 10 as arguments. The returned value will be printed.