# This is level 2 of previous rock,paper,scissors game
import random
option = ["rock","paper","scissors"]
comp_score = 0
user_score = 0
draw = 0

while True:
    comp = random.choice(option)
    choice = str(input("If you want to exit the game type 'quit'"))

    if choice == "quit":
        print("Thanks for playing the game !")
        print(f'''
              SCORE CARD:
              User = {user_score}
              Computer = {comp_score}
              Draw = {draw}
            ''')
        break

    else :
        print("The game is about to begin:")
        user = str(input("'rock','paper','scissors'"))
        user = user.lower()
        if user in option:
            if user == "rock" and comp == "paper":
                print("You Lost!")
                comp_score += 1
                print(f"Computer chose : {comp}")

            elif user == "paper" and comp == "scissors":
               print("You Lost !")
               comp_score += 1
               print(f"Computer chose: {comp}")

            elif user == "scissors" and comp == "rock":
               print("You Lost !")
               comp_score += 1
               print(f"Computer chose : {comp}")

            elif user == comp:
               print("It's a Draw!!")
               draw += 1

            else :
               print("Yay ! You won ")
               user_score += 1
               print(f"Computer chose: {comp}")
        
        else:
            print("You did not typed what was written there !")