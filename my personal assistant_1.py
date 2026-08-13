#Making my own personal assistant
import random
history = []
print("="* 15)
print("MY PYTHON ASSISTANT")
print("="* 15)
def tasks():
    print('''
    1. Add a note
    2. View notes
    3. Calculator
    4. Random Number
    5. Exit
    ''')
    user_choice = int(input("Enter the task you want assistant to do: "))
    
    if user_choice == 1:
        add_a_note()
    elif user_choice == 2:
        view_notes()
    elif user_choice == 3:
        calculator()
    elif user_choice == 4:
        random_number()
    else:
        print("Thanks for using the assistant . Hope your day will be good!!")

def add_a_note():
    user_response = input("Enter your note : ")
    history.append(user_response)
    print("Note saved successfully")
    tasks()

def view_notes():
    print("Your saved notes are:")
    print(history)
    tasks()

def calculator():
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number : "))
    operations = input("Enter the operation: ")
    if operations == "+":
        Total = Num1 + Num2
        print(Total)
        Total = 0
        
    elif operations == "-":
        if Num1 > Num2:
            Total = Num1 - Num2
            print(Total)
            Total = 0
        elif Num2 > Num1:
            Total = Num2 - Num1
            print(Total)
            Total = 0

    elif operations == "*":
        Total = Num1 * Num2
        print(Total)
        Total = 0

    elif operations == "/":
        if Num2 != 0 and Num1 != 0:
            Total = Num1 / Num2
            print(Total)
            Total = 0
        else:
            print("You stupid or what?")
            calculator()
    else:
        print("You selected wrong operations.....Operations are only(+,-,*,/)")
        calculator()
    user_response = bool(input("Press Enter if you want to calculate more:"))
    if user_response == False:
        calculator()
    else:
        tasks()

def random_number():
    computer = random.randint(1,100000000)
    print(computer)
    tasks()

tasks()    