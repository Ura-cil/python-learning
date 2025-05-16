# xercise 3: Create a new string made of the first, middle, and last characters of each input string # type: ignore
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# Given:

# s1 = "America"
# s2 = "Japan"
# Expected Output:

# AJrpan

s1 = "America"
s2 = "Japan"

index1=len(s1)
index1=len(s2)

jump1 = len(s1) // 2 

a=s1[::jump1]

jump2 = len(s2) // 2 

b=s2[::jump2]


print(a[:]+b[:])
