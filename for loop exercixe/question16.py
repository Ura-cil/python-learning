# Exercise 17: Find the sum of a series of a number up to n terms
# Write a program to calculate the sum of this series up to n terms. For example, if the number is 2 and the number of terms is 5, then the series will be 2+22+222+2222+22222=2469

# Given:

# # number of terms
# num = 2
# terms = 5
# Expected output:

# 24690

sum=0
num=int(input("enter the number"))
temp = num
term=int(input("enter the term"))
for i in range(term):
    sum=sum+temp
    temp=temp*10 + num
    print(temp,"      ",sum)
print (sum)    
    


