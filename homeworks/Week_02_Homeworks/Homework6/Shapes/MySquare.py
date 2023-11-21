from .MyShape import Shape

class Square(Shape):
    def __init__(self, squareSide):
        self.squareSide = squareSide

    def area(self):
        squareArea=self.squareSide**2
        return squareArea  # deleting previous line and returning 'self.squareSide*self.squareSide' should  also be  valid