class Triathlete(object):

    def __init__(self, name, id_number):
        self.name = name
        self.tid = id_number
        self.d = {}

    def __str__(self):
        return 'Name: {:s}\nID: {:d}\nRace time: {:d}'.format(self.name, self.tid, sum(self.d.values()))

    def add_time(self, s, t):
        self.d[s] = t

    def get_time(self, s):
        return self.d[s]

    def __eq__(self, other):
        return (sum(self.d.values()) == sum(other.d.values()))

    def __gt__(self, other):
        return (sum(self.d.values()) > sum(other.d.values()))

    def __lt__(self, other):
        return (sum(self.d.values()) < sum(other.d.values()))
