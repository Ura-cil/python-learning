class person:
    name = "harry"
    occupation = "software developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()

a.name = "gaurav"
a.occupation= "CA"
a.name = "hh"
a.occupation= "hr"

# print(a.name,a.occupation)   
 
a.info()