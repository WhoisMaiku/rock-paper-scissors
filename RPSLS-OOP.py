import random
    
class Game:

    def __init__(self, options = [], win_conditions = {}):
        self.options = options
        self.win_conditions = win_conditions
        self.user_choice = ""
        self.cpu_choice = ""
        self.winner = ""
        self.win_msg = ""
        self.play_again = ""
    
    def add_win_condition(self, winner, loser, message):
        # Adds an extra win condition to an already existing option
        self.win_conditions[str(winner)][str(loser)] = message 
    
    def add_new_win_condition(self, winner, loser, message):
        # Adds a new option and win condition
        self.options.append(winner)
        self.win_conditions[str(winner)] = {str(loser): message}

    def generate_options_list(self):
        # Generates a new list of game options from scratch
        print("Please write down the possible options you would like to add to the game:")
        print("Type End when complete")
        while True:
            new_option = input().lower()
            if new_option == "end":
                break
            else:
                self.options.append(new_option)

    def del_win_condition(self, winner):
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
rps.add_new_win_condition("lizard", "paper", "Lizard eats Paper")
rps.add_win_condition("lizard", "spock", "Lizard poisons Spock")
rps.add_new_win_condition("spock", "scissors", "Spock smashes Scissors")
rps.add_win_condition("spock", "rock", "Spock vaporises Rock")

# Playing RPSLS using the original RPS object
rps.play_game()
