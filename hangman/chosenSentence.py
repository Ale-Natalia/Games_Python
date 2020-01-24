class ChosenSentence(object):
    def __init__(self, sentence):
        self._sentence = sentence
        self._guesses = []
        self._hangman = "hangman"
        self._hangmanToDisplay = ""
        self._numberOfWrongGuesses = 0

    @property
    def Sentence(self):
        return self._sentence

    @Sentence.setter
    def Sentence(self, sentence):
        self._sentence = sentence

    @property
    def FullSentence(self):
        return self._sentence.FullSentence

    @FullSentence.setter
    def FullSentence(self, sentence):
        self._sentence.FullSentence = sentence

    @property
    def SentenceToDisplay(self):
        return self._sentence.SentenceToDisplay

    @property
    def Hangman(self):
        return self._hangman

    @property
    def HangmanToDisplay(self):
        return self._hangmanToDisplay

    @property
    def Guesses(self):
        return self._guesses

    def initializeSentenceToDisplay(self):
        '''\
        the sentence is initialized with spaces, underscores and the first/last letter in all the positions
        '''
        if len(self._sentence.FullSentence) > 0:
            self._guesses.append(self._sentence.FullSentence[0])
            self._guesses.append(self._sentence.FullSentence[-1])
        firstCharacter = self._sentence.FullSentence[0]
        lastCharacter = self._sentence.FullSentence[-1]
        for character in self._sentence.FullSentence:
            if character in [firstCharacter, lastCharacter, " "]:
                self._sentence.SentenceToDisplay += character
            else:
                self._sentence.SentenceToDisplay += "_"

    def fillSentence(self, letter):
        '''

        :param letter: the correctly guessed letter
        :return: the display sentence is filled with the letter in all the positions
        '''
        for characterIndex in range(len(self._sentence.FullSentence)):
            if self._sentence.FullSentence[characterIndex] == letter:
                self._sentence.SentenceToDisplay = self._sentence.SentenceToDisplay[:characterIndex] + letter + self._sentence.SentenceToDisplay[characterIndex+1:]

    def fillHangman(self):
        '''
        :return:         the hangman word is filled if the user guessed incorrectly
        '''
        self._numberOfWrongGuesses += 1
        self._hangmanToDisplay += self._hangman[self._numberOfWrongGuesses - 1]

    def guess(self, letter):
        '''
        the guess is made
        :param letter: the letter that the player is trying to guess
        :return: the sentence/ hangman word is filled accordingly
        '''
        if len(letter) > 1:
            raise ValueError("Letter length must be (obviously) 1")
        if not (letter >= "a" and letter <= "z"):
            raise ValueError("You must guess a letter!")
        if letter in self._guesses:
            raise ValueError("You already tried to guess this letter!")
        if letter in self._sentence.FullSentence:
            self.fillSentence(letter)
        else:
            self.fillHangman()
        self._guesses.append(letter)