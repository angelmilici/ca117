from random import randint
class Coin(object):

    def __init__(self, sideup='Heads'):
        self.sideup = sideup

    def flip(self):
        if randint(0,1) == 0:
            self.sideup = 'Tails'
        else:
            self.sideup = 'Heads'

    def getstate(self):
        return self.sideup

    def __str__(self):
        return 'Current state: {:}'.format(self.getstate())
