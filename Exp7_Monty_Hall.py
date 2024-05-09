import random

def monty_hall_simulate(strategy='stay', num_trials=1000):
    """
    Simulate the Monty Hall problem.

    Parameters:
    - strategy (str): Strategy to use, either 'stay' or 'switch'.
    - num_trials (int): Number of trials to run.

    Returns:
    - win_count (int): Number of wins.
    - lose_count (int): Number of losses.
    """
    win_count = 0
    lose_count = 0

    for _ in range(num_trials):
        # Place the prize behind a random door
        prize_door = random.randint(1, 3)

        # Contestant selects a door
        contestant_choice = random.randint(1, 3)

        # Monty opens a door that doesn't have the prize and isn't the contestant's choice
        possible_open_doors = [door for door in range(1, 4) if door != prize_door and door != contestant_choice]
        monty_open_door = random.choice(possible_open_doors)

        # Determine the other door the contestant could switch to
        remaining_doors = [door for door in range(1, 4) if door != contestant_choice and door != monty_open_door]
        if strategy == 'switch':
            contestant_choice = remaining_doors[0]

        # Check if the contestant wins
        if contestant_choice == prize_door:
            win_count += 1
        else:
            lose_count += 1

    return win_count, lose_count

# Run the simulation
stay_wins, stay_losses = monty_hall_simulate(strategy='stay', num_trials=10000)
switch_wins, switch_losses = monty_hall_simulate(strategy='switch', num_trials=10000)

# Print results
print("Results for 'stay' strategy:")
print("Wins:", stay_wins)
print("Losses:", stay_losses)
print("Winning percentage:", (stay_wins / (stay_wins + stay_losses)) * 100, "%")

print("\nResults for 'switch' strategy:")
print("Wins:", switch_wins)
print("Losses:", switch_losses)
print("Winning percentage:", (switch_wins / (switch_wins + switch_losses)) * 100, "%")
