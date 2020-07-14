class Question(object):
    def __init__(self, id, text, choice_a, choice_b, choice_c, correctChoice, difficulty):
        self._id = id
        self._text = text
        self._choice_a = choice_a
        self._choice_b = choice_b
        self._choice_c = choice_c
        self._correctChoice = correctChoice
        self._difficulty = difficulty

    @property
    def ID(self):
        return self._id

    @property
    def Text(self):
        return self._text

    @property
    def Choice_a(self):
        return self._choice_a

    @property
    def Choice_b(self):
        return self._choice_b

    @property
    def Choice_c(self):
        return self._choice_c

    @property
    def CorrectChoice(self):
        return self._correctChoice

    @property
    def Difficulty(self):
        return self._difficulty

    @staticmethod
    def readQuestion(line):
        parts = line.split(";")
        id = int(parts[0].strip())
        text = parts[1].strip()
        choice_a = parts[2].strip()
        choice_b = parts[3].strip()
        choice_c = parts[4].strip()
        correctChoice = parts[5].strip()
        difficulty = parts[6].strip()
        return Question(id, text, choice_a, choice_b, choice_c, correctChoice, difficulty)

    @staticmethod
    def writeQuestion(question):
        id = question._id
        text = question._text
        choice_a = question._choice_a
        choice_b = question._choice_b
        choice_c = question._choice_c
        correct_choice = question._correctChoice
        difficulty = question._difficulty
        return str(id) + ";" + text + ";" + choice_a + ";" + choice_b + ";" + choice_c + ";" + correct_choice + ";" + difficulty

    def questionForPlayer(self):
        return self._text + "\n" + self._choice_a + "\n" + self._choice_b + "\n" + self._choice_c + "\n"

    def __str__(self):
        return str(self._id) + " " + self._text + " " + self._choice_a + " " + self._choice_b + " " + self._choice_c + " " + self._correctChoice + " " + self._difficulty

    def __eq__(self, other):
        return self._id == other.ID

class Quiz(object):
    def __init__(self, difficulty, numberOfQuestions, file):
        self._difficulty = difficulty
        self._numberOfQuestions = numberOfQuestions
        self._file = file
        self._questions = [None for i in range(self._numberOfQuestions)]

    @property
    def Difficulty(self):
        return self._difficulty

    @property
    def NumberOfQuestions(self):
        return self._numberOfQuestions

    @property
    def File(self):
        return self._file

    @property
    def Questions(self):
        return self._questions

    @Questions.setter
    def Questions(self, questions):
        self._questions = questions