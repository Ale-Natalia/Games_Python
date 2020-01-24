from domain import Sentence

class Service(object):
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator

    def add(self, sentenceString):
        '''
        function for adding new sentences
        :param sentenceString: the sentence as the string
        :return: the sentence as an object is added
        '''
        sentenceString = sentenceString.lower()
        sentence = Sentence(sentenceString)
        self._validator.validateSentence(sentence)
        self._repo.addS(sentence)
