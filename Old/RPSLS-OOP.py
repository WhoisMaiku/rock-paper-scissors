import random
import os
    
class Game:

    def __init__(self, options = [], win_conditions = {}):
        self.options = options
        self.win_conditions = win_conditions
    
    def generate_options_list(self):
        # Generates a new list of game options from scratch
        print("Please write down the possible options you would like to add to the game:")
        print("Type 'end' when complete")
        while True:
            new_option = input().lower()
            if new_option == "end":
                break
            else:
                self.add_option(new_option)
    
    def generate_win_conditions(self):
        # Generates win conditions for a list of game options
        for val in range(len(self.options)):
            while True:
                os.system("clear")
                print(f"What does {self.options[val]} beat?")
                loser = input().lower()
                print(f"Please enter the win message for when {self.options[val]} beats {loser}:")
                win_message = input().lower()
                self.add_win_condition(self.options[val], loser, win_message)
                print(f"Does {self.options[val]} beat anything else? [Y/N]")
                add_more = input().lower()
                if add_more in ("n", "no"):
                    break

    def add_option(self, option):
        # Add a new option to the game
        self.options.append(option)

    def del_option(self, option):
        # Delete an existing option from the game
        self.options.remove(option)

    def add_win_condition(self, winner, loser, message):
        # Adds a new win condition. If the option does not already exist it will add it.
        if winner in self.win_conditions and winner in self.options:
            self.win_conditions[str(winner)][str(loser)] = message 
        elif winner in self.options:
            self.win_conditions[str(winner)] = {str(loser): message}
        else:
            self.add_option(winner)
            self.win_conditions[str(winner)] = {str(loser): message}  

    def del_win_condition(self, winner):
        # Deletes a win condition from the win logic map
        del self.win_conditions[winner]
    
    def collect_input(self):
        # Collect & Validate user input via text input.
        while True:
            print("Please select one of the following options: " + ", ".join(self.options))
            self.user_choice = input().lower()
            if self.user_choice not in (self.options):
                print("Error: Please enter a valid option")
            else:
                return self.user_choice
    
    def random_selector(self):
        # Select the computer's choice from predetermined possible options
        self.cpu_choice = random.choice(self.options)
        return self.cpu_choice

    def determine_winner(self):
        # This secion checks the logic of the entire program as follows:
        # If the user and the computer chose the same option, the game is a tie.
        # If the computers option is a value within the key of the users option, the user wins
        # Otherwise the computer wins.
        if self.user_choice == self.cpu_choice:
            self.win_msg = "The game is a tie!"
            self.winner = "There is no winner"
        elif self.cpu_choice in self.win_conditions[self.user_choice]:
            self.win_msg = self.win_conditions[self.user_choice][self.cpu_choice]
            self.winner = "You win!"
        else:
            self.win_msg = self.win_conditions[self.cpu_choice][self.user_choice]
            self.winner = "The cpu wins!"
        return self.win_msg, self.winner
       
    def print_winner(self):
        # Print the outcome of the game
        os.system("clear")
        print("You have chosen", self.user_choice, "and the cpu has chosen", self.cpu_choice)
        print(self.win_msg)
        print(self.winner)
    
    def replay_game(self):
        # This function is responsible for determining if the user would like to play again.
        while True:
            self.play_again = input("Do you want to play again? Enter Y/N: ").lower()
            if self.play_again not in ("y", "n", "yes", "no"):
                print("Please select a valid option.")
            else:
                return self.play_again

    def play_game(self):
        while True:
            os.system("clear")
            self.collect_input()
            self.random_selector()
            self.determine_winner()
            self.print_winner()
            self.replay_game()
            if self.play_again in ("n", "no"):
                print("Thank you for playing!")
                break

# Inputs for a simple Rock Paper Scissors Game
rps_options = ["rock", "paper", "scissors"]

win_logic = {
    "rock": {"scissors": "Rock crushes Scissors"},
    "paper": {"rock": "Paper covers Rock"},
    "scissors": {"paper": "Scissors cuts Paper"},
}

# Creates RPS game objects
rps = Game(rps_options, win_logic)

# Using the methods defined to update the RPS dictionary to play RPSLS - Can comment out if you just want to play RPS
rps.add_win_condition("rock", "lizard", "Rock crushes Lizard")
rps.add_win_condition("paper", "spock", "Paper disproves Spock")
rps.add_win_condition("scissors", "lizard", "Scissors decapitates Lizard")
rps.add_win_condition("lizard", "paper", "Lizard eats Paper")
rps.add_win_condition("lizard", "spock", "Lizard poisons Spock")
rps.add_win_condition("spock", "scissors", "Spock smashes Scissors")
rps.add_win_condition("spock", "rock", "Spock vaporises Rock")

# Playing RPSLS using the original RPS object
rps.play_game()
