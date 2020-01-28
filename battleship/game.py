from players import Player, Human, Computer
import random

class Game(object):
    def __init__(self, gameBoard1, gameBoard2, player1, player2):
        self._gameBoard1 = gameBoard1
        self._gameBoard2 = gameBoard2
        self._player1 = player1
        self._player2 = player2

    @property
    def Ships(self):
        return self._gameBoard.Ships

    @Ships.setter
    def Ships(self, ships):
        self._gameBoard.Ships = ships

    def visualBoardForPlayer(self, player):
        if player == 1:
            return self._gameBoard1.visualBoardForPlayer()
        return self._gameBoard2.visualBoardForPlayer()

    def visualBoardForOpponent(self, player):
        if player == 1:
            return self._gameBoard1.visualBoardForOpponent()
        return self._gameBoard2.visualBoardForOpponent()

    def allShipsPlaced(self, player):
        '''
        function to determine whether the player placed two valid ships and can start the game
        :return: True/False
        '''
        if player == 1:
            return self._gameBoard1.allShipsPlaced()
        else:
            return self._gameBoard2.allShipsPlaced()

    def computerPlaceShips(self):
        '''
        function for computer's ship placement
        :param row1:
        :param column1:
        :param row2:
        :param column2:
        :param row3:
        :param column3:
        :return:
        '''

        orientation = random.choice(["horizontal", "vertical"])

        if orientation == "horizontal":
            row1 = random.choice(range(self._gameBoard1.Size))
            row2 = row1
            row3 = row1
            column1 = random.choice(range(self._gameBoard1.Size//2))
            column2 = column1 + 1
            column3 = column2 + 1
        elif orientation == "vertical":
            column1 = random.choice(range(self._gameBoard1.Size))
            column2 = column1
            column3 = column1
            row1 = random.choice(range(self._gameBoard1.Size // 2))
            row2 = row1 + 1
            row3 = row2 + 1

        try:
            self._gameBoard2.placeShip(row1, column1, row2, column2, row3, column3)
        except Exception:
            self.computerPlaceShips()

    def humanPlaceShips(self, row1, column1, row2, column2, row3, column3):
        self._gameBoard1.placeShip(row1, column1, row2, column2, row3, column3)

    def placeShips(self, player, row1, column1, row2, column2, row3, column3):
        '''
        function for placing the ship of the player at the given coordinates
        :param player:
        :param row1:
        :param column1:
        :param row2:
        :param column2:
        :param row3:
        :param column3:
        :return:
        '''
        if player == 1:
            self.humanPlaceShips(row1, column1, row2, column2, row3, column3)
        else:
            self.computerPlaceShips()
            self.computerPlaceShips()

    def humanAttack(self, rowCoordinate, columnCoordinate):
        self._gameBoard2.attack(rowCoordinate, columnCoordinate)

    def computerAttack(self):
        rowCoordinate = random.choice(range(self._gameBoard1.Size))
        columnCoordinate = random.choice(range(self._gameBoard1.Size))
        try:
            self._gameBoard1.attack(rowCoordinate, columnCoordinate)
        except ValueError:
            self.computerAttack()

    def attack(self, opponent, rowCoordinate, columnCoordinate):
        if opponent == 1:
            self.computerAttack()
        elif opponent == 2:
            self.humanAttack(rowCoordinate, columnCoordinate)

    def loser(self, player):
        if player == 1:
            return self._gameBoard1.loser()
        else:
            return self._gameBoard2.loser()


    def initializeGame(self):
        self._gameBoard1.initializeBoard()
        self._gameBoard2.initializeBoard()