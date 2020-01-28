class Player(object):
    def __init__(self, id, visualRepresentation):
        self._id = id
        self._visualRepresentation = visualRepresentation

    @property
    def ID(self):
        return self._id

    @ID.setter
    def ID(self, id):
        self._ID = id

    @property
    def VisualRepresentation(self):
        return self._visualRepresentation

    @VisualRepresentation.setter
    def VisualRepresentation(self, visualRepresentation):
        self._visualRepresentation = visualRepresentation

class Human(Player):
    def __init__(self, id, visualRepresentation):
        Player.__init__(self, id, visualRepresentation)

class Computer(Player):
    def __init__(self, id, visualRepresentation):
        Player.__init__(self, id, visualRepresentation)