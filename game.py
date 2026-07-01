"""
Snake and Ladder Game
A simple console-based implementation for 2 or more players.
"""

import random

# Board size
BOARD_SIZE = 100

# Snakes: position of snake's head -> position of snake's tail (moves player DOWN)
SNAKES = {
    99: 54,
    95: 42,
    92: 88,
    87: 24,
    64: 60,
    62: 19,
    56: 53,
    49: 11,
    48: 26,
    16: 6,
}

# Ladders: position of ladder's bottom -> position of ladder's top (moves player UP)
LADDERS = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
}


def roll_dice():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)


def get_players():
    """Ask the user for number of players and their names."""
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")

    players = {}
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ").strip()
        if not name:
            name = f"Player {i}"
        players[name] = 0
    return players


def move_player(position, dice_value):
    """Calculate new position after a dice roll, applying snakes/ladders."""
    new_position = position + dice_value

    if new_position > BOARD_SIZE:
        # Must land exactly on 100, otherwise stay in place
        return position, "overshoot"

    event = None
    if new_position in SNAKES:
        bitten_from = new_position
        new_position = SNAKES[new_position]
        event = f"Oh no! Bitten by a snake at {bitten_from}. Slide down to {new_position}."
    elif new_position in LADDERS:
        climbed_from = new_position
        new_position = LADDERS[new_position]
        event = f"Yay! Climbed a ladder at {climbed_from}. Jump up to {new_position}."

    return new_position, event


def print_board_positions(players):
    """Print current positions of all players."""
    print("\n--- Current Positions ---")
    for name, pos in players.items():
        print(f"{name}: {pos}")
    print("--------------------------\n")


def play_game():
    print("=" * 40)
    print("      WELCOME TO SNAKE AND LADDER")
    print("=" * 40)

    players = get_players()
    player_names = list(players.keys())
    winner = None

    turn_index = 0
    while not winner:
        current_player = player_names[turn_index]
        input(f"{current_player}'s turn. Press Enter to roll the dice...")

        dice_value = roll_dice()
        print(f"{current_player} rolled a {dice_value}.")

        current_position = players[current_player]
        new_position, event = move_player(current_position, dice_value)

        if event == "overshoot":
            print(f"{current_player} needs exact count to reach 100. Staying at {current_position}.")
        else:
            players[current_player] = new_position
            print(f"{current_player} moves to {new_position}.")
            if event:
                print(event)

        print_board_positions(players)

        if players[current_player] == BOARD_SIZE:
            winner = current_player
            break

        # Extra turn on rolling a 6
        if dice_value != 6:
            turn_index = (turn_index + 1) % len(player_names)

    print("=" * 40)
    print(f"🎉 {winner} wins the game! Congratulations! 🎉")
    print("=" * 40)


if __name__ == "__main__":
    play_game()
