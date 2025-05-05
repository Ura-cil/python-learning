

def prime(a):
    
    isprime=1
    for i in range(2,a):
        if a%i == 0:
            isprime = 0
            break
    return isprime

if prime(2) == 1:
    print("number is prime")
else:
    print("not prime")           



