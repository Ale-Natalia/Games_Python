import unittest
from game import Game
from gameboard import GameBoard
from players import Human, Computer
from tile import Tile

class MyTestCase(unittest.TestCase):
    def test_playerMove_valid(self):
        gameBoard = GameBoard(3, 3)

        player1 = Human(1, "x")
        player2 = Computer(2, "o")

        game = Game(player1, player2, gameBoard)

        gameBoard.initializeBoard()

        game.move(player1, 0, 0)
        print(gameBoard.Board[0][0])
        self.assertEqual(gameBoard.Board[0][0].Value, player1)

    def test_playerMove_invalid_tileTaken(self):
        gameBoard = GameBoard()

        player1 = Human(1, "x")
        player2 = Computer(2, "o")

        game = Game(player1, player2, gameBoard)
        gameBoard.initializeBoard()

        game.move(player1, 0, 0)
        try:
            game.move(player2, 0, 0)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Tile already occupied!")

    def test_playerMove_invalid_rowOutOfRange(self):
        gameBoard = GameBoard()

        player1 = Human(1, "x")
        player2 = Computer(2, "o")

        game = Game(player1, player2, gameBoard)
        gameBoard.initializeBoard()

        try:
            game.move(player1, 10, 0)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Row/column coordinate must be 0->n-1!")

    def test_playerMove_invalid_columnOutOfRange(self):
        gameBoard = GameBoard()

        player1 = Human(1, "x")
        player2 = Computer(2, "o")

        game = Game(player1, player2, gameBoard)
        gameBoard.initializeBoard()

        try:
            game.move(player1, 0, 10)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Row/column coordinate must be 0->n-1!")

if __name__ == '__main__':
    unittest.main()
