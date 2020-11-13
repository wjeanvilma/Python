import random

words = ["variable", "pineapple", "beautiful"]

chosen_word = random.choice(words)
chosen_word_length = len(chosen_word)
count = chosen_word_length + 2

dash_word = []
for i in range(len(chosen_word)):
     dash_word.append("-")
print(''.join(dash_word))

while "-" in dash_word:
    if count == 0:
        print("You lost")
        break
    else:
        guess_letter = input("Guess a letter: ").lower()
        for position in range(chosen_word_length):
            letter = chosen_word[position]
            if letter == guess_letter:
                dash_word[position] = letter
    count-=1
    print(f"{''.join(dash_word)} \nYou have {count} chances remaining")

if count > 0:
    print("".join(dash_word))
    print("You win")

