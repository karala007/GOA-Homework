
password = "Da.20.04.2006.to"

while True:
    password_guess = input("password: ")
    if password_guess == password:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong password, try again.")