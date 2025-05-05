# Exercise 21: Flatten a nested list using loops
# Write a program to flatten a nested list using loops.

# Given:

# nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

# # write function 'flatten_list' to flatten a nested list
# flattened = flatten_list(nested_list)
# print("Flattened list:", flattened)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



flatten_list=[] #variable intialize

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]    #list

#one by one going to elmwnt of an nested list
for e in nested_list:

    if isinstance(e, list): #if statement to check wheter e is an list or not

        for g in e: # for loop to append elment oof master list elment
            flatten_list.append(g)
    else:

        flatten_list.append(e)    
        
         
print(flatten_list)
            

