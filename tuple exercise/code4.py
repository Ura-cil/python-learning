# Exercise 5: Swap two tuples in Python
# Given:

# tuple1 = (11, 22)
# tuple2 = (99, 88)
# Expected output:

# tuple1: (99, 88)
# tuple2: (11, 22)

tuple1 = (11, 22)
tuple2 = (99, 88)

a,b=tuple1
c,d = tuple2

a,b = c, d

print(tuple1)

print(tuple2)