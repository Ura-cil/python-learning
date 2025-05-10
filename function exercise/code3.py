# Exercise 3: Return multiple values from a function
# Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.

# Given:

# def calculation(a, b):
#     # Your Code

# res = calculation(40, 10)
# print(res)
# Expected Output

# 50, 30


def calculation(a,b):
    add=a+b
    sub=a-b
    print(add,",",sub)

if __name__ == '__main__' :
     

     calculation(40,10)
  