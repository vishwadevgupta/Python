#CONDITIONAL BLOCKS (IF ELSE)

is_Boy = True
is_above_18 = True

if is_Boy: # Here it will check if the variable is_Boy is True or not.
           #if the value of is_Boy is true it will goes inside the if block otherwise 
           # it will pass to the next elif block.  
    print("You are a boy")
elif is_above_18: # it will also work like if block but it will only execute 
                  #if the above if block is false and the condition of elif is true.
    print("You are a man")
else:  # it will execute if all the above conditions are false.
    print("You are a child")

