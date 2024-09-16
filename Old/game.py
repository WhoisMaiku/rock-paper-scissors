import random 

def collect_input():
  # Collect & Validate user input
  while True:
    user_choice = input("Please select rock, paper, or scissors: ")
    if user_choice.lower() not in ("rock", "paper", "scissors"):
      print("Error: Please enter a valid option")
    else:
      break
  return user_choice

def random_selector(choice1, choice2, choice3):
  # Select the computer's choice from three possible options
  possible_options = [choice1, choice2, choice3]
  cpu_choice = random.choice(possible_options)
  return cpu_choice

def determine_winner(user_input, cpu_input):
  # Determine who the winner is
  print("You have chosen "+ user_input + " and the cpu has chosen " + cpu_input)
  if user_input == cpu_input:
    print("There is no winner, the game is a tie!")
  elif user_input.lower() == "rock":
    if cpu_input == "paper":
      print("Paper covers rock. The cpu wins!")
    else:
      print("Rock crushes scissors. You win!")
  elif user_input.lower() == "paper":
    if cpu_input == "scissors":
      print("Scissors cuts paper. The cpu wins!")
    else:
      print("Paper covers rock. You win!")
  elif user_input.lower() == "scissors":
    if cpu_input == "rock":
      print("Rock crushes scissors. The cpu wins!")
    else:
      print("Scissors cuts paper. You win!")

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
    user_choice = collect_input()
    cpu_choice = random_selector("rock", "paper", "scissors")
    determine_winner(user_choice, cpu_choice)
    play_again = replay_game() 
    if play_again.lower() == "y":
      continue
    else:
      print("Thank you for playing!")
      break

game()
