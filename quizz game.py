# Creating another quiz game but this time with functions
import time
import random
Score = 0
answer = 0
def main_screen():
    print('''
    1. Play game
    2. Exit
    ''')
    user_choice = int(input("Enter your choice : "))

    if user_choice == 1 :
        print("Let's start the game")
        time.sleep(5)
        questions  = [first_question,second_question,third_question]
        random.shuffle(questions)
        return questions
        
    else:
        print("Thanks for playing")
        return []

def first_question():
    print("What is the capital of India:\n 1. New Delhi \n 2. Kolkata \n 3. Mumbai \n 4. Bangalore")
    answer = 1
    user_answer = int(input("Enter your answer: "))
    if user_answer == answer:
        print("Correct answer!")
        return 1
        
        
    else :
        print("Wrong answer")
        return 0



def second_question():
    print("What is 79 + 35\n1. 130 \n2. 119 \n3. 114 \n4.116")
    answer = 3
    user_answer = int(input("Enter your answer : "))
    if user_answer == answer:
        
        print("Correct answer!")
        time.sleep(5)
        return 1
    else:
        print("Wrong answer")
        time.sleep(6)
        return 0


def third_question():
    print("Who discovered the gravity? \n1. Einstein \n2. Heisenberg \n3. Maxwell \n4. Newton")
    answer = 4
    user_answer = int(input("Enter  your answer : "))
    if user_answer == answer:
        print("Correct answer!")
        time.sleep(5)
        return 1
    else:
        print("Wrong answer")
        time.sleep(6)
        return 0

questions = main_screen()

for question in questions:
    Score += question()

print(f"Your final score is: {Score}/{len(questions)}")