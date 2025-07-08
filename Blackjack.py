# BlackJack
import random
import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal():
    dealedCard = random.choice(cards)
    return dealedCard


def calculateTotal(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def compare(user, dealer):
    if user == dealer:
        print("It's a DRAW!")
    elif dealer == 0:
        print("Dealer has BLACKJACK, you LOSE!")
    elif user == 0:
        print("You have BLACKJACK, you WIN!")
    elif user > 21:
        print("You went over, you LOSE!")
    elif dealer > 21:
        print("Dealer went over, you WIN!")
    elif user > dealer:
        print("You have higer cards, you WIN!")
    else:
        print("Delaer has higher card, you LOSE!")


def play_game():
    print(logo.blackjack_logo)
    myDeal = []
    dealerDeal = []
    gameOver = False

    for _ in range(2):
        myDeal.append(deal())
        dealerDeal.append(deal())

    while not gameOver:
        userTotal = calculateTotal(myDeal)
        dealerTotal = calculateTotal(dealerDeal)
        print(f"Your cards are {myDeal}")
        print(f"Your current score is {userTotal}")
        print(f"Dealer's card {dealerDeal[0]}")

        if userTotal == 0 or dealerTotal == 0 or userTotal > 21:
            gameOver = True
        else:
            want_to_draw = input("Do you want to draw another card?")
            if want_to_draw == "y":
                myDeal.append(deal())
            else:
                gameOver = True

    while dealerTotal != 0 and dealerTotal <= 17:
        dealerDeal.append(deal())
        dealerTotal = calculateTotal(dealerDeal)

    print(f"Your final cards were {myDeal} that totals to {userTotal}")
    print(f"Dealer's final cards were {dealerDeal} that totals to {dealerTotal}")
    compare(userTotal, dealerTotal)


while input("Do you want to play blackjack game?") == "y":
    print("\n" * 10)
    play_game()
