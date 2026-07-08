# Types of String and String Operations
First_Name = "Vishwadev"
Last_Name = "Gupta "

# this is a long string , like we can store paras and long strings or texts
# in it by using " ''' "
Long_String = """  
Hi WHats up
I am good 

0 0
---

-     -
 -   -
  - - 
   -
"""

print(Long_String)
print(
    First_Name + " " + Last_Name
)  # By this way we can add two diffrent strings or we can say
# String Concatenation

# Escape Sequence
str = 'it\'s a "good day" bro '
print(str)
# so here \ is a escape sequence without this it was not
# possible to write this kind of string
# Now let's assume we want to give a huge space before a string and we want to print a part of
# a string in next line how will we do it. So for that we have diffrent type of escape sequence

str2 = "\t hi guys \n how are you"  # \t will give the extra space before sentence and \n for new line
print(str2)

# formatted strings
name = "Vishwadev"
age = 22

print(f" Hi {name}, you are {age} years old")
print(" Hi {}, you are {} years old".format(name, age))
print(" Hi {1}, you are {0} years old".format(name, age))

# STRING INDEXES
# So Lets say we have a string "word " and we want to access the 2nd letter of the string how
# do we access that , or we can print that !

string = "01234567"  # its an example how string are places in memory
print(string[2])  # if we want to print the second place charcter in string
print(
    string[0:4]
)  # if we want to print the character palced between 0 place to 4th place
print(
    string[0:4:2]
)  # if we want to print the string from 0th place to 4th place and need to
# stepup om every second character
print(
    string[-1]
)  # now the string will start from the end , like if we print string[-2] it
# will print the second last word.

# IMMUTABILITY
# so it means that string in python are immutable

imstring = (
    "immutable"  # so her if we want to change this value of the string we have to
)
# reassign the whole value of string but if we want to replace a char in
# the exixting string index , we can't do that cz strings are immutable for e.g.
# imstring [2] = 'r'  so this operation can't be performed but if we want to add a extra char then
# we can do it for e.g.
imstring = (
    imstring + "i"
)  # here it will add one char after the existing string , and it will become
# a new string
print(imstring)
