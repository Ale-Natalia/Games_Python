class SentenceValidator(object):
    def validateSentence(self, sentence):
        sentenceToSearchIn = sentence.FullSentence.lower()
        for character in sentenceToSearchIn:
            if not ((character >= "a" and character <= "z") or character == " "):
                raise ValueError("Sentence can only contain letters of the English alphabet and spaces!")