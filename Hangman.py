# Hangman
from Resources import data, logo
import random

print(logo.hangman_logo)
current_word = random.choice(data.word_list)

final_word = "_" * len(current_word)
print(final_word)
gameOver = False
correct_letter = []
lives = 5
while not gameOver:
    display_word = ""
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter not in current_word:
        print(f"You guessed {guessed_letter}, that's not in word. You lose life!")
        lives = lives - 1
    else:
        print(f"You have already guessed {guessed_letter}, guess a new word!")

    for letter in current_word:
        if letter == guessed_letter:
            display_word += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display_word += letter
        else:
            display_word += "_"

    print(display_word)
    print(logo.hanglist[lives])
    print(f"******************* {lives} LIVES LEFT********************")

    if "_" not in display_word:
        print("************************YOU WIN*************************")
        gameOver = True

    if lives == 0:
        print(f"******************YOU LOSE, IT WAS {current_word}*******************")
        gameOver = True
