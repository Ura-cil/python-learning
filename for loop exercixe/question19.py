# Exercise 22: Find largest and smallest digit in a number
# Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.

# Input:

# num1 = 9876543210
# num2 = -5082
# Output:


# Largest digit in 9876543210: 9
# Smallest digit in 987654321: 1

# Largest digit in -5082: 8
# Smallest digit in -5082: 0

num1 = 9876543210
num2 = -5082


num1=str(num1)
num2=str(num2)

 
for num in [num1, num2]:
    
    max = 0  
    min = 0
    for e in num:
        if e.isdigit() and int(e) > max:
            max=int(e)

        if e.isdigit() and int(e) < min:
            min=int(e)
    print(num, ": ")
    print(max) 
    print(min)   






