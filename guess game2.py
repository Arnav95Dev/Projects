# Creating a guess game where computer guesses a number 

import random

comp = random.randint(1,101)
attempt = 0 

while True:
    user = int(input("Guess a word between 1 to 100 : "))

    if user == comp :
        attempt += 1
        if attempt < 5 :
            print("Wow, you guessed it really quick!!")
            break

        else:
            print("HUH ! You are not that fast")
            break

    elif user > comp:
        print("Too HIGH")
        attempt += 1

    else:
        print("Too LOW")
        attempt += 1

print(attempt)