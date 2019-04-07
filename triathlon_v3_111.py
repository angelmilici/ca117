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

    def __str__(self):
        l = []
        for e in sorted(self.d.values(), key=lambda x: x.name):
            l.append('Name: {:s}'.format(e.name))
            l.append('ID: {:d}'.format(e.tid))
        return '\n'.join(l)

    def best(self):
        return min(self.d.values(), key=lambda x: x.race_times)

    def worst(self):
        return max(self.d.values(), key=lambda x: x.race_times)

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}
        self.race_times = 0

    def __str__(self):
        return 'Name: {:s}\nID: {:d}\nRace time: {:d}'.format(self.name, self.tid, sum(self.d.values()))

    def add_time(self, s, t):
        self.d[s] = t
        self.race_times += t

    def get_time(self, s):
        return self.d[s]

    def __eq__(self, other):
        return (sum(self.d.values()) == sum(other.d.values()))

    def __gt__(self, other):
        return (sum(self.d.values()) > sum(other.d.values()))

    def __lt__(self, other):
        return (sum(self.d.values()) < sum(other.d.values()))
