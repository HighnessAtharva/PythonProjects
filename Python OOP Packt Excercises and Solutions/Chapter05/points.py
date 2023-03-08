import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def perimeter(polygon):
    points = polygon + [polygon[0]]
    return sum(distance(points[i], points[i+1]) for i in range(len(polygon)))


square = [(1,1), (1,2), (2,2), (2,1)]
perimeter(square)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

class Polygon:
    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        points = self.vertices + [self.vertices[0]]
        return sum(points[i].distance(points[i+1]) for i in range(len(self.vertices)))


square = Polygon()
square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))
square.perimeter()

class Polygon2(Polygon):
    def __init__(self, points=None):
        points = points or []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)
