class Score(object):

    def __init__(self, goals=0, points=0):
        self.g = goals
        self.p = points

    def greater_than(self, s2):
        return (self.p + self.g * 3) > (s2.p + s2.g * 3)

    def less_than(self, s2):
        return (self.p + self.g * 3) < (s2.p + s2.g * 3)

    def equal_to(self, s2):
        return (self.p + self.g * 3) == (s2.p + s2.g * 3)
