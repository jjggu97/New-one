import random
import matplotlib.pyplot as plt

def play_game():
    choices = ["rock", "paper", "scissor"]
    my_wins = 0
    computer_wins = 0

    while my_wins < 2 and computer_wins < 2:
        my_choice = random.choice(choices)
        computer_choice = random.choice(choices)

        if my_choice == computer_choice:
            continue  # 비겼을 경우 다시 시도

        if (my_choice == "rock" and computer_choice == "scissor") or \
           (my_choice == "paper" and computer_choice == "rock") or \
           (my_choice == "scissor" and computer_choice == "paper"):
            my_wins += 1
        else:
            computer_wins += 1

    if my_wins == 2:
        return 'win'
    else:
        return 'lose'

def simulate_and_plot(num_simulations):
    win_count = 0
    results = {'win': 0, 'lose': 0}

    for _ in range(num_simulations):
        result = play_game()
        results[result] += 1
        if result == 'win':
            win_count += 1

    win_probability = win_count / num_simulations

    # Visualization using a bar chart
    labels = list(results.keys())
    values = list(results.values())

    plt.bar(labels, values, color=['green', 'red'])
    plt.title(f"Win Probability after {num_simulations} Simulations: {win_probability:.2%}")
    plt.show()

# Adjust the number of simulations and call the function
simulate_and_plot(num_simulations=1000)
