class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.lentgh = length

    def area(self):
        return self.lentgh * self.lentgh

example1 = Shape()
print(example1.area())

example2 = Square(5)
print(example2.area())




