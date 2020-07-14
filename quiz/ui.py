class UI(object):
    def __init__(self, questionService, quizService, quizToPlay):
        self._questionService = questionService
        self._quizService = quizService
        self._quizToPlayService = quizToPlay

    def welcomeToQuiz(self):
        self._questionService.initialize()
        print("Welcome to QUIZ MASTER 2000!")
        command = input("Your command: ")
        if command == "exit":
            return
        parts = command.split(" ")
        if len(parts) < 2:
            print("Invalid command!")
            self.welcomeToQuiz()
            return
        else:
            if parts[0].strip() == "add":
                try:
                    question = ""
                    for part in parts[1:]:
                        question += part + " "
                    self._questionService.add(question.strip())
                    self.welcomeToQuiz()
                    return
                except ValueError as error:
                    print(error)
                    self.welcomeToQuiz()
                    return
            elif parts[0].strip() == "create":
                try:
                    quiz = ""
                    for part in parts[1:]:
                        quiz += part + " "
                    self._quizService.createQuiz(quiz.strip())
                    self.welcomeToQuiz()
                    return
                except ValueError as error:
                    print(error)
                    self.welcomeToQuiz()
                    return
            elif parts[0].strip() == "start":
                try:
                    file = parts[1:]
                    if len(file) > 1:
                        print("Command must be <start #filename#>")
                        self.welcomeToQuiz()
                        return
                    file = file[0]  # turn the list into a string
                    try:
                        if file[-4:] != ".txt":
                            print("File name must be filename.txt")
                            self.welcomeToQuiz()
                            return
                    except IndexError:
                        print("File name must be filename.txt")
                        self.welcomeToQuiz()
                        return
                    self.playQuiz(file)
                    self.welcomeToQuiz()
                    return
                except ValueError as error:
                    print(error)
                    self.welcomeToQuiz()
                    return
            else:
                print("Invalid command!")
                self.welcomeToQuiz()
                return

    def displayQuestion(self):
        print(self._quizToPlayService.displayQuestion())

    def answerQuestion(self):
        choice = input("Your choice is: ")
        print(self._quizToPlayService.answerQuestion(choice))

    def printQuizOverMessage(self):
        print("You scored " + str(self._quizToPlayService.Score) + " out of a maximum of " + str(self._quizToPlayService.MaximumScore))

    def playQuiz(self, file):
        try:
            self._quizToPlayService.initializeQuiz(file)
        except ValueError as error:
            print(error)
            return
        isQuizOver = False
        while not isQuizOver:
            self.displayQuestion()
            self.answerQuestion()
            if self._quizToPlayService.isQuizOver():
                isQuizOver = True
                self.printQuizOverMessage()