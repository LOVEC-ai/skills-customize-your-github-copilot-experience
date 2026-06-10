 # 📘 Assignment: Hangman Game

 ## 🎯 Objective

 Build a console-based Hangman game that practices string manipulation, loops, conditionals, and user input handling. Students will implement game logic to select a word, accept guesses, track progress, and display win/lose outcomes.

 ## 📝 Tasks

 ### 🛠️ Build the Hangman Game

 #### Description
 Implement a playable Hangman game in Python. The program should randomly select a word from a predefined list, display the word as blanks, accept single-letter guesses from the player, reveal correct letters in their positions, track guessed letters and remaining attempts, and end the game with a win or lose message.

 #### Requirements
 Completed program should:

- Randomly select a word from a predefined list (in-code list or external data file).
- Display the word progress using underscores and revealed letters (e.g., `_ a _ _ m a n`).
- Accept only single-letter guesses and validate input.
- Show a list of letters already guessed.
- Decrement remaining attempts for incorrect guesses and display remaining attempts.
- End the game when the word is fully revealed (win) or attempts reach zero (lose).
- Print a clear win or lose message and reveal the full word on loss.

 #### Example

 Input/Output example (user input in bold):

 ```
 Word: _ _ _ _ _
 Guessed: 
 Attempts left: 6
 Guess a letter: **a**
 Word: _ a _ _ _
 Guessed: a
 Attempts left: 6
 Guess a letter: **z**
 Incorrect! Attempts left: 5
 ```

 Optional enhancements (not required):

- Load words from `assignments/games-in-python/data.csv` or another data file.
- Add difficulty levels that change word length or allowed attempts.
- Implement a simple ASCII-art hangman that updates with each wrong guess.

