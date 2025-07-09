# CoffeeMachine
import logo
import data

MENU = data.Tea_Menu
INITIAL_STOCK = {"milk": 500, "tea": 100, "water": 200, "money": 0}


def get_index(choice):
    index = next(
        (
            i
            for i, item in enumerate(MENU)
            if item["name"].strip().lower() == choice.strip().lower()
        ),
        -1,
    )
    return index


def check_stock(index):
    global INITIAL_STOCK
    print("Checking Stock")
    keys = list(INITIAL_STOCK.keys())

    for item in keys[:3]:
        if MENU[index]["ingredients"][item] <= INITIAL_STOCK[item]:
            INITIAL_STOCK[item] -= MENU[index]["ingredients"][item]
        else:
            print(f"OOPS! Not enough {item} in the machine!🫙")
            return False


def calculate_money(index, totalMoney):

    item = MENU[index]
    item_price = item["price"]
    print(f"Price for {item["name"]} is ₹ {item_price}")
    if item_price <= totalMoney:
        INITIAL_STOCK["money"] += item_price
        print("Credited Money to the Machine!! 💰")
        brew_tea()
        change(totalMoney - item_price)
        return True
    else:
        print("You don't have enough money!!💸")
        refund(totalMoney)
        return False


def brew_tea():
    print("Brewing Tea...🫖")
    print("Your Tea is ready!! ☕")


def refund(totalAmount):
    print(
        f"Refunding your money back to you safely...₹ ₹ ₹ \nRefund successful of ₹{totalAmount}"
    )


def change(amount):
    print(f"Here is your change...₹{amount}")
    print("Enjoy you tea!")


print(logo.Tea_logo)
choice = (
    input(
        "What would you like to have?\nGinger Tea 🫚 ☕\nBlack Tea ☕🖤\nMilk Tea 🧋\n"
    )
    .strip()
    .lower()
)
index = get_index(choice)
print(f"your index {index}")
check_stock(index)

print("Please insert coins!")
rs10 = int(input("How many 10₹ ?"))
rs5 = int(input("How many 5₹ ?"))
rs2 = int(input("How many 2₹ ?"))
rs1 = int(input("How many 1₹  ?"))

totalMoney = rs1 + (rs2 * 2) + (rs5 * 5) + (rs10 * 10)

calculate_money(index, totalMoney)
