while 1:

    a=int(input("Enter number a: "))
    b=int(input("Enter number b: "))
    c=int(input("Enter number c: "))
    if c>=1:
        print(a)
    if c>=2:
        print(b)

    for i in range(c-2):
        num=a+b
        a=b
        b=num
        print(num)
    