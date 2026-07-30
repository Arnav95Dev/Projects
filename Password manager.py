passwords = {
    "Chrome" : "arnu367",
    "Google" : "goojel378",
    "Steam" : "sbao5260"
}
def password_manager():
    password_manager_access = int(input("Enter the 6 digit PIN: "))

    if password_manager_access == 156203:
        print("You got access to password manager")
        user_choice = str(input("Which password you want to know: "))
        print(passwords[user_choice])
        user_choice = bool(input("Press ENTER if you want to add a password in password manager: "))
        if user_choice == False:
            user_choice_1 = str(input("Which password you want to save? : "))
            user_password = str(input("Save your password here: "))
            passwords[user_choice_1] = user_password
        else:
            print("Thanks !")
    else:
        print("Sorry wrong password")
        password_manager()

password_manager()