import random

class GamePlay(object):
    def __init__(self, filename, chosenSentence):
        self._filename = filename
        self._chosenSentence = chosenSentence

    @property
    def FullSentence(self):
        return self._chosenSentence.FullSentence

    @property
    def SentenceToDisplay(self):
        return self._chosenSentence.SentenceToDisplay

    @property
    def HangmanToDisplay(self):
        return self._chosenSentence.HangmanToDisplay

    @property
    def Guesses(self):
        return self._chosenSentence.Guesses

    def guess(self, letter):
        '''
        the player makes the guess
        :param letter: the letter to guess
        :return: the fills are made accoridngly
        '''
        self._chosenSentence.guess(letter)

    def playerWon(self):
        '''

        :return: True/False (won/didn't)
        '''
        if self._chosenSentence.FullSentence == self._chosenSentence.SentenceToDisplay:
            return True
        return False

    def computerWon(self):
        '''

        :return: True/False (won/didn't)
        '''
        if self._chosenSentence.Hangman == self._chosenSentence.HangmanToDisplay:
            return True
        return False

    def isEndGame(self):
        '''
        is the game over?
        :return: boolean value
        '''
        if self.playerWon() or self.computerWon():
            return True
        return False

    def chooseSentence(self):
        '''

        :return: a randomly chosen sentence
        '''
        self._chosenSentence.FullSentence = random.choice(open(self._filename).read().splitlines()).strip("\n")
        self._chosenSentence.Length = len(self._chosenSentence.FullSentence)
