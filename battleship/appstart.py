from ui import UI
from game import Game
from gameBoard import GameBoard
from players import Player, Human, Computer

human = Human("X")
computer = Computer("X")

humanGameBoard = GameBoard()
computerGameBoard = GameBoard()

game = Game(humanGameBoard, computerGameBoard, human, computer)

ui = UI(game)

ui.welcome()