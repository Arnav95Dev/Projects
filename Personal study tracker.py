# Creating a personal study tracker
print("="*10)
print("The Personal Study Tracker")
print("="*10)
def main_screen():
    print('''
         1. Add Study Session
         2. View all study session's
         3. Calculate total Study Time
         4. Search Subject
         5. Exit
    ''')
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        add_study_session()
    elif user_choice == 2:
        view_all_study_sessions()
    elif user_choice == 3:
        calculate_total_study_time()
    elif user_choice == 4:
        search_subject()
    elif user_choice == 5:
        print("Thanks for using this :)")
    else:
        print("You have not selected the right choice")
        print("Please enter the right choice")
        main_screen()

def add_study_session():   
    sub = input("Enter the subject : ")
    topic = input("Enter the topic of the subject : ")
    time = int(input("Allot the time for the topic in minutes: "))
    subject.append(sub)
    Topic.append(topic)
    Time.append(time)
    print("Do you want to add another study session?")
    print('''
    1. Add another study session
    2. Main screen
    ''')
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        add_study_session()
    else:
        main_screen()

def view_all_study_sessions():
    print("Let me show you your today sessions")
    if len(subject) == 0:
        print("You have not added anything in the tracker currently")
        print("Please add something:")
        main_screen()
    else:
        for i in range(len(subject)):
                print(f"{subject[i]}   ||  {Topic[i]}   ||  {Time[i]}")

def calculate_total_study_time():
    for i in range(len(Time)):
        Total_time += Time[i]
    print(f"Your total study time is : {Total_time}")
    main_screen()

def search_subject():
    Find_subject = input("Enter the subject you want to check: ")
    for i in range(len(Time)):
        if subject[i] == Find_subject:
            print(f"{Find_subject}  ||  {Topic[i]}   ||    {Time[i]}")
            main_screen()
    else:
        print("Sorry , There is no such subject in the list")
        main_screen()

subject = []
Time = []
Topic = []
Total_time = 0

main_screen()