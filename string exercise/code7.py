# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

# Given:

# Case 1:

# s1 = "Yn"
# s2 = "PYnative"
# Expected Output:


# Case 2:

# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output:
#true
# False

s= "PYnative"
s2="yn"
flag=True

for char in s:
    if char in s2:
        continue
    else:
        flag=False   
print(flag)        




