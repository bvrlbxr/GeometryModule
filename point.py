class Point:
    def __init__(self, x: float, y: float):
        self.coord = (x, y)

    def __repr__(self):
        return "Point(%s, %s)" % self.coord
