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

    for item in MENU[index]["ingredients"]:
        if MENU[index]["ingredients"][item] > INITIAL_STOCK[item]:
            print(f"OOPS! Not enough {item} in the machine!🫙")
            return False

    for item in MENU[index]["ingredients"]:
        INITIAL_STOCK[item] -= MENU[index]["ingredients"][item]

    return True


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


def report():
    print("==============REPORT==============")
    print(f"Water : {INITIAL_STOCK['water']}ml")
    print(f"Milk : {INITIAL_STOCK['milk']}ml")
    print(f"Tea : {INITIAL_STOCK['tea']}g")
    print(f"Money : {INITIAL_STOCK['money']}₹")
    print("==================================")


def adiCafe():
    print(logo.Tea_logo)
    while True:
        choice = (
            input(
                "What would you like to have?\nGinger Tea 🫚 ☕\nBlack Tea ☕🖤\nMilk Tea 🧋\n"
            )
            .strip()
            .lower()
        )
        if choice == "report":
            report()
            continue

        index = get_index(choice)
        if index == -1:
            print("We don't serve that. Please check the spelling 🍵")
            continue
        if check_stock(index):

            print(f"Please insert ₹{MENU[index]["price"]} or more in coins!")
            rs10 = int(input("How many 10₹ ?"))
            rs5 = int(input("How many 5₹ ?"))
            rs2 = int(input("How many 2₹ ?"))
            rs1 = int(input("How many 1₹  ?"))

            totalMoney = rs1 + (rs2 * 2) + (rs5 * 5) + (rs10 * 10)

            calculate_money(index, totalMoney)

        more = input("Do you want to order again? ['y'/'n']").strip().lower()

        if more != "y":
            print("Thank you! Visit Again!!")
            break


adiCafe()
