class QuizToPlay(object):
    def __init__(self, readEntity):
        self._file = None
        self._numberOfPoints = 0
        self._questionNumber = -1
        self._maximumScore = 0
        self._entities = []
        self._readEntity = readEntity

    @property
    def NumberOfPoints(self):
        return self._numberOfPoints

    @NumberOfPoints.setter
    def NumberOfPoints(self, number):
        self._numberOfPoints = number

    @property
    def MaximumScore(self):
        return self._maximumScore

    @MaximumScore.setter
    def MaximumScore(self, number):
        self._maximumScore = number

    @property
    def File(self):
        return self._file

    @File.setter
    def File(self, file):
        self._file = file

    def answer(self, choice):
        question = self._entities[self._questionNumber]
        if choice == question.CorrectChoice:
            if question.Difficulty == "easy":
               self._numberOfPoints += 1
            elif question.Difficulty == "medium":
               self._numberOfPoints += 2
            elif question.Difficulty == "hard":
                self._numberOfPoints += 3
            return "You are right!"
        return "You are wrong. " + question.CorrectChoice + " was the right answer."

    def __readAllFromFile(self):
        self._entities = []
        try:
            with open(self._file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line.strip()
                    if line != "":
                        entity = self._readEntity(line)
                        self._entities.append(entity)
                        question = entity
                        if question.Difficulty == "easy":
                            self._maximumScore += 1
                        elif question.Difficulty == "medium":
                            self._maximumScore += 2
                        elif question.Difficulty == "hard":
                            self._maximumScore += 3
        except FileNotFoundError:
            raise ValueError("File not found!")

    def initializeQuiz(self):
        self.__readAllFromFile()

    def displayQuestion(self):
        self._questionNumber += 1
        return self._entities[self._questionNumber].questionForPlayer()

    def isQuizOver(self):
        return self._questionNumber == len(self._entities) - 1