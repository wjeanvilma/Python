import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#seed = int(input("Enter a seed number: "))
#random.seed(seed)

choices = [rock, paper, scissors]
random_num = random.randint(0, 2)
computer_choice = random_num
if random_num == 0:
  chosen_name = "rock"
elif random_num == 1:
  chosen_name = "paper"
else:
  chosen_name = "scissors"

#get user's choice
your_choice = int(input("Enter 0 for rock, 1 for paper, or 2 for scissors:\n"))

print(f"The computer's choice:  {chosen_name} \n {choices[random_num]}")

print(f"Your choice: \n {choices[your_choice]}")

if your_choice >= 3 or your_choice < 0:
    print("Invalid number")
elif your_choice == 0 and computer_choice == 2:
    print("You win")
elif your_choice == 2 and computer_choice == 0:
    print("You lose")
elif computer_choice == your_choice:
    print("It's a draw")
elif computer_choice > your_choice:
    print('You lost')
elif computer_choice < your_choice:
    print('You win')

# Another way that it could be done
# Checking possible cases
# if your_choice==random_num:
#   print("It's a draw")
#
# elif random_num==0:
#   if your_choice == 1:
#     print("You win")
#   else:
#     print('You lost')
#
# elif random_num == 1:
#   if your_choice == 0:
#     print("You lost")
#   else:
#     print('You win')
#
# else:
#   if your_choice == 0:
#     print("You win")
#   else:
#     print('You lost')
