guess = 1

while True:
    num = input("Please guess the number (between 0-100): ")
    try:
        num = int(num)
    except:
        print("Invalid number, please guess again.")
        continue

    if num < 45:
        print("your guess was under")
    elif num > 45:
        print("your guess was over")
    else:
        break

    guess += 1

print(f"you guessed it in {guess} guesses")