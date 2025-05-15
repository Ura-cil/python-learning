# Exercise 2: Access value 20 from the tuple
# The given tuple is a nested tuple. write a Python program to print the value 20.

# Given:

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# Expected output:

# 20
# tuple1 = ("Orange", [10, 30,20], (5, 15, 25))
# print(tuple1[1][2])


def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))

