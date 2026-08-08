import random
print("================================")
print("       NUMBER GUESSING GAME")
print("================================")
number = random.randint(1, 100)
attempts = 0
while True:
    try:
        guess = int(input("\nGuess a number between 1 and 100: "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("\n🎉 Congratulations!")
            print("You guessed the correct number.")
            print("Number of attempts:", attempts)
            break
    except ValueError:
        print("Invalid input! Please enter a number.")

print("\nThanks for playing!")