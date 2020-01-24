class Tile(object):
    def __init__(self, visualRepresentation):
        self._status = "undiscovered"
        self._value = None
        self._visualRepresentation = "."
        self._searchedThrough = False

    @property
    def Status(self):
        return self._status

    @Status.setter
    def Status(self, status):
        self._status = status

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
    def SearchedThrough(self):
        return self._searchedThrough

    @SearchedThrough.setter
    def SearchedThrough(self, searchedThrough):
        self._sarchedThrough = searchedThrough