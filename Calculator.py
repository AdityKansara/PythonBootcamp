# Calculator
import logo


def sum(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operatinos = {"+": sum, "-": minus, "*": multiply, "/": divide}


def calc():
    print(logo.calc_logo)
    should_continue = "y"
    num1 = int(input("What's first number?: "))

    while should_continue == "y":
        print("+\n-\n*\n/\n")
        op = input("pick operation: ")
        num2 = int(input("What's next number?: "))

        ans = operatinos[op](num1, num2)
        print(f"{num1}{op}{num2}={ans}")

        should_continue = input(
            "Type y to continue calculating, or type n to start new."
        )
        if should_continue == "y":
            num1 = ans
        else:
            should_continue == "n"
            print("\n" * 20)
            calc()


calc()
