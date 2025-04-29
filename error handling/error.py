a=(input("enter the number:  "))


try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("sorry some error occurred")       
    print("invalid input") 