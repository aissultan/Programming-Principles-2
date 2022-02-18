import math

class Point:
    def __init__(self, x, y):
        self.x_1 = x
        self.y_1 = y

    def show(self):
        print(self.x_1, self.y_1)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self):
        self.x1 = self.x_1
        self.y1 = self.y_1
        self.x2 = self.x
        self.y2 = self.y
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

x, y = map(int, input().split())
point1 = Point(x, y)   
point1.show()
x1, y1 = map(int, input().split())
point1.move(x1, y1)
print(point1.dist())