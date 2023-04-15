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

def determine_winner(user_input, cpu_input, win_logic):
  # This secion checks the logic of the entire program as follows:
  # If the user and the computer chose the same option, the game is a tie.
  # If the computers option is a value within the key of the users option, the user wins
  # Otherwise the computer wins.
  if user_input == cpu_input:
    msg_winner = "The game is a tie!"
    winner = "There is no winner"
  elif cpu_input in win_logic[user_input]:
    winner = "You win!"
    msg_winner = win_logic[user_input][cpu_input]
  else:
    winner = "The cpu wins!"
    msg_winner = win_logic[cpu_input][user_input]
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

def rpsls_game():
  # Main Program
  pos_options = ["rock", "paper", "scissors", "lizard", "spock"]
  
  # This nested dictionary contains each game option as a key, followed by each win condition as a nested key and the value being the win message.
  win_logic = {
    "rock": {"scissors": "Rock crushes Scissors", "lizard": "Rock crushes Lizard"},
    "paper": {"rock": "Paper covers Rock", "spock": "Paper disproves Spock"},
    "scissors": {"paper": "Scissors cuts Paper", "lizard": "Scissors decapitates Lizard"},
    "lizard": {"paper": "Lizard eats Paper", "spock": "Lizard poisons Spock"},
    "spock": {"scissors": "Spock smashes Scissors", "rock": "Spock vaporises Rock"},
  }

  while True:
    user_choice = collect_input(pos_options)
    cpu_choice = random_selector(pos_options)
    msg_win, winner = determine_winner(user_choice, cpu_choice, win_logic)
    print_winner(user_choice, cpu_choice, msg_win, winner)
    play_again = replay_game() 
    if play_again in ("n", "no"):
      print("Thank you for playing!")
      break

rpsls_game()
