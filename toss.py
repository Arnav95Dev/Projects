# Let's toss a coin

import random

option = [ "H" , "T"]

comp_score = 0
man_score = 0

while True:
    comp = random.choice(option)
    request = bool(input("Enter any key to play the game"))

    if request == True:
        user = str(input("Head(H) or Tail(T): "))

        if user == "T" and comp == "H":
            print("You lost the toss!")
            comp_score += 1

        elif user == "H" and comp == "T":
            print("You lost the toss!")
            comp_score += 1

        else :
            print("YAY ! You won the toss")
            man_score += 1
            print(f'''
SCORE CARD :
                  computer score = {comp_score}
                  User score = {man_score}
                  ''')

    else:
        print("You don't wanna play >: <")
        print("As your wish !")
        break