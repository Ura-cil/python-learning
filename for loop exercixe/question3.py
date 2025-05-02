# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)



a=int(input(" enter the number a: "))
sum=0

for i in range(a):
    sum=sum+i+1
print(sum)


## best approach:


print(a*(a+1)/2)



