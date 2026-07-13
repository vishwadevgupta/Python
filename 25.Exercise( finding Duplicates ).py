# FIND DUPLICATES IN LIST
# 1. Solution (without using anything just loops and ifs)

NList = ['a','c','b','a']
DList = []
i = 0
j = 0 
counter =0
for items in NList:
    i=0 
    for items2 in NList:
        if i != j:
            if items2 == items:
                if items2 not in DList:
                    DList.append(items2)
        i += 1
    j+= 1
print (DList)

#2 Using Enumerates

NList = ['a','c','b','a','e','f','j','c','k','f']
DList = []
for i,items in enumerate(NList):
    for j,items2 in enumerate(NList):
        if i != j and items2 == items and items2 not in DList:
            DList.append(items2)
print(DList)

#3 using count function;

NList = ['a','c','b','a','e','f','j','c','k','f']
DList = []

for items in NList:
    if NList.count(items) > 1 and items not in DList:
        DList.append(items)

print(DList)

            
        