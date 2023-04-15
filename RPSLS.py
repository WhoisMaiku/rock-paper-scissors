import random

def collect_input(pos_choice):
  # Collect & Validate user input via text input from a predetermined list.
  while True:
    print("Please select one of the following options: " + ", ".join(pos_choice))
    user_choice = input().lower()
    if user_choice not in (pos_choice):
      print("Error: Please enter a valid option")
    else:
      return user_choice

def random_selector(pos_options):
  # Select the computer's choice from predetermined possible options
  return random.choice(pos_options)

def determine_winner(user_input, cpu_input):
  # Dictionary containing the winning conditions within the first value pair, followed by the win messages in the second value pair
  win_logic = {
    "rock": (("scissors", "lizard"), ("Rock crushes Scissors", "Rock crushes Lizard")),
    "paper": (("rock", "spock"), ("Paper covers Rock", "Paper disproves Spock")),
    "scissors": (("paper", "lizard"), ("Scissors cuts Paper", "Scissors decapitates Lizard")),
    "lizard": (("paper", "spock"), ("Lizard eats Paper", "Lizard poisons Spock")),
    "spock": (("scissors", "rock"), ("Spock smashes Scissors", "Spock vaporises Rock")),
    "tie": ("The game is a tie!"),
  }

  # This secion checks the logic of the entire program as follows:
  # If the user and the computer chose the same option, the game is a tie.
  # If the computers option is a value within the first value pair of the key for the players option, then the player wins.
  # Otherwise the computer wins.
  if user_input == cpu_input:
    msg_winner = win_logic["tie"]
    winner = "There is no winner"
  elif cpu_input in win_logic[user_input][0]:
    if cpu_input == win_logic[user_input][0][0]:
      msg_winner = win_logic[user_input][1][0]
    else:
      msg_winner = win_logic[user_input][1][1]
    winner = "You win!"
  else:
    if user_input == win_logic[cpu_input][0][0]:
      msg_winner = win_logic[cpu_input][1][0]
    else:
      msg_winner = win_logic[cpu_input][1][1]
    winner = "The cpu wins!"
  return msg_winner, winner
    
def print_winner(user_choice, cpu_choice, win_msg, winner):
  # Print the outcome of the game
  print("You have chosen", user_choice, "and the cpu has chosen", cpu_choice)
  print(win_msg)
  print(winner)

def replay_game():
  # This function is responsible for determining if the user would like to play again.
  while True:
    play_again = input("Do you want to play again? Enter Y/N: ").lower()
    if play_again not in ("y", "n", "yes", "no"):
      print("Please select a valid option.")
    else:
      return play_again

def game():
  # Main Program
  pos_options = ["rock", "paper", "scissors", "lizard", "spock"]

  while True:
    user_choice = collect_input(pos_options)
    cpu_choice = random_selector(pos_options)
    msg_win, winner = determine_winner(user_choice, cpu_choice)
    print_winner(user_choice, cpu_choice, msg_win, winner)
    play_again = replay_game() 
    if play_again in ("n", "no"):
      print("Thank you for playing!")
      break

game()
