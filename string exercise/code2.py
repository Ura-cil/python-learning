# 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

# Given:

# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:

# AuKellylt
# new_string = original_string[:index] + string_to_append + original_string[index:]



s1 = "Ault"
s2 = "Kelly"

index=len(s1)//2 

a = s1[:index] + s2 + s1[index:]
print(a)
