from players import Player, Human, Computer
import random

class Game(object):
    def __init__(self, player1, player2, gameBoard):
        self._player1 = player1
        self._player2 = player2
        self._gameBoard = gameBoard

    @property
    def VisualBoard(self):
        return self._gameBoard.VisualBoard

    @property
    def Player1(self):
        return self._player1

    @Player1.setter
    def Player1(self, player):
        self._player1 = player

    @property
    def Player2(self):
        return self._player2

    @Player2.setter
    def Player2(self, player):
        self._player2 = player

    def initializeGame(self, size, winSize, firstPlayerID, firstPlayerType, firstPlayerSign, secondPlayerID, secondPlayerType, secondPlayerSign):
        if size == None: #all are none
            self._player1 = Human(1, "x")
            self._player2 = Computer(2, "o")
            self._gameBoard.initializeBoard()
            return

        self._gameBoard.Size = size
        self._gameBoard.WinSize = winSize
        self._gameBoard.initializeBoard()

        if firstPlayerType == "human":
            firstPlayerType = Human
        else:
            firstPlayerType = Computer

        if secondPlayerType == "human":
            secondPlayerType = Human
        else:
            secondPlayerType = Computer

        self._player1 = firstPlayerType(firstPlayerID, firstPlayerSign)
        self._player2 = secondPlayerType(secondPlayerID, secondPlayerSign)

    def isWinner(self, player):
        return self._gameBoard.isWinner(player)

    def isDraw(self):
        return self._gameBoard.isDraw()

    def humanMove(self, player, rowCoordinate, columnCoordinate):
        self._gameBoard.move(player, rowCoordinate, columnCoordinate)

    def computerMove(self, player):
        rowCoordinate = random.choice(range(self._gameBoard.Size))
        columnCoordinate = random.choice(range(self._gameBoard.Size))
        try:
            self._gameBoard.move(player, rowCoordinate, columnCoordinate)
        except Exception: #already occupied
            self.computerMove(player)

    def move(self, player, rowCoordinate, columnCoordinate):
        if rowCoordinate == None and columnCoordinate == None:
            self.computerMove(player)
        else:
            self.humanMove(player, rowCoordinate, columnCoordinate)