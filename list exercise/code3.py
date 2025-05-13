# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.


# Expected output:

# [1, 4, 9, 16, 25, 36, 49]



l1=[1,2,3,4,5,6,7]

list3 = [i * j for i, j in zip(l1,l1)]
print(list3 )