# OOP Exercise 10: Calculate the area of different shapes using OOP
# Given:

# You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.


# Now, Write a OOP code to calculate the area of each shapes (each subclass must write its own implementation of area() method to calculates its area).

# Use the following code

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):  
        return 3.14159 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side*self.side


# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area()) 

