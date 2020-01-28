class UI(object):
    def __init__(self, game):
        self._game = game
        self._gameOver = False

    def printStartMenu(self):
        print("Tic Tac Toe")
        print("1. Settings")
        print("2. Start game")
        print("0. Exit")

    def welcome(self):
        self.printStartMenu()
        choice = input("Make your choice")
        if choice == "1":
            self.settings()
            self.welcome()
            return
        elif choice == "2":
            self._game.initializeGame(None, None, None, None, None, None, None, None)
            self.run()
            return
        elif choice == "3":
            return

    def settings(self):
        try:
            size = int(input("Board size: "))
        except ValueError:
            print("Size must be an integer")
            return
        try:
            winSize = int(input("Win size: "))
        except ValueError:
            print("Size must be an integer")
            return
        try:
            firstPlayerID = int(input("First player ID: "))
        except ValueError:
            print("ID must be an integer")
            return
        try:
            firstPlayerType = int(input("First player type (1-human, 2-computer): "))
            if firstPlayerType not in [1, 2]:
                raise ValueError
            if firstPlayerType == 1:
                firstPlayerType = "human"
            else:
                firstPlayerType = "computer"
        except ValueError:
                print("You must type 1-2 for player type")
                return
        firstPlayerSign = input("First player sign: ")

        try:
            secondPlayerID = int(input("Second player ID: "))
        except ValueError:
            print("ID must be an integer")
            return
        try:
            secondPlayerType = int(input("Second player type (1-human, 2-computer): "))
            if secondPlayerType not in [1, 2]:
                raise ValueError
            if secondPlayerType == 1:
                secondPlayerType = "human"
            else:
                secondPlayerType = "computer"
        except ValueError:
                print("You must type 1-2 for player type")
                return
        secondPlayerSign = input("Second player sign: ")

        self._game.initializeGame(size, winSize, firstPlayerID, firstPlayerType, firstPlayerSign, secondPlayerID, secondPlayerType, secondPlayerSign)

    def printGameOver(self):
        if self.isWinner(self._game.Player1):
            print(self._game.Player1.VisualRepresentation + " wins!")
        elif self.isWinner(self._game.Player2):
            print(self._game.Player2.VisualRepresentation + " wins!")
        else:
            print("It's a draw!")

    def isWinner(self, player):
        return self._game.isWinner(player)

    def isDraw(self):
        return self._game.isDraw()

    def humanMove(self, player):
        print("Player " + player.VisualRepresentation + " makes their move")
        try:
            rowCoordinate = int(input("Choose row: "))
            columnCoordinate = int(input("Choose column: "))
            try:
                self._game.move(player, rowCoordinate, columnCoordinate)
                if self.isWinner(player) or self.isDraw():
                    self._gameOver = True
            except ValueError as error:
                print(error)
                self.humanMove(player)
                return
        except ValueError:
            print("Choice must be integer")
            self.humanMove(player)
            return

    def computerMove(self, player):
        print("Player " + player.VisualRepresentation + " makes their move")
        self._game.move(player, None, None)
        if self.isWinner(player) or self.isDraw():
            self._gameOver = True

    def playerMove(self, player):
        print(self._game.VisualBoard.draw())
        if player.__class__.__name__ == "Human":
            self.humanMove(player)
        else:
            try:
                self.computerMove(player)
            except ValueError as error:
                print(error)

    def run(self):
        while not self._gameOver:
            self.playerMove(self._game.Player1)
            if self._gameOver:
                self.printGameOver()
                break
            self.playerMove(self._game.Player2)
            if self._gameOver:
                self.printGameOver()
                break