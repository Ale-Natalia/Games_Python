#from game import Game #DELETE after!!!!!!!!!!!!!!!!!!!

class UI(object):
    def __init__(self, game):
        self._game = game #change after!!!!!!!!!!!!!!!
        self._gameOver = False

    def printTurn(self):
        print(self._game)

    def printGameOver(self):
        if self._game.isWinner():
            print("You won!")
        elif self._game.isLoser():
            print("You lost!")

    def acresBuyOrSell(self):
        '''
        we get the player input and update the acres to buy/sell
        :return:
        '''
        try:
            acres = int(input("Acres to buy/sell(+/-)-> "))
        except ValueError:
            print("Acres must be integer!")
            self.acresBuyOrSell()
            return
        try:
            self._game.acresBuyOrSell(acres)
        except ValueError as error:
            print(error)
            self.acresBuyOrSell()
            return

    def unitsToFeedPopulation(self):
        '''
        we get the player input and update the acres to buy/sell
        :return:
        '''
        try:
            units = int(input("Units to feed the population-> "))
        except ValueError:
            print("Units must be integer!")
            self.unitsToFeedPopulation()
            return
        try:
            self._game.unitsToFeedPopulation(units)
        except ValueError as error:
            print(error)
            self.unitsToFeedPopulation()
            return

    def acresToHarvest(self):
        '''
        we get the player input and update the acres to harvest (plant)
        :return:
        '''
        try:
            units = int(input("Acres to plant-> "))
        except ValueError:
            print("Acress must be integer!")
            self.acresToHarvest()
            return
        try:
            self._game.acresToHarvest(units)
        except ValueError as error:
            print(error)
            self.acresToHarvest()
            return

    def initializeTurn(self):
        self._game.initializeTurn()

    def play(self):
        self.initializeTurn()
        self.printTurn()
        self._gameOver = self._game.GameOver
        if self._gameOver is True:
            self.printGameOver()
            return
        self.acresBuyOrSell()
        self.unitsToFeedPopulation()
        self.acresToHarvest()
        self.play()