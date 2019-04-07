class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, athlete):
        self.d[athlete.tid] = athlete

    def remove(self, tid):
        del self.d[tid]

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        return None

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
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
