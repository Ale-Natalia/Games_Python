class Player(object):
    def __init__(self, signToDisplay):
        self._signToDisplay = signToDisplay

    @property
    def SignToDisplay(self):
        return self._signToDisplay

    @SignToDisplay.setter
    def SignToDisplay(self, sign):
        self._signToDisplay = sign

class Human(Player):
    def __init__(self, signToDisplay):
        Player.__init__(self, signToDisplay)

class Computer(Player):
    def __init__(self, signToDisplay):
        Player.__init__(self, signToDisplay)