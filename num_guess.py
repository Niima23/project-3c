#Amiin Samatar
#niima23
#10/11/22
#Entering my guesses to see if it is too low or too high

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

