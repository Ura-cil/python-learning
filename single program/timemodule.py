import time

def usingwhile():
    i= 0
    while i < 50000:
        i = i+1
        print(i)
def usingfor():
    for i in range(50000):
        print(i)


# init = time.time()
# usingfor()
# t1 = time.time()-init


# init = time.time()
# usingwhile()
# print(time.time()-init)
# print(t1)


print(4)
time.sleep(5)
print("this is printed after 3 sec")


t = time.localtime()
timeime = time.strftime("%y-%m-%d %H:%M:%S",t)

print(timeime)
