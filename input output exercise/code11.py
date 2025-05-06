# Exercise 14: Tabular Output from Lists
# You have two lists: names = ["Alice", "Bob", "Charlie"] and names = ["Alice", "Bob", "Charlie"]. Print these lists as a simple table with columns “Name” and “Score”.

# Expected Output:

# Name       Score
# ------------------
# Alice      85   
# Bob        92   
# Charlie    78 

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score':<5}")
print("-"*20)

for i in range(len(names)):
    print(f"{names[i]:<10}{scores[i]:<5}")