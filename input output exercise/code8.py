# Exercise 8: Percentage Display
# Ask the user for a numerator and a denominator. Calculate the percentage and display
#  it with two decimal places followed by a percent sign (e.g., 75.50%).


num=int(input("enter the numerator: "))
den=int(input("enter the denominator: "))

value= ((num-den)/num)*100

print("%.2f" % value)

