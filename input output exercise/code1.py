# Exercise 1: Format Output String
# Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.

# Use the print() function to format the given words in the specified format. Display the ** separator between each string.

# Expected Output:

# For example: print('your code') should display My**Name**Is**James

a = []

for i in range(1,5):

    a.append(input(", "))


for e in a:
    print(e, end="**")