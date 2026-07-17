secret_number = 27
attempts = 0

while True:
    num = int(input("Guess the number : "))
    attempts += 1

    if num == secret_number:
        print("Wow you guessed it right")
        break

    elif num > secret_number:
        print("Your number is greater than the answer")
        

    else:
        print("Your number is less than the actual answer")
        

print(f"No. of attempts: {attempts}")