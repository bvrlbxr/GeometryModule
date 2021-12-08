from geometry.point import Point

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.points = (point1, point2)

    def __repr__(self):
        return "Line(%s, %s)" % self.points

    def length(self):
        return ((self.points[1].coord[0] - self.points[0].coord[0]) ** 2 +
                (self.points[1].coord[1] - self.points[0].coord[1]) ** 2) ** 0.5




