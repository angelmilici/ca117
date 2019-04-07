class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = int(goals)
        self.points = int(points)

    def __str__(self):
        return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)

    def total(self):
        return self.points + self.goals * 3

    def __eq__(self, s2):
        return self.total() == s2.total()

    def __lt__(self, s2):
        return self.total() < s2.total()

    def __gt__(self, s2):
        return self.total() > s2.total()

    def __ge__(self, s2):
        return self.total() >= s2.total()

    def __le__(self, s2):
        return self.total() <= s2.total()

    def __add__(self, s2):
        return Score(self.goals + s2.goals, self.points + s2.points)

    def __sub__(self, s2):
        return Score(self.goals - s2.goals, self.points - s2.points)

    def __iadd__(self, s2):
        self.goals += s2.goals
        self.points += s2.points
        return self

    def __isub__(self, s2):
        self.goals -= s2.goals
        self.points -= s2.points
        return self
