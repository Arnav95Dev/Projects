# Making a real text based game
import time
import random
enemy = random.randint(1,5)
lose = 0
print("Remember if you die game ends")
user = int(input("Enter a number between 1 to 5 (remember if your mumber matches the enemy game ends!!): "))

if user != enemy and user in [1,2,3,4,5]:
    time.sleep(0.8)
    print("Oh you are saved for this round!")
    time.sleep(1)
    print("Next round coming up!")
    time.sleep(1.5)
    print("Story: You decided to go on a trip this weekend!\nSo you decided to go to mountains\nEverything was good untill this happen!!")
    choices = ["woods" , "road" , "tree"]
    time.sleep(2)
    user = input("You are given 3 choices(woods,road,tree)\nselect carefully: ")
    enemy = random.choice(choices)

    if enemy == user and enemy == "woods":
        time.sleep(1)
        print("LOL, You were eaten by bears....but they didn't like your taste\nEWWWWWWW")
        lose += 1

    elif enemy == user  and enemy == "road":
        time.sleep(0.5)
        print("I think you should cross the road carefully")
        time.sleep(1)
        print("You are dead! LOL")
        lose += 1

    elif enemy == user  and enemy == "tree":
        time.sleep(2)
        print("There were snakes too my boy")
        lose += 1

    else:
        print("Oh you survived this")
        time.sleep(3)
        print("This game is under dev come months later :)")

elif user == enemy:
    time.sleep(0.9)
    print("Oh ! You were caught !")
    lose += 1
    time.sleep(1)
    print("Next round coming up!")

else:
    print("You didn't type what was written")

