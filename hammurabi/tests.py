import unittest
from repo import Repo
from game import Game
from validators import GameValidator

class MyTestCase(unittest.TestCase):
    def test_acresBuyOrSell_buy(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        game.acresBuyOrSell(100)
        game.buyOrSellAcres()
        self.assertEqual(repo.LandAcres, 1100)

    def test_acresBuyOrSell_sell(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        game.acresBuyOrSell(-100)
        game.buyOrSellAcres()
        self.assertEqual(repo.LandAcres, 900)

    def test_acresBuyOrSell_sell_invalid(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        try:
            game.acresBuyOrSell(-1000000)
        except ValueError as error:
            self.assertEqual(str(error), "You don't have 1000000 acres to sell!")


    def test_acresBuyOrSell_buy_invalid(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        try:
            game.acresBuyOrSell(1000000)
        except ValueError as error:
            self.assertEqual(str(error), "You don't have enough units to buy 1000000 acres!")

    def test_feedPopulation_valid(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        game.unitsToFeedPopulation(2000)
        game.feedPopulation()
        self.assertEqual(repo.Units, 800)

    def test_feedPopulation_invalid(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        try:
            game.unitsToFeedPopulation(300000)
        except ValueError as error:
            self.assertEqual(str(error), "You don't have enough units!")

    def test_feedPopulation_peopleStarved(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        game.unitsToFeedPopulation(0)
        game.feedPopulation()
        self.assertEqual(repo.PopulationStarved, 100)

    def test_peopleComeToCity_populationStarved(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        game.unitsToFeedPopulation(0)
        game.feedPopulation()
        self.assertEqual(repo.NewPopulation, 0)

    def test_peopleComeToCity_populationNotStarved(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        game.unitsToFeedPopulation(100)
        game.feedPopulation()
        self.assertGreaterEqual(repo.NewPopulation, 0)

    def test_harvestGrain(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        unitsBeginning = repo.Units
        game.acresToHarvest(100)
        game.harvestGrain()
        unitsAfterHarvest = repo.Units
        extraUnits = unitsAfterHarvest - unitsBeginning
        expectedExtraUnits = repo.Harvest * repo.AcresToHarvest
        self.assertEqual(extraUnits, expectedExtraUnits)

    def test_acresToHarvest_invalid_not_enough_acres(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        try:
            game.acresToHarvest(10000)
        except ValueError as error:
            self.assertEqual(str(error), "You don't have enough acres!")

    def test_acresToHarvest_invalid_not_enough_units(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        try:
            game.acresToHarvest(1000)
        except ValueError as error:
            self.assertEqual(str(error), "You don't have enough units to harvest these acres!")

    def test_ratsInfestation(self):
        repo = Repo()
        validator = GameValidator()
        game = Game(repo, validator)
        unitsBeginning = repo.Units
        percentEaten = game.ratsInfestation()
        if percentEaten is None:
            self.test_ratsInfestation()
            return
        unitsAfterRats = repo.Units
        unitsDropExpected = unitsBeginning - percentEaten * unitsBeginning // 100
        self.assertEqual(unitsAfterRats, unitsDropExpected)

if __name__ == '__main__':
    unittest.main()
