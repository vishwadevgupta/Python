# Types of String and String Operations
First_Name = 'Vishwadev'
Last_Name = 'Gupta '

# this is a long string , like we can store paras and long strings or texts
# in it by using " ''' "
Long_String = '''  
Hi WHats up
I am good 

0 0
---

-     -
 -   -
  - - 
   -
'''

print(Long_String)
print (First_Name + ' ' + Last_Name) # By this way we can add two diffrent strings or we can say 
                                     # String Concatenation

#Escape Sequence
str = "it's a \"good day\" bro "
print(str)
 # so here \ is a escape sequence without this it was not 
 # possible to write this kind of string
# Now let's assume we want to give a huge space before a string and we want to print a part of 
# a string in next line how will we do it. So for that we have diffrent type of escape sequence

str2 = "\t hi guys \n how are you" # \t will give the extra space before sentence and \n for new line
print(str2) 

#formatted strings
name = "Vishwadev"
age = 22

print(f" Hi {name}, you are {age} years old")
print(" Hi {}, you are {} years old".format(name,age))
print(" Hi {1}, you are {0} years old".format(name,age))