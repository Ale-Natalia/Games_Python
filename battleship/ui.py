class UI(object):
    def __init__(self, game):
        self._game = game
        self._gameOver = False
        self._winner = None

    def printWelcome(self):
        print("Welcome to the game! Place your ships!")

    def placeShips(self):
        letterToNumber = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        command = input("Place a ship: ")
        if command == "start":
            if self._game.allShipsPlaced(1):
                self._game.placeShips(2, None, None, None, None, None, None)
                self.start()
                return
            else:
                print("You need to place two valid ships first!")
                self.placeShips()
                return
        else:
            parts = command.split(" ")
            if len(parts) != 2:
                print("Command must be of structure ship <𝑪𝟏𝑳𝟏𝑪𝟐𝑳𝟐𝑪𝟑𝑳𝟑> !")
                self.placeShips()
                return
            elif parts[0] != "ship":
                print("Command must be of structure ship <𝑪𝟏𝑳𝟏𝑪𝟐𝑳𝟐𝑪𝟑𝑳𝟑> !")
                self.placeShips()
                return
            else:
                shipCoordinates = parts[1]
                shipCoordinates.strip(" ")
                if len(shipCoordinates) != 6:
                    print("Ship must be  <𝑪𝟏𝑳𝟏𝑪𝟐𝑳𝟐𝑪𝟑𝑳𝟑> !")
                    self.placeShips()
                    return
                else:
                    try:
                        column1 = letterToNumber[shipCoordinates[0]]
                        row1 = int(shipCoordinates[1])
                        column2 = letterToNumber[shipCoordinates[2]]
                        row2 = int(shipCoordinates[3])
                        column3 = letterToNumber[shipCoordinates[4]]
                        row3 = int(shipCoordinates[5])
                    except KeyError:
                        print("Invalid coordinates!")
                        self.placeShips()
                        return
                    try:
                        self._game.placeShips(1, row1, column1, row2, column2, row3, column3)
                        print(self._game.visualBoardForPlayer(1))
                        self.placeShips()
                        return
                    except Exception as error:
                        print(error)
                        self.placeShips()
                        return

    def welcome(self):
        self.printWelcome()
        self._game.initializeGame()
        self.placeShips()

    def cheat(self, player):
        if player == 1:
            print(self._game.visualBoardForPlayer(2))
        else:
            print(self._game.visualBoardForPlayer(1))

    def humanTurn(self):
        letterToNumber = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        command = input("Your command: ")
        command.strip(" ")
        if command == "exit":
            return
        if command == "cheat":
            self.cheat(1)
            self.start()
            return
        else:
            parts = command.split(" ")
            parts[0].strip(" ")
            parts[1].strip(" ")
            rowCoordinate = int(parts[1][1])
            columnCoordinate = letterToNumber[parts[1][0]]
            try:
                self._game.attack(2, rowCoordinate, columnCoordinate)
            except Exception as error:
                print(error)
                self.humanTurn()
                return
            if self._game.loser(2):
                self._gameOver = True
                self._winner = 1

    def computerTurn(self):
        self._game.attack(1, None, None)
        if self._game.loser(1):
            self._gameOver = True
            self._winner = 2

    def printGameOverMessage(self):
        if self._winner == 1:
            print("Human wins!")
        else:
            print("Computer wins!")

    def start(self):
        while not self._gameOver:
            self.humanTurn()
            print(self._game.visualBoardForPlayer(1))
            print(self._game.visualBoardForOpponent(2))
            if self._gameOver:
                self.printGameOverMessage()
                return
            self.computerTurn()
            print(self._game.visualBoardForPlayer(1))
            print(self._game.visualBoardForOpponent(2))
            if self._gameOver:
                self.printGameOverMessage()
                return