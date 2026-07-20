# Making a rock, paper, scissors game 

import random
option = ["rock" , "paper" , "scissors"]
comp_score = 0
user_score = 0

while True:
    com = random.choice(option)
    request = bool(input("Enter any letter to play the game : "))

    if request == True:
        user = str(input("Select rock , paper or scissors : "))
        user = user.lower()
        if user == "rock" and com == "paper":
            print(f"Oh You lost as you select {user} and computer selected {com}")
            comp_score += 1

        elif user == "paper" and com == "scissors":
            print(f"Oh You lost as you select {user} and computer selected {com}")
            comp_score += 1

        elif user == "scissors" and com == "rock":
            print(f"Oh You lost as you select {user} and computer selected {com}")
            comp_score += 1

        elif user == com :
            print("No one wins here!!! It ties")

        else:
            print("User wins here!!!!")
            user_score += 1


    else:
        print("Thanks for playing the game!!!")
        print(f'''
    SCORE CARD:
              Computer score : {comp_score}
               User score : {user_score}          
''')
        break