class GameValidator(object):
    def validateSize(self, size):
        if size not in range(3, 31):
            raise ValueError("Size needs to be 3-30")
    def validateWinSize(self, boardSize, winSize):
        if winSize not in range(3, boardSize + 1):
            raise ValueError("Win size needs to be from 3 to the board size")
