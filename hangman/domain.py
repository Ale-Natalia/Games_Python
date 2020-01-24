class Sentence(object):
    def __init__(self, fullSentence):
        self._fullSentence = fullSentence
        self._length = len(fullSentence)
        self._sentenceToDisplay = ""

    @property
    def FullSentence(self):
        return self._fullSentence

    @FullSentence.setter
    def FullSentence(self, sentence):
        self._fullSentence = sentence

    @property
    def Length(self):
        return self._length

    @property
    def SentenceToDisplay(self):
        return self._sentenceToDisplay

    @SentenceToDisplay.setter
    def SentenceToDisplay(self, sentence):
        self._sentenceToDisplay = sentence

    @staticmethod
    def read(line):
        sentence = line.strip()
        return Sentence(sentence)

    @staticmethod
    def write(sentence):
        return sentence._fullSentence