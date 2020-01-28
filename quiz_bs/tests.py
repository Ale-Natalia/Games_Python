import unittest
from service import Service, QuestionService, QuizService
from quizToPlay import QuizToPlay
from repo import Repo, FileRepo, Quiz
from domain import Question
from validators import QuestionValidator, QuizValidator

import os

class MyTestCase(unittest.TestCase):
    def test_addQuestion_valid(self):
        masterQuestionList = Repo()
        questionValidator = QuestionValidator()
        service = QuestionService(masterQuestionList, questionValidator)
        quizToPlay = QuizToPlay("")

        service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard.")
        self.assertEqual(str(masterQuestionList.ListOfAll[0]), "1 Who is the president of the US Donald Duck Donald Trump Dumbo the elephant Donald Trump hard")

    def test_addQuestion_invalid_duplicateID(self):
        masterQuestionList = Repo()
        questionValidator = QuestionValidator()
        service = QuestionService(masterQuestionList, questionValidator)
        quizToPlay = QuizToPlay("")

        service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard.")
        try:
            service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard.")
        except ValueError as error:
            self.assertEqual(str(error), "Duplicate ID!")

    def test_addQuestion_invalid_wrongFormat(self):
        masterQuestionList = Repo()
        questionValidator = QuestionValidator()
        service = QuestionService(masterQuestionList, questionValidator)
        quizToPlay = QuizToPlay("")

        try:
            service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard;easy.")
        except ValueError as error:
            self.assertEqual(str(error), "Question should be of structure id;text;xhoixe_a;choice_b;choice_c;correct_choice;difficulty.")

    def test_createQuiz_valid(self):
        masterQuestionList = Repo()
        questionValidator = QuestionValidator()
        service = QuestionService(masterQuestionList, questionValidator)

        quizRepo = Repo()
        quizValidator = QuizValidator()
        quizService = QuizService(quizRepo, masterQuestionList, quizValidator)

        quizToPlay = QuizToPlay("")
        service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard.")
        service.add("4;What does the fox say;Meow;Woof;Ringringring;Ringringring;medium.")
        service.add("2;Which is prime;1;3;9;3;easy.")
        service.add("3;Which is prime;1;2;9;2;easy.")

        quizService.createQuiz("easy 3 easytest.txt")
        self.assertEqual(os.path.exists("easytest.txt"), True)
        open("easytest.txt", "w").close()
        os.remove("easytest.txt")

    def test_createQuiz_invalid_notEnoughQuestionsDifficulty_error(self):
        masterQuestionList = Repo()
        questionValidator = QuestionValidator()
        service = QuestionService(masterQuestionList, questionValidator)

        quizRepo = Repo()
        quizValidator = QuizValidator()
        quizService = QuizService(quizRepo, masterQuestionList, quizValidator)

        quizToPlay = QuizToPlay("")
        service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard.")
        service.add("4;What does the fox say;Meow;Woof;Ringringring;Ringringring;medium.")
        service.add("2;Which is prime;1;3;9;3;easy.")
        service.add("3;Which is prime;1;2;9;2;easy.")

        try:
            quizService.createQuiz("hard 4 hardtest.txt")
        except ValueError as error:
            self.assertEqual(str(error), "Not enough questions of given difficulty to create quiz!")

    def test_createQuiz_invalid_notEnoughQuestionsDifficulty_fileNotCreated(self):
        masterQuestionList = Repo()
        questionValidator = QuestionValidator()
        service = QuestionService(masterQuestionList, questionValidator)

        quizRepo = Repo()
        quizValidator = QuizValidator()
        quizService = QuizService(quizRepo, masterQuestionList, quizValidator)

        quizToPlay = QuizToPlay("")
        service.add("1;Who is the president of the US;Donald Duck;Donald Trump;Dumbo the elephant;Donald Trump;hard.")
        service.add("4;What does the fox say;Meow;Woof;Ringringring;Ringringring;medium.")
        service.add("2;Which is prime;1;3;9;3;easy.")
        service.add("3;Which is prime;1;2;9;2;easy.")

        try:
            quizService.createQuiz("hard 4 hardtest.txt")
        except ValueError as error:
            pass
        self.assertEqual(os.path.exists("hardtest.txt"), False)


if __name__ == '__main__':
    unittest.main()
