# RockPaperScissor
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
      """

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock, paper, scissor]

user = int(input("What do you choose? rock - 0, paper - 1 or scissor - 2 \n"))
computer = random.randint(0, 2)
while user > 2:
    user = int(input("What do you choose? rock - 0, paper - 1 or scissor - 2 \n"))
print(rps[user])
print("Computer chose:")
print(rps[computer])

if user == computer:
    print("It's a Draw")
elif user == 0 and computer == 2:
    print("You Win!")
elif computer == 0 and user == 2:
    print("You Lose!")
elif computer > user:
    print("You Lose!")
else:
    print("You Win!")
