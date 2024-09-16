import os
from abc import ABC, abstractmethod

class GameInputStrategy(ABC):
    @abstractmethod
    def create_options_list(self):
        """Creates a list of possible game options"""

    @abstractmethod
    def create_win_logic(self):
        """Creates a dictionary format with win logic"""

class DictionaryInputStrategy(GameInputStrategy):
    # Checks if a list already exists
    def create_options_list(self, options):
        if not options:
            return print("Error: No game options present")
        else:
            return options
    
    # Checks if a dictionary already exists
    def create_win_logic(self, win_logic):
        if not win_logic:
            return print("Error: No win logic provided")
        else:
            return win_logic

class TerminalInputStrategy(GameInputStrategy):
    # Adds a new win condition. If the option does not already exist it will add it.
    def add_win_condition(self, winner, loser, message):
        if winner in self.win_conditions and winner in self.options:
            self.win_conditions[str(winner)][str(loser)] = message 
        elif winner in self.options:
            self.win_conditions[str(winner)] = {str(loser): message}
        else:
            self.options.append(winner)
            self.win_conditions[str(winner)] = {str(loser): message}
        return self.win_conditions

    def create_options_list(self, options):
        self.options = options
        # Generates a new list of game options from scratch
        print("Please write down the possible options you would like to add to the game:")
        print("Type 'end' when complete")
        while True:
            new_option = input().lower()
            if new_option == "end":
                break
            else:
                self.options.append(new_option)
        return self.options

    def create_win_logic(self, win_conditions):
        self.win_conditions = win_conditions
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
        return self.win_conditions

class TextInputStrategy(GameInputStrategy):
    def create_options_list(self, options):
        self.options = options
        with open("inputs.txt") as f:
            for line in f:
                word = line.split(None, 1)[0]
                opt = word.strip(",")
                if opt not in self.options:
                    self.options.append(opt)
        return self.options 
    
    def create_win_logic(self, win_conditions):
        self.win_conditions = win_conditions
        with open("inputs.txt") as f:
            for line in f:
                stripped = line.strip()
                (winner, loser, message) = stripped.split(", ")
                if winner in self.win_conditions:
                    self.win_conditions[str(winner)][str(loser)] = message 
                else:
                    self.win_conditions[str(winner)] = {str(loser): message}
        return self.win_conditions
    
