# Exercise 5: Create an inner function
# Create a program with nested functions to perform an addition calculation as follows:

# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def outFun(a,b):

    def add(p,q):
        return p+q
    

    sum = add(a,b) 

    return sum + 5


print(outFun(5,10))