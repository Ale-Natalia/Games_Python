class Minesweeper(object):
    def __init__(self, gamePlay):
        self._gamePlay = gamePlay
        self._gameOver = False

    def printWelcomeMenu(self):
        print("1. Game settings")
        print("2. Start game")
        print("0. Exit")

    def gameSettings(self):
        try:
            height = int(input("Board height: "))
        except ValueError:
            print("Height must be integer")
        try:
            width = int(input("Board width: "))
        except ValueError:
            print("Width must be integer")
        try:
            numberOfMines = int(input("Number of mines: "))
        except ValueError:
            print("Number of mines must be integer")
        try:
            self._gamePlay.initializeGameBoard(height, width, numberOfMines)
        except ValueError as error:
            print(error)

    def welcomeScreen(self):
        self.printWelcomeMenu()
        choice = input("Make your choice: ")
        while True:
            if choice == "1":
                self.gameSettings()
                self.welcomeScreen()
                break
            elif choice == "2":
                self.run()
                break
            elif choice == "0":
                break
            else:
                print("Choice must be 0-2")
                self.welcomeScreen()
                break

    def playerWon(self):
        if self._gamePlay.playerWon():
            return True

    def playerLost(self):
        if self._gamePlay.playerLost():
            return True

    def gameOver(self):
        return self._gamePlay.gameOver()


    def checkForGameOver(self):
        if self.playerWon():
            print(self._gamePlay.VisualBoardComplete)
            print("Congrats! You won!")
            self._gameOver = True
        elif self.playerLost():
            print(self._gamePlay.VisualBoardComplete)
            print("Oh no, you loser!")
            self._gameOver = True
        else:
            pass

    def markFlag(self):
        try:
            rowCoordinate = int(input("Row coordinate: "))
            columnCoordinate = int(input("Column coordinate: "))
        except ValueError:
            print("Coordinates must be integers")
        try:
            self._gamePlay.markFlag(rowCoordinate, columnCoordinate)
        except Exception as error:
            print(error)

    def unmarkFlag(self):
        try:
            rowCoordinate = int(input("Row coordinate: "))
            columnCoordinate = int(input("Column coordinate: "))
        except ValueError:
            print("Coordinates must be integers")
        try:
            self._gamePlay.unmarkFlag(rowCoordinate, columnCoordinate)
        except Exception as error:
            print(error)

    def markSafeTile(self):
        try:
            rowCoordinate = int(input("Row coordinate: "))
            columnCoordinate = int(input("Column coordinate: "))
        except ValueError:
            print("Coordinates must be integers")
        try:
            self._gamePlay.markSafeTile(rowCoordinate, columnCoordinate)
            self.checkForGameOver()
        except Exception as error:
            print(error)

    def cheat(self):
        print(self._gamePlay.VisualBoardComplete)

    def printGameMenu(self):
        print("1. Mark tile as safe")
        print("2. Mark tile with flag")
        print("3. Remove flag from tile")
        print("4. Cheat (You'd better be ashamed)")
        print("0. Exit")

    def run(self):
        print(self._gamePlay.VisualBoardForPlayer)
        self.printGameMenu()
        choice = input("Make your choice: ")
        while not self._gameOver:
            if choice == "1":
                self.markSafeTile()
                if self._gameOver:
                    break
                self.run()
                break
            elif choice == "2":
                self.markFlag()
                self.run()
                break
            elif choice == "3":
                self.unmarkFlag()
                self.run()
                break
            elif choice == "4":
                self.cheat()
                self.run()
                break
            elif choice == "0":
                break
            else:
                print("Choice must be 0-4")
                self.run()
                break