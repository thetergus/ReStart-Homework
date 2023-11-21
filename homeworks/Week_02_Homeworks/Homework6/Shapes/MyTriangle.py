from .MyShape import Shape
import math

class Triangle(Shape):
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def area(self): #Heron's formula cause I am using sides, not base and height. 
        SP =(self.A + self.B + self.C)/2                                                        #semi perimeter (s = (a + b + c)/2.)
        triangleArea = math.sqrt(SP * (SP-self.A)*(SP-self.B)*(SP-self.C))   #(A = √[s(s-a)(s-b)(s-c)])
        return triangleArea