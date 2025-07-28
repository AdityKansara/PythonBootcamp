# Higher Lower game

import random
from Resources import data, logo

INSTALIST = data.higherLower_list
score = 0
B = random.choice(INSTALIST)


def compare(A, B):
    return "A" if A["followers"] > B["followers"] else "B"


def higherLower():
    print(logo.higherLower_logo)
    global B, score
    while True:
        A = B
        B = random.choice(INSTALIST)
        while B == A:
            B = random.choice(INSTALIST)

        print("----------------------")
        print(f"{A['name']}")
        print(f"{A['desc']}")
        print("----------------------")

        print(logo.vs_logo)

        print("----------------------")
        print(f"{B['name']}")
        print(f"{B['desc']}")
        print("----------------------")

        ans = input("Who has more followers? 'A' or 'B': ").strip().upper()

        compared = compare(A, B)
        if ans == compared:
            score += 1
            print("Your Answer is correct!")
        else:
            print(f"Sorry that answer is wrong! \n Your total score is {score}")
            break


higherLower()
