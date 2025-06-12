class employee:
    
    def __init__(self,name ,salary):
        self.name= name
        self.salary = salary

    @classmethod
    def str(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
string = "john-12000"
e1 = employee.str(string)   
print(e1.name)
print(e1.salary)   
    
        
string = "uracil-12000"
e2 = employee.str(string)   
print(e2.name)
print(e2.salary)   

string = "slovish-122000"
e3= employee.str(string)   
print(e3.name)
print(e3.salary)     
