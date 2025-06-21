#Hangman
hanglist = [
    '''
    _______
    |/     /|
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
 ___|___
''',
    '''
    _______
    |/     /|
    |      (_)
    |      \\|/
    |       |
    |      /
    |
 ___|___
''',
    '''
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      
    |
 ___|___
''',
    '''
    _______
    |/      |
    |      (_)
    |      \\|/
    |       
    |      
    |
 ___|___
''',
    '''
    _______
    |/      |
    |      (_)
    |      
    |       
    |      
    |
 ___|___
''',
    '''
    _______
    |/      |
    | 
    |      
    |       
    |      
    |
 ___|___
'''
]

word_list = ["panipuri", "fafda", "jalebi", "vadapav"]
import random

current_word = random.choice(word_list)

final_word = "_"*len(current_word)
print(final_word)
gameOver = False
correct_letter = []
lives = 5
while not gameOver:
    display_word = ""
    guessed_letter = input("Guess a letter: ").lower()
    for letter in current_word:
        if letter == guessed_letter:
            display_word += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display_word+= letter
        else:
            display_word+= "_"
        
    if guessed_letter not in current_word:
        lives = lives - 1

    print(display_word)
    print(hanglist[lives])

    if "_" not in display_word:
        print("You win!")
        gameOver = True
    
    if lives == 0:
        print("you lose!")
        gameOver = True