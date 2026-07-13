# WHILE LOOPS

i = 0

while (
    i < 10
):  # here is the condition of while loop that i will run until i is less than 10
    print(i)
    i += 1  # here the value of i is incremented by 1 after each iteration of the loop, so that eventually the condition will become false and the loop will stop running.

# USE OF BREAK STATEMENT
j = 0

while j < 10:
    print(j)
    if j == 5:  # here the break statement is used to exit the loop when j is equal to 5
        break
    j += 1

# USE OF CONTINUE STATEMENT


k = 0
while k < 10:
    k += 1
    if (
        k == 5
    ):  # here if k is equal to 5, the continue statement will skip the rest of the code in the loop and move on to the next iteration of the loop. means it will go to the while loop and check the condition again, if it is true then it will run the loop again.
        continue
    print(k)
