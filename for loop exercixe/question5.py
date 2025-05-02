# Exercise 5: Count the total number of digits in a number
# Write a Python program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.


a=int(input("emter the number: "))
# print(a)
count=0
while(a!=0):
    a=a//10
    count=count+1
print(count)


