import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100!")
level = input("Chose a level. Type 'easy' or 'hard': ").lower()
guess = int(input("Make a guess: "))

number = random.randint(1, 100)
attempts = 0
comparison = ""

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5

while number != guess:
    attempts -= 1
    if guess > number:
        comparison = "Too high"
    elif guess < number:
        comparison = "Too low"
    if attempts == 0:
        print(f"You lost. The number is: {number}")
        break

    print(f"{comparison}.\nGuess again. \nYou have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))

if number == guess:
    print("You win. Bravo")
