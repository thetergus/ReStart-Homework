from .MyShape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius

    def area(self):
        return math.pi * self.radius**2 # or math.pi * (self.radius*self.radius)