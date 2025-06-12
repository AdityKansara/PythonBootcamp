#TreasureIsland
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
direction = input("You're at cross road. Where do you want to go?\n Type \"left\" or \"right\" \n").lower()

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    swim= input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if swim == "wait":
        print("You've arrived at the island unharmed. There is a house with three doors. One red, one yellow one blue.")
        door = input("Which colour door you want to open?\n").lower()
        if door != "yellow":
            print("Game Over")
        else:
            print("You Win!")
    else:
        print("You've drown. Game Over")
else:
    print("You fell into a hole. Game Over")
