class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

example1 = Shape()
print(example1.area())

example2 = Rectangle(5, 10)
print(example2.area())