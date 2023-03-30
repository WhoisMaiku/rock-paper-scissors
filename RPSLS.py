import random

def collect_input(pos_choice1, pos_choice2, pos_choice3, pos_choice4, pos_choice5):
  # Collect & Validate user input versus 5 predetermined posibilities.
  while True:
    print("Please select one of the following options:", pos_choice1, pos_choice2, pos_choice3, pos_choice4, pos_choice5)
    user_choice = input()
    if user_choice.lower() not in (pos_choice1, pos_choice2, pos_choice3, pos_choice4, pos_choice5):
      print("Error: Please enter a valid option")
    else:
      break
  return user_choice

def random_selector(choice1, choice2, choice3, choice4, choice5):
  # Select the computer's choice from five possible options
  possible_options = [choice1, choice2, choice3, choice4, choice5]
  cpu_choice = random.choice(possible_options)
  return cpu_choice

def determine_winner(user_input, cpu_input):
  # Determine who the winner is through a dictionary search
  win_logic = {
    "rock": ("lizard", "scissors"),
    "paper": ("rock", "spock"),
    "scissors": ("paper", "lizard"),
    "lizard": ("paper", "spock"),
    "spock": ("scissors", "rock"),
  }

  # Show a custom win message through contatinating inputs together
  win_msg = {
    "rocklizard": ("Rock crushes Lizard"),
    "rockscissors": ("Rock crushes Scissors"),
    "paperrock": ("Paper covers Rock"),
    "paperspock": ("Paper disproves Spock"),
    "scissorspaper": ("Scissors cuts Paper"),
    "scissorslizard": ("Scissors decapitates Lizard"),
    "lizardpaper": ("Lizard eats Paper"),
    "lizardspock": ("Lizard poisons Spock"),
    "spockscissors": ("Spock smashes Scissors"),
    "spockrock": ("Spock vaporises Rock"),
    "tie": ("The game is a tie!"),
  }

  # This secion checks the logic of the entire program as follows:
  # If the user and the computer chose the same option, the game is a tie.
  # If the computers option is a value within the key for the players option, then the player wins.
  # Otherwise the computer wins.
  # The values are then concatinated together with the format "winning_option+losing_option" to display the correct outcome message
  if user_input == cpu_input:
    msg_display = "tie"
    winner = "There is no winner"
  elif cpu_input in win_logic[user_input]:
    msg_display = user_input + cpu_input
    winner = "You win!"
  else:
    msg_display = cpu_input + user_input
    winner = "The cpu wins!"
    
  # Print the outcome of the game
  print("You have chosen "+ user_input + " and the cpu has chosen " + cpu_input)
  print(win_msg[msg_display])
  print(winner)

def replay_game():
  while True:
    play_again = input("Do you want to play again? Enter Y/N: ")
    if play_again.lower() not in ("y", "n"):
      print("Please select a valid option.")
    else:
      break
  return play_again

def game():
  # Main Program
  while True:
    user_choice = collect_input("rock", "paper", "scissors", "lizard", "spock")
    cpu_choice = random_selector("rock", "paper", "scissors", "lizard", "spock")
    determine_winner(user_choice, cpu_choice)
    play_again = replay_game() 
    if play_again.lower() == "y":
      continue
    else:
      print("Thank you for playing!")
      break

game()
