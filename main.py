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
Rock_Paper_Scissor = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
if choice>=3 or choice<0:
  print("You entered invalid option.")
else:
  print(Rock_Paper_Scissor[choice])
  comp_choice = random.randint(0, 2)
  print("Computer chose:")
  print(Rock_Paper_Scissor[comp_choice])
  if choice==0 and comp_choice==2:
    print("You win")
  elif choice==2 and comp_choice==0:
    print("You lose.")
  elif comp_choice>choice:
    print("You lose")
  elif choice>comp_choice:
    print("You win")
  elif choice==comp_choice:
    print("Draw!")