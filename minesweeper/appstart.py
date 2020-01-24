from minesweeper import Minesweeper
from gamePlay import GamePlay
from gameBoard import GameBoard
from validators import GameValidator
from domain import Tile

gameBoard = GameBoard(10, 10, 10)
validator = GameValidator()
gamePlay = GamePlay(gameBoard, validator)

newGame = Minesweeper(gamePlay)

newGame.welcomeScreen()