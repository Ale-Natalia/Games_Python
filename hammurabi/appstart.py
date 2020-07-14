from ui import UI
from game import Game
from repo import Repo
from validators import GameValidator

repo = Repo()
validator = GameValidator()
game = Game(repo, validator)
ui = UI(game)

ui.play()