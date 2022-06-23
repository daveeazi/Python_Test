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

#Write your code below this line 👇
import random
computer_choice = random.randint(0,2)

image = (rock, paper, scissors)

answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("Computer choice is:")
print(image[computer_choice])

if answer > 2:
  print("Sorry, you chose an invalid number, please try again! \n")
elif answer < 0:
  print("Sorry, you chose an invalid number, please try again! \n")
elif answer == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice > answer:
  print("You lose!")
elif computer_choice == answer:
  print("Draw!!!")