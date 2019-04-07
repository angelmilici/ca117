class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def midpoint(self, p2):
        return Point((self.x + p2.x) / 2, (self.y + p2.y) / 2)

    def __str__(self):
        return 'Centre: ({:.1f}, {:.1f})'.format(self.x, self.y)

class Circle(object):
    
    def __init__(self, radius=0, centre=Point(0,0)):
        self.radius = radius
        self.centre = centre

    def __add__(self, c2):
        self.centre = 
