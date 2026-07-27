# In this i have made an ATM simulator which logins with a pin , check balance , deposit money , withdraw money
import time
pin = 12503

balance = 5000


user_pin = int(input("Enter the pin: "))

if user_pin == pin:
    print("Access granted")
    time.sleep(1)
    print(f"Available balance = {balance}")

    withdraw = bool(input("Type any key if you want to withdraw the money: "))
    if withdraw == True:
        user_withdrewel_amount = int(input("How much money do you want to withdrew: "))

        if user_withdrewel_amount <= balance:
            print("Money withdrawn successfully")
            balance -= user_withdrewel_amount

        else:
            print("Insufficient balance")

    else:
        print("Ok, so no withdrawn!!")

    deposit = int(input("How much money do you want to deposit: "))
    balance += deposit
    print(f"Balance left: {balance}")

else:
    print("Your pin was incorrect")
    