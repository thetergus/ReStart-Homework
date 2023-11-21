import math
from Shapes.MyTriangle import Triangle
from Shapes.MySquare import Square
from Shapes.MyRectangle import Rectangle
from Shapes.MyCircle import Circle

def create_triangle():
    A=int(input("Enter the llenght of side A of the triangle: "))
    B=int(input("Enter the llenght of side B of the triangle: "))
    C=int(input("Enter the llenght of side C of the triangle: "))
    print(f"Triangle sides input {A},{B},{C}")

    assert (A+B>C), "Incorrect values, inequality theorem must be respected to geta valid triangle, A+B is not bigger than C"
    assert (A+C>B),  "Incorrect values, inequality theorem must be respected to geta valid triangle, A+C is not bigger than B"
    assert (B+C>A), "Incorrect values, inequality theorem must be respected to geta valid triangle, B+C is not bigger than A"
    #or just one asert as bellow, but it does not help you pinpoint which case scenario was incorrect:
    #assert (A+B>C) and (A+C>B) and (B+C>A), "Incorrect values, inequality theorem must be respected to geta valid triangle"
    return Triangle(A,B,C)

def create_square():
    squareSide=int(input("Enter the lenght of the side of the Square: "))
    print(f"Square  side input {squareSide}")
    assert (squareSide>0), "Incorrect values, side has to be higher than 0"
    return Square(squareSide)

def create_rectangle():
    length=int(input("Enter the length of the rectangle: "))
    width=int(input("Enter the width of the rectangle: "))
    print(f"Rectangle lenght and width input {length},{width}")
    assert length>0 and width>0, "Incorrect values, both lenght and width have to be above 0"
    return Rectangle(length,width)

def create_circle():
    radius=int(input("Enter the radius of your circle: "))
    print(f"Circle's radius input {radius}")
    assert radius>0, "Incorrect values, radius has to be higher than 0"
    return Circle(radius)

def choose_your_destiny():
    print("Choose your destiny:")
    print("1. Create a Triangle.    ▲")
    print("2. Create a Square      ■")
    print("3. Create a Rectangle ▬ (not square)")    
    print("4. Create a your circle ●")

    option = int(input("Enter your choice (1-4): "))
    print(f'your option was {option}')
    assert 1 <= option <= 4, "Invalid choice. Please enter a number between 1 and 4."
    return option

def main():
    while True:
        destiny = choose_your_destiny()

        if destiny == 1:
            triangle = create_triangle()
            print(f"Triangle Area ▲: {triangle.area()}")
            break

        elif destiny == 2:
            square  = create_square()
            print(f"Square Area ■: {square.area()}")
            break

        elif destiny == 3:
            rectangle=create_rectangle()
            print(f"Rectangle Area ▬: {rectangle.area()}")
            break

        elif destiny == 4:
            circle=create_circle()
            print(f"Circle Area ●:{circle.area()}")
            break

if __name__=="__main__":
    main()