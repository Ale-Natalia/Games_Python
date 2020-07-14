# Games

* Battleship
  - the classic battleship game with a console-based interface
  - human vs computer
  - Rules:
    - in the beginning, the player can place two ships with the command: "ship C1L1C2L2C3L3", where the columns are letters from A-F and lines are numbers from 0-5
    - the player can try to place as many ships as they like; the last 2 will be taken into consideraton
    - when the player is ready, they need to type start
    - from now on, the possible commands are:
      - "attack CL"
      - "cheat" - the opponent's board is shown
      - "exit"
    - the hit spots are represented as "o", the spots where a battleship is placed as "+", while the empty ones are shown as "."
    
* Hangman
  - a console-based version of the Hangman game
  - the computer randomly selects a sentence from the file and the human player attempts to guess it
  - Rules:
    - the computer displays the sentence with underscores instead of letters, showing only the first and last letter of every word and the apparitions of these letters within words
    - the player attempts to guess by typing a letter
    - starting from an empty string, the computer fills a new letter in the word "hangman" for each wrong guess
    - if "hangman" is complete, the player loses; if the player guesses the sentence before, the player wins
    
* Minesweeper
  - a console-based version of the classical Minesweeper game
  - customizable board size and number of mines
  - menu-based controls
  - Rules:
    - 1. Game Settings - choose the width, height and number of mines
    - 2. Start game
      - 1. Mark tile as safe - type the coordinates of the tile you want to mark as safe
      - 2. Mark tile with flag - type the coordinates of the tile you believe has a mine
      - 3. Remove flag from tile - type the coordinates of the tile from where you want to remove the tile
      - 4. Cheat - see where the mines are
 
* Quiz
  - a console-based application that allows creating and solving quizzes
  - Commands:
    - "add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty>" - the user can add a question to the master question list
    - "create <difficulty><number_of_questions><file>" - the user can create a new quiz
      - difficulty: easy/medium/hard - at least half the questions are of the provided difficulty
      - number of questions - the number of questions in the quiz
      - file - the name of the file where the quiz is saved
    - "start <file>" - the user can take the quiz found at the provided location
      - the user types their choice for each question
      - the user receives their score at the end of the quiz
        - easy question - 1p
        - medium question - 2p
        - hard question - 3p
  
* Tic-tac-toe
  - a console-based 2-player version of the classical Tic-tac-toe game
  - custom board size and win size (length of segment that wins)
  - can be played human vs. human/ human vs. computer/ computer vs. computer
  - menu-based controls
  - Rules:
    - 1: Settings - choose the board size, the win size and the player types
    - 2. Start game
      - choose coordinates (row and column) to place tile by typing the numbers
      - the game ends when one of the players has completed a contiguous segment of the chosen length in row/column/diagonal or the board is full
