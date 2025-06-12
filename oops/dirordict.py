#dir :

x = [1,2,3]
print(dir(x))

print(x.__add__)
# dict:

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = person("uracil",16)
print(p.__dict__)
print(help(person))     


