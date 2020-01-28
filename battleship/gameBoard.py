import copy
from tile import Tile

class GameBoard(object):
    def __init__(self):
        self._board = []
        self._size = 6
        self._ships = [None, None]

    @property
    def Board(self):
        return self._board

    @Board.setter
    def Board(self, board):
        self._board = board

    @property
    def Size(self):
        return self._size

    @Size.setter
    def Size(self, size):
        self._size = size

    @property
    def Ships(self):
        return self._ships

    @Ships.setter
    def Ships(self, ships):
        self._ships = ships

    def initializeBoard(self):
        for row in range(self._size):
            currentRow = []
            for column in range(self._size):
                tile = Tile()
                currentRow.append(tile)
            self._board.append(currentRow)

    def visualBoardForPlayer(self):
        '''
        the visual board to display to the player
        :return:
        '''
        board = ""
        for row in range(self._size):
            currentRow = ""
            for column in range(self._size):
                if self._board[row][column].Discovered is True or self._board[row][column].Value is True:
                    currentRow += self._board[row][column].VisualRepresentation + " "
                else:
                    currentRow += ". "
            board += currentRow + "\n"
        return board

    def visualBoardForOpponent(self):
        '''
        the visual board to display to the opponent
        :return:
        '''
        board = ""
        for row in range(self._size):
            currentRow = ""
            for column in range(self._size):
                if self._board[row][column].Discovered is True:
                    currentRow += self._board[row][column].VisualRepresentation + " "
                else:
                    currentRow += ". "
            board += currentRow + "\n"
        return board

    def allShipsPlaced(self):
        '''
        function to determine whether the player placed two valid ships and can start the game
        :return: True/False
        '''
        if self._ships[0] != None and self._ships[1] != None:
            return True
        return False

    def clearShip(self):
        '''
        clears a ship if the player decides he wants to place another
        :return: the ship is cleared
        '''
        for tile in range(len(self._ships[0])):
            row = self._ships[0][tile][0]
            column = self._ships[0][tile][1]
            self._board[row][column].Value = None
            self._board[row][column].VisualRepresentation = "o"

    def validateShip(self, row1, column1, row2, column2, row3, column3):
        if row1 not in range(self._size) or row2 not in range(self._size) or row3 not in range(self._size) or column1 not in range(self._size) or column2 not in range(self._size) or column3 not in range(self._size):
            raise ValueError("Coordinates out of range!")
        if not(row1 == row2 and row2 == row3) and not(column1 == column2 and column2 == column3):
            raise ValueError("Ship must be on same line/same row! ")
        if row1 == row2 and row2 == row3 and column2 != (column1 + column3)//2:
            raise ValueError("Ship must be on adjacent squares!")
        if column1 == column2 and column2 == column3 and row2 != (row1 + row3)//2:
            raise ValueError("Ship must be on adjacent squares!")

    def validateShipsDontOverlap(self, row1, column1, row2, column2, row3, column3):
        if self._board[row1][column1].Value != None or self._board[row2][column2].Value != None or self._board[row3][column3].Value != None:
            raise ValueError("Ships overlap!")

    def placeShip(self, row1, column1, row2, column2, row3, column3):
        '''
        places a ship on the player's board at the given coordinates
        :param row1:
        :param column1:
        :param row2:
        :param column2:
        :param row3:
        :param column3:
        :return:
        '''
        self.validateShip(row1, column1, row2, column2, row3, column3)
        if self._ships[0] == None:
            self.validateShipsDontOverlap(row1, column1, row2, column2, row3, column3)
            self._ships[0] = [[row1, column1], [row2, column2], [row3, column3]]
        elif self._ships[1] == None:
            self.validateShipsDontOverlap(row1, column1, row2, column2, row3, column3)
            self._ships[1] = [[row1, column1], [row2, column2], [row3, column3]]
        else:
            '''
            we clear the first ship from the board
            then we transfer the second ship to the first ship
            then we place the new ship on the second position
            '''
            self.clearShip()
            self.validateShipsDontOverlap(row1, column1, row2, column2, row3, column3)

            for tile in range(len(self._ships[1])):
                self._ships[0][tile][0] = self._ships[1][tile][0]
                self._ships[0][tile][1] = self._ships[1][tile][1]

            self._ships[1][0][0] = row1
            self._ships[1][0][1] = column1
            self._ships[1][1][0] = row2
            self._ships[1][1][1] = column2
            self._ships[1][2][0] = row3
            self._ships[1][2][1] = column3


        self._board[row1][column1].Value = True
        self._board[row2][column2].Value = True
        self._board[row3][column3].Value = True
        self._board[row1][column1].VisualRepresentation = "+"
        self._board[row2][column2].VisualRepresentation = "+"
        self._board[row3][column3].VisualRepresentation = "+"

    def attack(self, rowCoordinate, columnCoordinate):
        '''
        function for attacking a square
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        if self._board[rowCoordinate][columnCoordinate].Discovered is True:
            raise ValueError("Tile already discovered!")
        self._board[rowCoordinate][columnCoordinate].Discovered = True

    def hit(self, rowCoordinate, columnCoordinate):
        '''
        it determines whether the attacked tile was a hit or miss
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        if self._board[rowCoordinate][columnCoordinate].Value == None:
            return False
        return True

    def loser(self):
        '''
        determines whether the player loses or not
        :param rowCoordinate:
        :param columnCoordinate:
        :return:
        '''
        for ship in self._ships:
            row1 = ship[0][0]
            column1 = ship[0][1]
            row2 = ship[1][0]
            column2 = ship[1][1]
            row3 = ship[2][0]
            column3 = ship[2][1]
            if self._board[row1][column1].Discovered is True and self._board[row2][column2].Discovered is True and self._board[row3][column3].Discovered is True:
                return True
        return False