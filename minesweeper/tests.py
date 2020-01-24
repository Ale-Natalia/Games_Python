import unittest
from gameBoard import GameBoard
from gamePlay import GamePlay
from validators import GameValidator

class MyTestCase(unittest.TestCase):
    def test_gamePlay_initializeBoard_minesPlaced(self):
        gameBoard = GameBoard(10, 10, 10)
        validator = GameValidator()
        gamePlay = GamePlay(gameBoard, validator)
        gamePlay.initializeGameBoard(10, 10, 10)
        self.assertEqual(gameBoard.NumberOfMines, 10)

    def test_gameBoard_numberOfSurroundingMines(self):
        gameBoard = GameBoard(10, 10, 10)
        validator = GameValidator()
        gamePlay = GamePlay(gameBoard, validator)
        gamePlay.initializeGameBoard(10, 10, 10)
        for rowCoordinate in range(1, gameBoard.Height - 1):
            for columnCoordinate in range(1, gameBoard.Width - 1):
                if gameBoard.Board[rowCoordinate][columnCoordinate].Value == "mine":
                    self.assertNotEqual(gameBoard.numberOfSurroundingMines(rowCoordinate - 1, columnCoordinate), 0)

    def test_gameBoard_autofill(self):
        gameBoard = GameBoard(10, 10, 10)
        validator = GameValidator()
        gamePlay = GamePlay(gameBoard, validator)
        gamePlay.initializeGameBoard(10, 10, 10)
        print(gameBoard.VisualBoardComplete)
        gameBoard.autoFill(9, 9)
        print(gameBoard.VisualBoardForPlayer)
        self.assertEqual(gameBoard.Board[9][9].Status, "discovered")

if __name__ == '__main__':
    unittest.main()
