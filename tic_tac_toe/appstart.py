from ui import UI
from game import Game
from gameboard import GameBoard
from players import Human, Computer

gameBoard = GameBoard()

player1 = Human(1, "x")
player2 = Computer(2, "o")

game = Game(player1, player2, gameBoard)
ui = UI(game)

ui.welcome()