def my_genertor():
    for i in range(50):
        yield i 

gen = my_genertor()
for j in gen:
    print(j)
