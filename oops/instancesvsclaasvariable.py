class employee:
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
    def showdetails(self):
        print(f"the name of thr employee is {self.name} and the raise value is {self.raise_amount}")     
emp1 = employee("uracil")        
emp1.raise_amount = 0.3
emp1.showdetails()

emp2 = employee("harry")        
emp2.showdetails()

# employee.showdetails(emp1)

