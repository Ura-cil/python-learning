a=int(input("enter the number a: "))
isprime=1
for i in range (2,a):
    if (a%i)==0:
        isprime=0
        break
if(isprime)==1:
    print("number is prime")  

else:
    print("not prime")    
    

