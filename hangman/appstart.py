from ui import Hangman
from gamePlay import GamePlay
from chosenSentence import ChosenSentence
from service import Service
from repo import Repo, FileRepo
from domain import Sentence
from validators import SentenceValidator

repo = FileRepo("sentences.txt", Sentence.read, Sentence.write)
sentenceValidator = SentenceValidator()
service = Service(repo, sentenceValidator)

sentence = Sentence("")
chosenSentence = ChosenSentence(sentence)
gamePlay = GamePlay("sentences.txt", chosenSentence)
gamePlay.chooseSentence()
chosenSentence.initializeSentenceToDisplay()

hangman = Hangman(service, gamePlay)

hangman.run()