import random

# roll the dice and display the result
def dice_roll():
    """
    Simulate rolling a six-sided dice and return the result (1-6).
    """
    value = random.randint(1, 6)
    print(f"You rolled a {value}.")
    return value

# check for snakes or ladders and return the new position
def snake_ladder_check(position):
    """
    Check if the position is at the base of a ladder or the head of a snake.
    Return the new position and a message if a snake or ladder is encountered.
    """
    ladders = {
        4: 14, 9: 31, 20: 38, 28: 84,
        40: 59, 51: 67, 63: 81, 71: 91
    }
    snakes = {
        17: 7, 54: 34, 62: 19, 64: 60,
        87: 24, 93: 73, 95: 75, 99: 78
    }
    if position in ladders:
        print(f"Ladder! Climb up from {position} to {ladders[position]}.")
        return ladders[position]
    elif position in snakes:
        print(f"Snake! Slide down from {position} to {snakes[position]}.")
        return snakes[position]
    else:
        return position

# get the new position after a dice roll
def get_position(player, current_pos, dice_value):
    """
    Calculate the new position for the player after rolling the dice.
    If the move exceeds 100, bounce back by the extra amount.
    """
    next_pos = current_pos + dice_value
    if next_pos > 100:
        # Bounce back if overshooting the 100th position
        bounce = next_pos - 100
        next_pos = 100 - bounce
        print(f"{player} needs exact roll to finish. Bounced back to {next_pos}.")
    return next_pos

# display function for the current board status of all players
def display_board_status(players_dict):
    """
    Display the current positions of all players.
    """
    print("\nCurrent Board Status:")
    for player, pos in players_dict.items():
        print(f"  {player}: {pos}")
    print()

# Main game loop structure for each player
def play_game():
    """
    Main function to play the Snakes and Ladders game.
    Handles player registration, turn management, and win condition.
    """
    print("""
========================================
  Welcome to Snakes and Ladders!
========================================
Game Rules:
- 2 to 4 players, each with a custom name
- First to reach exactly 100 wins
- Ladders help you climb up, snakes bring you down
- Roll the dice (1-6) each turn
- Bounce back if you overshoot 100
- Enjoy the game!
========================================
""")
    # Player registration and name input
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    players_dict = {}
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i+1}: ").strip()
            if not name:
                print("Name cannot be empty. Try again.")
            elif name in players_dict:
                print("Name already taken. Choose a different name.")
            else:
                players_dict[name] = 0
                break
    print("\nPlayers:")
    for player in players_dict:
        print(f"- {player}")
    print()
    # Game looping structure for each player
    winner = None
    while not winner:
        for player in players_dict:
            input(f"{player}'s turn. Press Enter to roll the dice...")
            dice_value = dice_roll()
            current_pos = players_dict[player]
            print(f"{player} is at position {current_pos}.")
            new_pos = get_position(player, current_pos, dice_value)
            # Check for snakes or ladder
            final_pos = snake_ladder_check(new_pos)
            players_dict[player] = final_pos
            print(f"{player} moved to position {final_pos}.")
            display_board_status(players_dict)
            if final_pos == 100:
                winner = player
                break
    print(f"\n🎉 Congratulations, {winner} wins the game! 🎉\n")
    print("Final Positions:")
    for player, pos in players_dict.items():
        print(f"  {player}: {pos}")

# Run the game if this script is executed directly
if __name__ == "__main__":
    play_game() 