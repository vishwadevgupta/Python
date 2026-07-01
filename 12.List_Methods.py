Basket = [1,2,3,4,5]

#adding methods

Basket.append(12) # it will add a item at the end of list
Basket.insert(3,16) # it will insert a item at 3rd index
Basket.extend([10,11,12,123]) # it will extends the lists 
print (Basket)

#removing methods

Basket.pop() # it will remove the value at last index of list by default.
print(Basket)
Basket.pop(1) # if we give the index value, it will remove the value at that index.
print(Basket)
Basket.remove(5) # it will remove the value 5 from the list 
print(Basket)
Basket.clear() # it will clear down the whole list
print(Basket)

# count/index methods 

Basket2 = ['a','b','c','d','e','a','z','f']
print(Basket.index(2,0,4)) # here we are checking the indev value of 2 between the index 0 to 4
print ('c' in Basket2) # here we will check if the char d is present in the list or not, it will
                       # return bool
print (Basket2.count('a')) # this method will count that how many times do a value occur in list

# Sorting methods

Basket2.sort() # here it will sort the list .
Basket2.reverse() # here it will just print the reversed list , it will not sort !