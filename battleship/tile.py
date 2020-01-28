class Tile(object):
    def __init__(self):
        self._value = None
        self._visualRepresentation = "o"
        self._discovered = False

    @property
    def Value(self):
        return self._value

    @Value.setter
    def Value(self, value):
        self._value = value

    @property
    def VisualRepresentation(self):
        return self._visualRepresentation

    @VisualRepresentation.setter
    def VisualRepresentation(self, visualRepresentation):
        self._visualRepresentation = visualRepresentation

    @property
    def Discovered(self):
        return self._discovered

    @Discovered.setter
    def Discovered(self, discovered):
        self._discovered = discovered