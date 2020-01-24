import unittest
from gamePlay import GamePlay
from chosenSentence import ChosenSentence
from service import Service
from repo import Repo
from domain import Sentence

class MyTestCase(unittest.TestCase):
    def test_chosenSentence_SentenceToDisplay(self):
        sentence = Sentence("i am new here")
        chosenSentence = ChosenSentence(sentence)
        gamePlay = GamePlay("", chosenSentence)
        chosenSentence.initializeSentenceToDisplay()
        self.assertEqual(sentence.SentenceToDisplay, "i __ _e_ _e_e")

    def test_chosenSentence_hangman(self):
        sentence = Sentence("i am new here")
        chosenSentence = ChosenSentence(sentence)
        gamePlay = GamePlay("", chosenSentence)
        chosenSentence.initializeSentenceToDisplay()
        gamePlay.guess("z")
        self.assertEqual(chosenSentence.HangmanToDisplay, "h")

    def test_gameOver(self):
        sentence = Sentence("ana")
        chosenSentence = ChosenSentence(sentence)
        gamePlay = GamePlay("", chosenSentence)
        chosenSentence.initializeSentenceToDisplay()
        gamePlay.guess("n")
        self.assertEqual(gamePlay.isEndGame(), True)

    def test_playerWon(self):
        sentence = Sentence("ana")
        chosenSentence = ChosenSentence(sentence)
        gamePlay = GamePlay("", chosenSentence)
        chosenSentence.initializeSentenceToDisplay()
        gamePlay.guess("n")
        self.assertEqual(gamePlay.playerWon(), True)

    def test_computerWon(self):
        sentence = Sentence("ana")
        chosenSentence = ChosenSentence(sentence)
        gamePlay = GamePlay("", chosenSentence)
        chosenSentence.initializeSentenceToDisplay()
        gamePlay.guess("b")
        gamePlay.guess("c")
        gamePlay.guess("d")
        gamePlay.guess("e")
        gamePlay.guess("f")
        gamePlay.guess("g")
        gamePlay.guess("h")
        self.assertEqual(gamePlay.computerWon(), True)

if __name__ == '__main__':
    unittest.main()
