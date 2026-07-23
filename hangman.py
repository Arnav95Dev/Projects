# Tic,tac and toe game operated by computer
import random
import time

ops = ["python" , "programming" , "developer" , "he","she" , "computer" , "hangman" , "play"]
comp_response = random.choice(ops)


lives = 4

while (lives > 0):
    print(f"You have {lives} chances ")
    time.sleep(1)
    print("Your game is being started")
    print(f"Loading:")
    time.sleep(3)
    print("Your game is getting started")
    time.sleep(1)
    
    print("Your options :[python , programming , developer , he , she , computer , hangman , play ")
    user = str(input("Guess the word: "))

    
    if user == comp_response:
        print("Yay, You guessed it right !")
        break
        

    else :
        print("Nah, You guessed it wrong!")
        lives -= 1

else:
    print("Ops all your chances are over !")
    print(f"The answer was: {comp_response}")
    