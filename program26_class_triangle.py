class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        area = 0.5 * self.base * self.height
        print("Area =", area)


t1 = Triangle(7, 5)
t1.calculateArea()
