var = int(input("Enter the integer for the player to guess.\n"))

count = 4
guess = int(input("Enter your guess.\n"))

while (True):
    count = count

    if (guess > var):
        guess = int(input("Too high - try again:\n"))
        continue
    elif (guess < var):
        guess = int(input("Too low - try again:\n"))
        continue
    else:
        break

print("You guessed it in", count, "tries.")

