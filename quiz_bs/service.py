from copy import *
from random import *
from domain import Question
from repo import Quiz

class Service(object):
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator

class QuestionService(Service):
    def __init__(self, repo, validator):
        Service.__init__(self, repo, validator)

    def add(self, questionAsString):
        '''
        a question is added to the list of questions
        :param questionAsString: the question as provided by the user
        :return: the question is added or an error is raised
        '''
        question = self._validator.validateQuestion(questionAsString)
        self._repo.add(question)

    def initialize(self):
        '''
        initializes the list at startup by uploading all the questions from file into memory
        :return: the list is initialized
        '''
        self._repo.initialize()

class QuizService(Service):
    def __init__(self, repo, masterList, validator):
        Service.__init__(self, repo, validator)
        self._masterList = masterList

    def questionsForQuiz(self, difficulty, numberOfQuestions):
        '''
        picks the questions for a quiz
        :param difficulty: given difficulty
        :param numberOfQuestions: given no. of questions
        :return: the list of questions or raises an error if the quiz could not be created
        '''
        currentNumberOfQuestions = 0
        necessaryNumberOfQuestionsWithGivenDifficulty = numberOfQuestions//2
        listOfPossibleQuestions = deepcopy(self._masterList.ListOfAll)
        if numberOfQuestions > len(listOfPossibleQuestions):
            raise ValueError("Not enough questions in master question list!")
        listOfQuestions = []
        for question in listOfPossibleQuestions:
            if question.Difficulty == difficulty:
                listOfQuestions.append(question)
                currentNumberOfQuestions += 1
                listOfPossibleQuestions.remove(question)
            if currentNumberOfQuestions >= necessaryNumberOfQuestionsWithGivenDifficulty:
                break
        if currentNumberOfQuestions < necessaryNumberOfQuestionsWithGivenDifficulty:
            raise ValueError("Not enough questions of given difficulty to create quiz!")
        for question in listOfPossibleQuestions:
            newQuestion = choice(listOfPossibleQuestions)
            listOfQuestions.append(newQuestion)
            currentNumberOfQuestions += 1
            listOfPossibleQuestions.remove(newQuestion)
            if currentNumberOfQuestions == numberOfQuestions:
                return listOfQuestions

    def createQuiz(self, quiz):
        '''
        creates a quiz with given requirements if possible or raises an error otherwise
        :param quiz: the quiz requirements as provided by the user
        :return:
        '''
        quizSpecifications = self._validator.validateQuiz(quiz)
        difficulty = quizSpecifications[0]
        numberOfQuestions = quizSpecifications[1]
        file = quizSpecifications[2]
        questionList = self.questionsForQuiz(difficulty, numberOfQuestions)
        quiz = Quiz(difficulty, numberOfQuestions, file, Question.readQuestion, Question.writeQuestion)
        quiz.ListOfAll = questionList
        quiz.updateFile(questionList)

class QuizToPlayService(Service):
    def __init__(self, quizToPlay, validator):
        Service.__init__(self, quizToPlay, validator)

    def initializeQuiz(self, file):
        self._repo.File = file
        self._repo.initializeQuiz()

    def displayQuestion(self):
        return self._repo.displayQuestion()

    def answerQuestion(self, choice):
        return self._repo.answer(choice)

    def isQuizOver(self):
        return self._repo.isQuizOver()

    @property
    def Score(self):
        return self._repo.NumberOfPoints

    @property
    def MaximumScore(self):
        return self._repo.MaximumScore