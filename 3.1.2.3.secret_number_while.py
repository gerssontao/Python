#!/usr/bin/python3

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

playerNumber=int(input("Type your number to guess: "))

while secret_number!=playerNumber:
    print("Ha! ha! Nice try Mugle, you're stuck in my loop!")
    playerNumber=int(input("Type your number to guess: "))

print("Well done mugle, you're Free!")
