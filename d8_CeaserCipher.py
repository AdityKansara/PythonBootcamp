# CaeserCipher
from Resources import logo

print(logo.caesercipher_logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
rerun = "yes"


def caeser(msg, key, choose):
    output = ""
    if choose == "decode":
        key *= -1
    for letter in msg:
        if letter in alphabet:
            output += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        else:
            output += letter
    print(f"Here's the output version {output}")


while rerun == "yes":
    choose = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    msg = input("Type your message:\n").lower()
    key = int(input("Type your key:\n"))
    caeser(msg, key, choose)
    rerun = input("Type yes if you want to run again, otherwise no\n").lower()
