
# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class vehicle:
    capacity = 4
    def __init__(self,max_speed,mileage,name):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
a = vehicle(150,50, "abc")
a2 = vehicle(15,20, "pqr")
a.capacity=6
print(a.max_speed,a.mileage,a.capacity)


