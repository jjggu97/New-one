import random

# select player`s choice
my_choice = input("Select rock, paper, scissor :")
print("Your Choice is..." + my_choice)

choices = ["rock","paper","scissor"]

# select computer`s choice
computer_choice = random.choice(choices)
print("Computer`s Choice is..."+computer_choice)

# rock, paper, scissor!
if my_choice == computer_choice:
    print("Draw!")
elif(my_choice == "rock" and computer_choice == "scissor") or (my_choice == "paper" and computer_choice == "rock") or (my_choice == "scissor" and computer_choice == "paper"):
    print("You Win!")
else:
    print("You lose...")


# previous code