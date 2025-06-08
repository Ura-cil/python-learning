class employee:
    def __init__(self):
        self.name ="uracil"
        self.__name ="uracil"

a=employee()
print(a.name)
print(a._employee__name)
# print(a.__dir__())

# a.emp1 = 5