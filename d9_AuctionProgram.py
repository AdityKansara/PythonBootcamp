# AuctionProgram
from Resources import logo

print(logo.auction_logo)
print("Welcome to the secret auction program.")
others = "yes"
bid = {}
while others == "yes":
    name = input("What is your name? ")
    bid_value = int(input("What is your bid? $"))
    others = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 100)

    bid[name] = bid_value

max_bid = 0
winner = ""
for bidder in bid:
    if bid[bidder] > max_bid:
        max_bid = bid[bidder]
        winner = bidder
print(f"The winner is {winner} with a bid of ${max_bid}.")
