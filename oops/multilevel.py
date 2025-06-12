class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")
class dog(animal):
    def __init__(self, name, species,breed):
        animal.__init__(name, species="dog")
        self.breed = breed
    def show_details(self):
        animal.show_details(self)
        print(f"breed:{self.breed}")
class goldenretriever(dog):
    def __init__(self, name, color):
        dog.__init__(name, species="golden retriever")
        self.color = color
    def show_details(self):
        dog.show_details(self)
        print(f"color:{self.color}")
o = goldenretriever("tommy","black")
o.show_details()

# dog.show_details(self)
# print(f"color:{self.color}")
