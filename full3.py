import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 +(self.y - other_point.y)**2)
        return distance
        

    def get(self):
        return(self.x, self.y)
        

    def set(self, x, y):
        self.x = x
        self.y = y


point1 = Point(2, 4)
point2 = Point(5, 1)

print(point1.get())
print(point2.get())

print(point1.distance(point2))

point1.set(2, 3)
print(point1.get())
