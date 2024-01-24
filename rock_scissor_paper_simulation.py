import random
import matplotlib.pyplot as plt

def play_game():
    choices = ["rock", "paper", "scissor"]
    my_choice = random.choice(choices)
    computer_choice = random.choice(choices)

    if my_choice == computer_choice:
        return 'draw'
    elif (my_choice == "rock" and computer_choice == "scissor") or \
         (my_choice == "paper" and computer_choice == "rock") or \
         (my_choice == "scissor" and computer_choice == "paper"):
        return 'win'
    else:
        return 'lose'

def visualize_win_probability_pie(num_simulations):
    wins = 0
    results = {'win': 0, 'draw': 0, 'lose': 0}

    for _ in range(num_simulations):
        result = play_game()
        results[result] += 1
        if result == 'win':
            wins += 1

    win_probability = wins / num_simulations

    # Visualization using a pie chart
    labels = list(results.keys())
    values = list(results.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Win Probability after {num_simulations} Simulations: {win_probability:.2%}")
    plt.show()

# Adjust the number of simulations and call the function
visualize_win_probability_pie(num_simulations=1000)

