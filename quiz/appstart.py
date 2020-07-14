from ui import UI
from service import Service, QuestionService, QuizService, QuizToPlayService
from quizToPlay import QuizToPlay
from repo import Repo, FileRepo, Quiz
from domain import Question
from validators import QuestionValidator, QuizValidator, QuizToPlayValidator

masterQuestionList = FileRepo("masterQuestionList.txt", Question.readQuestion, Question.writeQuestion)
questionValidator = QuestionValidator()
questionService = QuestionService(masterQuestionList, questionValidator)

quizRepo = Repo()
quizValidator = QuizValidator()
quizService = QuizService(quizRepo, masterQuestionList, quizValidator)

quizToPlay = QuizToPlay(Question.readQuestion)
quizToPlayValidator = QuizToPlayValidator()
quizToPlayService = QuizToPlayService(quizToPlay, quizToPlayValidator)



ui = UI(questionService, quizService, quizToPlayService)

ui.welcomeToQuiz()