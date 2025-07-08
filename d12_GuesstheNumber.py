#Guess the Number
import random
import logo
print(logo.guessinggame_logo)
print("Welcome to Guess the Number Game!")
print("I am thinking of a number between 1 and 100")

number = random.randint(1,100)

difficulty = input("Choose difficulty level: 'hard' or 'easy': ")
noOfAttempts = 10

if difficulty == 'hard':
    noOfAttempts = 5
elif difficulty == 'easy':
    noOfAttempts = 10
else:
    print("Wrong input! By default difficulty is chosen easy!")

win = False

while not win and noOfAttempts > 0:
    print(f"You have {noOfAttempts} attempts remaining to guess")
    guessed_number = int(input("Make a guess:"))

    if guessed_number < number:
        print("Too Low! \nGuess again!")
        noOfAttempts -= 1
    elif guessed_number > number:
        print("Too High! \nGuess again!")
        noOfAttempts -= 1
    else:
        print("You Win!")
        win = True

    if noOfAttempts == 0:
        print("You are Loser!!")
        print(f"Correct number was {number}")