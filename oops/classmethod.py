class employee:
    company ="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    @classmethod #clss method
    def changecompany(cls,newcompany):
        cls.company = newcompany

e1 =employee()
e1.name = "uracil"
e1.changecompany("tesla")
e1.show()
e2=employee()
e2.name = "harry"
e2.show()
print(employee.company)



