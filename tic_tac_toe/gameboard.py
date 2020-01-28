from texttable_master.texttable import Texttable
from tile import Tile

class GameBoard(object):
    def __init__(self, size = 3, winSize = 3):
        self._board = []
        self._size = size
        self._winSize = winSize

    @property
    def Board(self):
        return self._board

    @Board.setter
    def Board(self, otherBoard):
        self._board = otherBoard

    @property
    def Size(self):
        return self._size

    @Size.setter
    def Size(self, size):
        self._size = size

    @property
    def WinSize(self):
        return self._winSize

    @WinSize.setter
    def WinSize(self, size):
        self._winSize = size

    @property
    def VisualBoard(self):
        return self.createVisualBoard()

    def initializeBoard(self):
        for row in range(self._size):
            currentRow = []
            for column in range(self._size):
                tile = Tile()
                currentRow.append(tile)
            self._board.append(currentRow)

    def createVisualBoard(self):
        visualBoard = Texttable()
        for row in range(self._size):
            currentRow = []
            for column in range(self._size):
                tile = self._board[row][column].VisualRepresentation
                currentRow.append(tile)
            visualBoard.add_row(currentRow)
        return visualBoard

    def validateMove(self, rowCoordinate, columnCoordinate):
        if rowCoordinate not in range(self._size) or columnCoordinate not in range(self._size):
            raise ValueError("Row/column coordinate must be 0->n-1!")
        elif self._board[rowCoordinate][columnCoordinate].Value != None:
            raise ValueError("Tile already occupied!")


    def move(self, player, rowCoordinate, columnCoordinate):
        self.validateMove(rowCoordinate, columnCoordinate)
        self._board[rowCoordinate][columnCoordinate].Value = player
        self._board[rowCoordinate][columnCoordinate].VisualRepresentation = player.VisualRepresentation

    def hasMainDiagonalOfWinSize(self, player):
        diagonalSize = 0
        for column in range(self._size):
            for rowCoordinate in range(self._size - column):
                columnCoordinate = rowCoordinate + column
                if self._board[rowCoordinate][columnCoordinate].Value == player:
                    diagonalSize += 1
                    if diagonalSize == self._winSize:
                        return True
                else:
                    diagonalSize = 0
            diagonalSize = 0
        for row in range(1, self._size):
            for columnCoordinate in range(self._size - row):
                rowCoordinate = columnCoordinate + row
                if self._board[rowCoordinate][columnCoordinate].Value == player:
                    diagonalSize += 1
                    if diagonalSize == self._winSize:
                        return True
                else:
                    diagonalSize = 0
            diagonalSize = 0
        return False

    def hasSecondDiagonalOfWinSize(self, player):
        diagonalSize = 0
        for column in range(self._size):
            for rowCoordinate in range(self._size - column):
                columnCoordinate = self._size - 1 - rowCoordinate
                if self._board[rowCoordinate][columnCoordinate].Value == player:
                    diagonalSize += 1
                    if diagonalSize == self._winSize:
                        return True
                else:
                    diagonalSize = 0
            diagonalSize = 0
        for row in range(1, self._size):
            for columnCoordinate in range(self._size - 1, row - 1, -1):
                rowCoordinate = self._size - 1 - columnCoordinate
                if self._board[rowCoordinate][columnCoordinate].Value == player:
                    diagonalSize += 1
                    if diagonalSize == self._winSize:
                        return True
                else:
                    diagonalSize = 0
            diagonalSize = 0
        return False

    def hasRowOfWinSize(self, player):
        rowSize = 0
        for row in range(self._size):
            for column in range(self._size):
                if self._board[row][column].Value == player:
                    rowSize += 1
                    if rowSize == self._winSize:
                        return True
                else:
                    rowSize = 0
            rowSize = 0
        return False

    def hasColumnOfWinSize(self, player):
        '''
        determines if
        :param player:
        :return:
        '''
        columnSize = 0
        for column in range(self._size):
            for row in range(self._size):
                if self._board[row][column].Value == player:
                    columnSize += 1
                    if columnSize == self._winSize:
                        return True
                else:
                    columnSize = 0
            columnSize = 0
        return False

    def isWinner(self, player):
        '''

        :param player: the player we want to see whether is winner or not
        :return: True - wins / False = loses
        '''
        if self.hasRowOfWinSize(player) or self.hasColumnOfWinSize(player) or self.hasMainDiagonalOfWinSize(player) or self.hasSecondDiagonalOfWinSize(player):
            return True
        return False

    def isDraw(self):
        '''
        determines if the game is a draw
        :return: True/False
        '''
        for row in range(self._size):
            for column in range(self._size):
                if self._board[row][column].Value == None:
                    return False
        return True