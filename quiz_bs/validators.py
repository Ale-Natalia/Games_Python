from domain import Question
from repo import Quiz

class QuestionValidator(object):
    def validateQuestion(self, question):
        '''
        raises errors if the question has a wrong format
        :param question: the question as provided by the user
        :return: if the question string is valid, the question object is returned
        '''
        parts = question.split(";")
        if len(parts) != 7:
            raise ValueError("Question should be of structure id;text;xhoixe_a;choice_b;choice_c;correct_choice;difficulty.")
        try:
            id = int(parts[0].strip())
        except ValueError:
            raise ValueError("ID should be integer!")
        text = parts[1].strip()
        choice_a = parts[2].strip()
        choice_b = parts[3].strip()
        choice_c = parts[4].strip()
        correctChoice = parts[5].strip()
        if correctChoice not in [choice_a, choice_b, choice_c]:
            raise ValueError("Correct choice needs to be among choice_a, choice_b, choice_c!")
        difficulty = parts[6].strip()
        if difficulty[-1] != ".":
            raise ValueError("Command needs to end with <.> - period")
        difficulty = difficulty[:-1]
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty needs to be easy/medium/hard!")
        return Question(id, text, choice_a, choice_b, choice_c, correctChoice, difficulty)

class QuizValidator(object):
    def validateQuiz(self, quizAsString):
        parts = quizAsString.split(" ")
        if len(parts) != 3:
            raise ValueError("Quiz needs to be of structure difficulty numberOfQuestions filename")
        difficulty = parts[0].strip()
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Difficulty needs to be easy/medium/hard!")
        try:
            numberOfQuestions = int(parts[1].strip())
        except ValueError:
            raise ValueError("Number of questions should be integer!")
        file = parts[2].strip()
        return [difficulty, numberOfQuestions, file]

class QuizToPlayValidator(object):
    pass