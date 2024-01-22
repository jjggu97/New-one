import random

my_choice = input("Select rock, paper, scissor :")
print("Your Choice is..." + my_choice)

choices = {"rock","paper","scissor"}

computer_choice = random.choice(choices)

