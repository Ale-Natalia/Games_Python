#from repo import Repo #REMOVE AFTER
import random
import cmath

class Game(object):
    def __init__(self, repo, validator):
        self._repo = repo #Change to repo!!!!!!!!!!!!!!!
        self._validator = validator
        self._turn = 0
        self._gameOver = False

    @property
    def GameOver(self):
        return self._gameOver

    @property
    def Turn(self):
        return self._turn

    @Turn.setter
    def Turn(self, turn):
        self._turn = turn

    def __str__(self):
        string = "\n"
        string += "In  year " + str(self._turn) + ", " + str(self._repo.PopulationStarved) + " people starved.\n"
        string += str(self._repo.NewPopulation) + " people came to city.\n"
        string += "City population is " + str(self._repo.Population) + ".\n"
        string += "City owns " + str(self._repo.LandAcres) + " acres of land.\n"
        string += "Harvest was " + str(self._repo.Harvest) + " units/acres.\n"
        string += "Rats ate " + str(self._repo.UnitsEatenByRats) + " units\n"
        string += "Land price is " + str(self._repo.LandPrice) + " units/acre.\n"
        string += "Grain stocks are " + str(self._repo.Units) + " units.\n"
        return string

    def validateAcres(self, acres):
        if acres * self._repo.LandPrice > self._repo.Units:
            raise ValueError("You don't have enough units to buy " + str(acres) + " acres!")
        if acres < 0 and acres*(-1) > self._repo.LandAcres:
            raise ValueError("You don't have " + str(-acres) + " acres to sell!")

    def acresBuyOrSell(self, acres):
        '''
        player decides how many acres to buy/sell
        :param acres: number of acres
        :return: the game data is updated
        '''
        self.validateAcres(acres)
        self._repo.AcresToBuyOrSell = acres

    def validateUnits(self, units):
        if units > self._repo.Units + (-1) * self._repo.AcresToBuyOrSell * self._repo.LandPrice:
            raise ValueError("You don't have enough units!")

    def unitsToFeedPopulation(self, units):
        '''
        player decides how many units they want to feed the population
        :param units:
        :return:
        '''
        self.validateUnits(units)
        self._repo.UnitsToFeed = units

    def validateAcresToHarvest(self, acresToHarvest):
        if acresToHarvest > self._repo.LandAcres + self._repo.AcresToBuyOrSell:
            raise ValueError("You don't have enough acres!")
        if acresToHarvest > self._repo.Units - self._repo.UnitsToFeed - self._repo.AcresToBuyOrSell * self._repo.LandPrice:
            raise ValueError("You don't have enough units to harvest these acres!")

    def acresToHarvest(self, acres):
        '''
        player decides how many acres to harvest
        :param acres:
        :return:
        '''
        self.validateAcresToHarvest(acres)
        self._repo.AcresToHarvest = acres






    def buyOrSellAcres(self):
        '''
        the acres are bought/sold during the internal game turn
        :return:
        '''
        acres = self._repo.AcresToBuyOrSell
        if acres > 0: #buy
            self._repo.LandAcres += acres
            self._repo.Units -= acres * self._repo.LandPrice
        elif acres < 0: #sell
            self._repo.LandAcres -= -1 * acres
            self._repo.Units += (-1) * acres * self._repo.LandPrice


    def feedPopulationAutomatically(self):
        '''
        the units to feed attribute in repo is set automatically for first round
        used for first turn=no user input
        :return: repo data updated
        '''
        maximumPeopleThatCanBeFed = self._repo.Units // 20
        if maximumPeopleThatCanBeFed >= self._repo.Population: #no one starves
            self._repo.UnitsToFeed = self._repo.Population * 20
        else: #people starve. hard times
            self._repo.UnitsToFeed = maximumPeopleThatCanBeFed * 20

    def feedPopulation(self):
        '''
        the population is fed accordingly
        people come to the city if no one starved
        grain stocks updated
        population updated
        '''
        if self._turn == 1:
            self.feedPopulationAutomatically()
        else:
            maximumPeopleThatCanBeFed = self._repo.UnitsToFeed // 20
            if maximumPeopleThatCanBeFed >= self._repo.Population:  # no one starves
                self._repo.PopulationStarved = 0
                self._repo.Units -= self._repo.UnitsToFeed
                self.peopleComeToCity()
            else:  # people starve. hard times
                self._repo.Units -= maximumPeopleThatCanBeFed * 20
                self._repo.PopulationStarved = self._repo.Population - maximumPeopleThatCanBeFed
                if self._repo.PopulationStarved >= self._repo.Population // 2:
                    self._gameOver = True
                self._repo.Population = maximumPeopleThatCanBeFed
                self._repo.NewPopulation = 0


    def updateLandPrice(self):
        '''
        the land price is chosen automatically 15-25
        :return: land price is updated
        '''
        self._repo.LandPrice = random.choice(range(15, 26))

    def peopleComeToCity(self):
        '''

        :return: the number of new people is updated
        '''
        self._repo.NewPopulation = 0
        if self._repo.PopulationStarved == 0:
            self._repo.NewPopulation = random.choice(range(0, 11))
            self._repo.Population += self._repo.NewPopulation

    def updateHarvest(self):
        '''
        randomly generates a harvest 1-6
        :return: harvest updated
        '''
        self._repo.Harvest = random.choice(range(1, 7))

    def harvestGrain(self):
        '''
        grain is harvested automatically
        :return: the grain units are updated
        '''
        maximumAcresToHarvest = self._repo.Population * 10 #each person can harvest 10 acres
        if maximumAcresToHarvest >= self._repo.AcresToHarvest: #all acres are harvested
            self._repo.Units += self._repo.AcresToHarvest * self._repo.Harvest
        else: #only the maximum number of acres is harvested
            if maximumAcresToHarvest >= 0:
                self._repo.Units += maximumAcresToHarvest * self._repo.Harvest

    def ratsInfestation(self):
        '''
        the rats infest the city. Or do they?
        chance of 20%
        maximum 10% of grain is eaten
        :return: percentToEat + the grain is updated
        '''
        isInfested = random.choice(range(5))
        if isInfested == 0: # there are 20% for 0 to be picked from range(5), we suppose this is the number for infestation
            percentToEat = random.choice(range(0, 11))
            self._repo.UnitsEatenByRats = percentToEat * self._repo.Units // 100
            self._repo.Units -= self._repo.UnitsEatenByRats
            return percentToEat
        else:
            self._repo.UnitsEatenByRats = 0

    def initializeTurn(self):
        '''
        the turn is initialized with the new data
        :return:
        '''
        self._turn += 1
        self.buyOrSellAcres()
        self.updateHarvest()
        self.updateLandPrice()
        self.feedPopulation()
        self.harvestGrain()
        self.ratsInfestation()
        if self._turn == 5: #the game ends on the 5-th turn
            self._gameOver = True

    def isGameOver(self):
        return self._turn == 6

    def isWinner(self):
        if self._turn == 5 and self._repo.Population >= 100 and self._repo.LandAcres >= 1000:
            return True
        return False

    def isLoser(self):
        return True
