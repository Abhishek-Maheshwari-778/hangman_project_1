import random
import hangman_liat  # Assuming this has the hangman ASCII art stored
import words  # Assuming this has the word list stored

def play_game():
    lives = 6
    chosen_word = random.choice(words.word_list).lower()
    print(f"(The word has {len(chosen_word)} letters)")  # Optional: reveal the word's length for the player

    display = ["_" for _ in range(len(chosen_word))]
    wrong_guesses = []  # To track incorrect guesses

    game_over = False
    while not game_over:
        print(f"\nCurrent word: {' '.join(display)}")
        guessed_letter = input("Guess a letter: ").lower()

        # Input validation: Check if input is a single letter
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Correct guess: Fill in the display
        if guessed_letter in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guessed_letter:
                    display[position] = guessed_letter
        else:
            if guessed_letter not in wrong_guesses:
                wrong_guesses.append(guessed_letter)
                lives -= 1
                print(f"Wrong guess! '{guessed_letter}' is not in the word. Lives left: {lives}")
                print("Incorrect guesses so far:", ', '.join(wrong_guesses))
            else:
                print(f"You already guessed '{guessed_letter}'. Try another one.")

        # Display current state of the game
        print(display)
        print(hangman_liat.hangman_stages[lives])

        # Check win condition
        if "_" not in display:
            game_over = True
            print(f"Congratulations! You've won! The word was '{chosen_word}'.")

        # Check lose condition
        if lives == 0:
            game_over = True
            print(f"You've lost! The word was '{chosen_word}'.")
    
    return input("Would you like to play again? (yes/no): ").lower() == "yes"


# Main game loop with restart functionality
while True:
    if not play_game():
        print("Thank you for playing! Goodbye!")
        break
