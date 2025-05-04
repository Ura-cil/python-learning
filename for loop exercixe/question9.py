# Exercise 11: Print all prime numbers within a range
# Note: A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)

# A Prime Number is a natural number greater than 1 that cannot be made by multiplying other whole numbers.

# Examples:

# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply to make it.

# Given:

# # range
# start = 25
# end = 50
# Expected output:

# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47
start=25
end=50

for num in range(start, end+1):
    isprime = 1

    for i in range(2,num):

      if num%i == 0:
        isprime = 0
        break
    if isprime == 1:
       print(num)
    
 


    
        