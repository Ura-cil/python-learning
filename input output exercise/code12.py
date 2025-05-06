# Exercise 15: Padding with Zeros
# Ask the user for a number. Print this number padded with leading zeros to a width of 5.

# For example, if the input is 12, the output should be “00012“

a = input("enter the number")

# len = len(a)

val = 5-len(a)
print("0"*val + a)
