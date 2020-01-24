from domain import Tile
import random

class GamePlay(object):
    def __init__(self, gameBoard, validator):
        self._gameBoard = gameBoard
        self._validator = validator

    @property
    def VisualBoardForPlayer(self):
        return self._gameBoard.VisualBoardForPlayer

    @property
    def VisualBoardComplete(self):
        return self._gameBoard.VisualBoardComplete

    def playerWon(self):
        numberOfDiscoveredTiles = 0
        for rowCoordinate in range(self._gameBoard.Height):
            for columnCoordinate in range(self._gameBoard.Width):
                if self._gameBoard.Board[rowCoordinate][columnCoordinate].Status == "discovered":
                    numberOfDiscoveredTiles += 1
        if numberOfDiscoveredTiles == self._gameBoard.Width * self._gameBoard.Height - self._gameBoard.NumberOfMines:
            return True
        return False

    def playerLost(self):
        for rowCoordinate in range(self._gameBoard.Height):
            for columnCoordinate in range(self._gameBoard.Width):
                if self._gameBoard.Board[rowCoordinate][columnCoordinate].Value == "mine" and self._gameBoard.Board[rowCoordinate][columnCoordinate].Status == "discovered":
                    return True
        return False

    def gameOver(self):
        if self.playerLost() or self.playerWon():
            return True
        return False

    def markFlag(self, rowCoordinate, columnCoordinate):
        '''

        :param xTile: the row coordinate of the tile
        :param yTile: the column coordinate of the tile
        :return: marks a flag in the tile chosen by the player
        '''
        self._gameBoard.markFlag(rowCoordinate, columnCoordinate)

    def unmarkFlag(self, rowCoordinate, columnCoordinate):
        '''

        :param xTile: the x coordinate of the tile
        :param yTile: the y coordinate of the tile
        :return: unmarks a flag from a tile chosen by the player
        '''
        self._gameBoard.unmarkFlag(rowCoordinate, columnCoordinate)

    def markSafeTile(self, rowCoordinate, columnCoordinate):
        '''
        marks the tile the player considers to be safe (number/blank)
        :param xTile: the x coordinate of the tile
        :param yTile: the y coordinate of the tile
        :return:
        '''
        #self._gameBoard.markSafeTile(rowCoordinate, columnCoordinate)
        self._gameBoard.autoFill(rowCoordinate, columnCoordinate)
        if self.playerWon():
            return True
        elif self.playerLost():
            return False


    #SHOULD HAVE BEEN IN GAMEBOARD CLASS
    def fillNumbers(self):
        '''
        used to fill the numbers in the board after the mines have been placed
        :return: the board is updated
        '''
        for rowCoordinate in range(self._gameBoard.Height):
            for columnCoordinate in range(self._gameBoard.Width):
                if self._gameBoard.Board[rowCoordinate][columnCoordinate].Value != "mine":
                    numberOfSurroundingMines = self._gameBoard.numberOfSurroundingMines(rowCoordinate, columnCoordinate)
                    if numberOfSurroundingMines > 0:
                        self._gameBoard.Board[rowCoordinate][columnCoordinate].Value = numberOfSurroundingMines
                        self._gameBoard.Board[rowCoordinate][columnCoordinate].VisualRepresentation = str(numberOfSurroundingMines)

    def randomlyFindMine(self):
        '''
        used for finding a tile to place a mine
        if a mine already exists there, the function is recursively called until the mine is placed in an empty position
        :return:
        '''
        rowCoordinate = random.choice(range(self._gameBoard.Height))
        columnCoordinate = random.choice(range(self._gameBoard.Width))
        if self._gameBoard.Board[rowCoordinate][columnCoordinate].Value == None:
            self._gameBoard.Board[rowCoordinate][columnCoordinate].Value = "mine"
            self._gameBoard.Board[rowCoordinate][columnCoordinate].VisualRepresentation = "*"
        else:
            self.randomlyFindMine()

    def initializeEmptyGameBoard(self):
        '''
        we create the board, each tile having None value
        '''
        for rowCoordinate in range(self._gameBoard.Height):
            currentRow = []
            for columnCoordinate in range(self._gameBoard.Width):
                tile = Tile("O")
                currentRow.append(tile)
            self._gameBoard.Board.append(currentRow)

    def initializeGameBoard(self, height, width, numberOfMines):
        '''
        initializes the game board by randomly generating mines
        :return:
        '''
        self._validator.validateSettings(height, width, numberOfMines)
        self._gameBoard.Height = height
        self._gameBoard.Width = width
        self._gameBoard.NumberOfMines = numberOfMines
        self.initializeEmptyGameBoard()
        for mine in range(numberOfMines):
            self.randomlyFindMine()
        self.fillNumbers()