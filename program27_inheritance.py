class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area of Shape")


class Triangle(Shape):
    def area(self):
        result = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle:", result)


class Rectangle(Shape):
    def area(self):
        result = self.dim1 * self.dim2
        print("Area of Rectangle:", result)


t1 = Triangle(7, 5)
t1.area()

r1 = Rectangle(4, 8)
r1.area()
