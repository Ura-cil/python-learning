class person:
    def __init__(self,name ,occ):#constructor
        self.name = name
        self.occ = occ
        print("hey i am a person")

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("harry","developer") 
b = person("gaurav","hr")
a.info()
b.info()
