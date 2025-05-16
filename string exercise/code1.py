# Write a program to create a new string made of an input string’s first, middle, and last character.

# Given:

# str1 = "James"
# Expected Output:

# Jms

str1 = "Jameshfhfhg"
end = len(str1) - 1

mid =  end // 2


print(str1[0] + str1[mid] +str1[end])


jump = len(str1) // 2 

print(str1[::jump])
