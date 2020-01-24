class Hangman(object):
    def __init__(self, service, gamePlay):
        self._service = service
        self._gamePlay = gamePlay
        self._endGame = False

    def printStartMenu(self):
        print("1. Add sentences to repo")
        print("2. Start game")
        print("0. Exit")

    def printGameMenu(self):
        print("1. Make your turn")
        print("2. See letters you've already tried")
        print("3. Cheat (although you shouldn't)")
        print("0. Exit")

    def addSentence(self):
        sentence = input("The sentence you want to add:\n")
        try:
            self._service.add(sentence)
        except ValueError as error:
            print(error)
            print("Try again!")
            self.addSentence()

    def gameOverMessage(self):
        if self._gamePlay.playerWon():
            return "Congrats! You won!"
        return "Oh no! You lost!"

    def guesses(self):
        print("Letters you've already tried: " + str(self._gamePlay.Guesses))

    def cheat(self):
        print(self._gamePlay.FullSentence)

    def turn(self):
        print(self._gamePlay.SentenceToDisplay)
        letterGuess = input("Guess a letter: ")
        try:
            self._gamePlay.guess(letterGuess)
            print(self._gamePlay.SentenceToDisplay)
            print(self._gamePlay.HangmanToDisplay)
            if self._gamePlay.isEndGame():
                self._endGame = True
                print(self.gameOverMessage())
        except ValueError as error:
            print(error)
            print("Try again")
            self.turn()

    def playGame(self):
        while not self._endGame:
            self.printGameMenu()
            choice = input("Make your choice: ")
            if choice == "1":
                self.turn()
                self.playGame()
                break
            elif choice == "2":
                self.guesses()
                self.playGame()
                break
            elif choice == "3":
                self.cheat()
                self.playGame()
                break
            elif choice == "0":
                break
            else:
                print("Invalid choice. Must be 0-3")

    def run(self):
        playing = False
        while not playing:
            self.printStartMenu()
            choice = input("Make your choice: ")
            if choice == "1":
                self.addSentence()
                self.run()
                break
            elif choice == "2":
                self.playGame()
                break
            elif choice == "0":
                break
            else:
                print("Invalid choice. Must be 0-2")