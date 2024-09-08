import random
import hangman_liat
import words

lives = 6
chosen_word = random.choice(words.word_list)
print(chosen_word)
display = ["_" for _ in range(len(chosen_word))]
print(display)

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter
    else:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
    
    if "_" not in display:
        game_over = True
        print("You Win!!")
    
    print(display)
    print(hangman_liat.hangman_stages[lives])
