# Exercise 6: Accept any three string from one input() call
# Write a program to take three names as input from the user in a single call to the input() function.

# See: Get multiple inputs from a user in one line

# Expected Output

# Enter three string Emma Jessa Kelly
# Name1: Emma
# Name2: Jessa
# Name3: Kelly

# name=[]

# for i in range(1,4):

#     a=input(":")
#     name.append(a)


# print(name)


str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)





