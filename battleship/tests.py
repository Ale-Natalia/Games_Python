import unittest
from game import Game
from gameBoard import GameBoard
from tile import Tile
from players import Player, Human, Computer

class MyTestCase(unittest.TestCase):
    def test_placeShip_valid(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()

        game.placeShips(1, 0, 0, 1, 0, 2, 0)
        self.assertEqual(humanGameBoard.visualBoardForPlayer(), "+ . . . . . \n+ . . . . . \n+ . . . . . \n. . . . . . \n. . . . . . \n. . . . . . \n")

    def test_placeShip_invalid_shipsNotOnSameLineOrRow(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()

        try:
            game.placeShips(1, 1, 1, 1, 0, 2, 0)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Ship must be on same line/same row! ")

    def test_placeShip_invalid_shipsNotOnAdjacentSquares(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()

        try:
            game.placeShips(1, 1, 1, 1, 0, 1, 4)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Ship must be on adjacent squares!")

    def test_placeShip_invalid_coordinatesOutOfRange(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()

        try:
            game.placeShips(1, 1, 1, 1, 0, 1, 7)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Coordinates out of range!")

    def test_placeShip_invalid_shipsOverLap(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()
        game.placeShips(1, 0, 0, 1, 0, 2, 0)

        try:
            game.placeShips(1, 1, 0, 2, 0, 3, 0)
            self.assertFalse(True)
        except ValueError as error:
            self.assertEqual(str(error), "Ships overlap!")

    def test_attack_valid(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()
        game.placeShips(1, 0, 0, 1, 0, 2, 0)
        game.placeShips(1, 3, 2, 3, 3, 3, 4)

        humanGameBoard.attack(1, 1)
        self.assertEqual(humanGameBoard.Board[1][1].Discovered, True)

    def test_attack_invalid(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()
        game.placeShips(1, 0, 0, 1, 0, 2, 0)
        game.placeShips(1, 3, 2, 3, 3, 3, 4)

        humanGameBoard.attack(5, 5)
        try:
            humanGameBoard.attack(5, 5)
            self.assertEqual(True, False)
        except ValueError as error:
            self.assertEqual(str(error), "Tile already discovered!")

    def test_loser_true(self):
        human = Human("X")
        computer = Computer("X")

        humanGameBoard = GameBoard()
        computerGameBoard = GameBoard()

        game = Game(humanGameBoard, computerGameBoard, human, computer)
        game.initializeGame()
        game.placeShips(1, 0, 0, 1, 0, 2, 0)
        game.placeShips(1, 3, 2, 3, 3, 3, 4)

        humanGameBoard.attack(0, 0)
        humanGameBoard.attack(1, 0)
        humanGameBoard.attack(2, 0)
        self.assertEqual(game.loser(1), True)

if __name__ == '__main__':
    unittest.main()
