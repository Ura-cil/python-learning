# Exercise 3: Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.

# Given:

# et1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}s
# Expected output:

# {70, 40, 10, 50, 20, 60, 30}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))

