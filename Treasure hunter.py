# I am going to hide few things in 5x5 grid
import random
import time
pstn = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]
en1 = random.choice(pstn)
en2 = random.choice(pstn)
en3 = random.choice(pstn)
en4 = random.choice(pstn)
en5 = random.choice(pstn)
en6 = random.choice(pstn)
en7 = random.choice(pstn)
enemy = [en1,en2,en3,en4,en5,en6,en7]
t1 = random.choice(pstn)
t2 = random.choice(pstn)
t3 = random.choice(pstn)
treasure = [t1,t2,t3]
enemy != treasure
treasure_collected = 0
attempts = 10
time.sleep(0.8)
print("There is a 5x5 grid in this game where 3 treasurses are hidden")
time.sleep(4)
print("You only have 10 attempts and you have to collect all the treasures to win ")
print("Sound's easy!!!")
time.sleep(10)
print("But there are watchers of this palace who will not spare you if you get caught")
time.sleep(8)
print("Let's start the game")
time.sleep(3)
print("I forgot to give you the map!\n Remeber there are 7 enemies")
time.sleep(11)
print('''
A1 | B1 | C1 | D1 | E1
___|____|____|____|___
A2 | B2 | C2 | D2 | E2
___|____|____|____|___
A3 | B3 | C3 | D3 | E3
___|____|____|____|___
A4 | B4 | C4 | D4 | E4
___|____|____|____|___
A5 | B5 | C5 | D5 | E5

This is your map!!
''')
time.sleep(20)
allowment = input("Are you ready to start the game(Y/N): ")
while allowment == "Y":
    print("Let's start the game")
    time.sleep(1)
    
    while attempts > 0:
        user_choice = input("Select the place : ")
        if user_choice in treasure and user_choice in enemy:
           print("Oh you got the treasure but guard was also there")
           treasure_collected += 1
           attempts -= 1
        elif user_choice in treasure :
           treasure_collected += 1
           if treasure_collected == 3:
               print(f"Yay! You won the challenge in {attempts} attempts left")

           else:
               print("Yay! You got one")
               attempts -= 1

        elif user_choice in enemy:
          attempts -=1
          print("You got caught")

        else:
         attempts -= 1

    else:
       print("Oh your all attempts are over")
       break

else:
    print("Thanks for playing")