class Point(object):
    """Creates a point on a coordinate plane with values x and y."""
    COUNT = 0

    def __init__(self, _x, _y):
        """Defines x and y variables"""
        self.x = _x
        self.y = _y

    def move(self, dx, dy):
        """Determines where x and y move"""
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y)

    def change_coord(self, _x, _y):
        self.x = _x
        self.y = _y
