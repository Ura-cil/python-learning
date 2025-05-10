# Exercise 6: Create a recursive function
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself repeatedly.

# Expected Output:


# 55

counter = 10

def rec(a,b):
    counter -= 1
    if counter == 0:
        return
    sum = a + b
    print(sum)
    rec(b, sum)


rec(0,1)   
# a b sum
# 0 1 1
# 1 1 2
# 1 2 3
# 2 3 5
# 3 5 8