#  1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 

for i in range (5):
    for j in range(i+1):
        print(j+1, end=' ')
    print('')


a=5
for i in range (a):
    for j in range (i+1):
        print("*", end =" ")
    print("")    


for i in range(5,0,-1):
    for j in range (i):
        print("*", end =" ")
    print("")    

print('best approach: ')
for i in range(a):
    print('* '*(i+1))


a = "s"*5
print(a)

# 1 
# 2 3 
# 4 5 6 
# .....

b=5
sum=1

for i in range(b):
    for j in range(i+1):
        print(sum, end=" ")
        sum +=1
    print("")    
    