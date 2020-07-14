class Repo(object):
    def __init__(self):
        self._population = 100
        self._populationStarved = 0
        self._newPopulation = 0
        self._landAcres = 1000
        self._harvest = 3 #unit/acre
        self._unitsEatenByRats = 200
        self._landPrice = 20 #units/acre
        self._units = 2800

        self._acresToBuyOrSell = 0
        self._unitsToFeed = 0
        self._acresToHarvest = self._landAcres

    @property
    def Population(self):
        return self._population

    @property
    def PopulationStarved(self):
        return self._populationStarved

    @property
    def NewPopulation(self):
        return self._newPopulation

    @property
    def LandAcres(self):
        return self._landAcres

    @property
    def Harvest(self):
        return self._harvest

    @property
    def UnitsEatenByRats(self):
        return self._unitsEatenByRats

    @property
    def LandPrice(self):
        return self._landPrice

    @property
    def Units(self):
        return self._units

    @property
    def AcresToBuyOrSell(self):
        return self._acresToBuyOrSell

    @property
    def UnitsToFeed(self):
        return self._unitsToFeed

    @property
    def AcresToHarvest(self):
        return self._acresToHarvest



    @Population.setter
    def Population(self, population):
        self._population = population

    @PopulationStarved.setter
    def PopulationStarved(self, population):
        self._populationStarved = population

    @NewPopulation.setter
    def NewPopulation(self, population):
        self._newPopulation = population

    @LandAcres.setter
    def LandAcres(self, acres):
        self._landAcres = acres

    @Harvest.setter
    def Harvest(self, harvest):
        self._harvest = harvest

    @UnitsEatenByRats.setter
    def UnitsEatenByRats(self, value):
        self._unitsEatenByRats = value

    @LandPrice.setter
    def LandPrice(self, value):
        self._landPrice = value

    @Units.setter
    def Units(self, value):
        self._units = value

    @AcresToBuyOrSell.setter
    def AcresToBuyOrSell(self, acres):
        self._acresToBuyOrSell = acres

    @UnitsToFeed.setter
    def UnitsToFeed(self, value):
        self._unitsToFeed = value

    @AcresToHarvest.setter
    def AcresToHarvest(self, acres):
        self._acresToHarvest = acres