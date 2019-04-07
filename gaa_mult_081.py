class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = int(goals)
        self.points = int(points)

    def __str__(self):
        return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)

    def total(self):
        return self.points + self.goals * 3

    def __mul__(self, s2):
        return Score(self.goals * s2, self.points * s2)

    def __gt__(self, s):
        return self.total() > s.total()

    def __rmul__(self, s2):
        return Score(s2 * self.goals, s2 * self.points)

    def __imul__(self, s2):
        self.goals *= s2
        self.points *= s2
        return self

    def __eq__(self, s2):
        return self.total() == s2.total()
