import random

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 100)
print("A number between 1 and 100 is generated\nTry to guess it",)

while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess > random_integer:
        print("Your guess is too high")
    elif user_guess < random_integer:
        print("Your guess is too low")
    else:
        break

print("Congratulations, you have finally guessed the number")
