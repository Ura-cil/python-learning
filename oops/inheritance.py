class employee:
    def __init__(self,name,id):

        self.name = name
        self.id = id

    def showdetails(self):
        print(f"the name of employee : {self.id} is {self.name}")   
class programmer(employee):
    def showlanguage(self):
        print("the default lang is py")


e1 = employee("rohan as",400)
e1.showdetails()
e2 = programmer("harry",4100)
# e2 = employee("uracil",4001)
e2.showdetails()
e2.showlanguage()


