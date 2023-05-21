import random
import os 
import requests
from game_inputs import GameInputStrategy

class BuildGame:
    def __init__(self):
        self.local_player_score = 0
        self.local_cpu_score = 0
        self.player1_name = "Mike"
        self.player2_name = "CPU"

    def create_game_logic(self, game: GameInputStrategy, game_options = [], game_logic = {}):
        self.options = game.create_options_list(game_options)
        self.win_conditions = game.create_win_logic(game_logic)

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
            self.win_msg = f"The game is a tie! \n There is no winner"
            self.winner = "Tie"
        elif self.cpu_choice in self.win_conditions[self.user_choice]:
            self.win_msg = self.win_conditions[self.user_choice][self.cpu_choice] + ". You win!"
            self.winner = self.player1_name
            self.local_player_score += 1
        else:
            self.win_msg = self.win_conditions[self.cpu_choice][self.user_choice] + ". The cpu wins!"
            self.winner = self.player2_name
            self.local_cpu_score += 1
        return self.win_msg, self.winner

    def print_winner(self):
        # Print the outcome of the game
        os.system("clear")
        print(f"You have chosen {self.user_choice} and the cpu has chosen {self.cpu_choice}")
        print(self.win_msg)

    def replay_game(self):
        # This function is responsible for determining if the user would like to play again.
        while True:
            self.play_again = input("Do you want to play again? Enter Y/N: ").lower()
            if self.play_again not in ("y", "n", "yes", "no"):
                print("Please select a valid option.")
            else:
                return self.play_again

    def show_game_summary(self):
        # Provides the user with a summary of the games played in this session
        print("Thank you for playing!")
        print(f"In this session you won {self.local_player_score} times and the cpu won {self.local_cpu_score} times")   

    def play_game(self):
        # This is the main method that runs the game
        while True:
            os.system("clear")
            self.collect_input()
            self.random_selector()
            self.determine_winner()
            self.print_winner()
            self.replay_game()
            if self.play_again in ("n", "no"):
                self.show_game_summary()
                break

# A dict based input game that posts the results to a Notion database, and reads total wins & ties
class OnlineGame(BuildGame):
    # Inherits the initialisation from the super class, but also sets up the required info to communicate with Notion database
    def __init__(self, api_key, database_id):
        super().__init__()
        self.api_key = api_key
        self.database_id = database_id
        self.database_url = f"https://api.notion.com/v1/databases/{self.database_id}"
        self.headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + self.api_key,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
        }

    # Checks the HTTP status code of the database
    def get_database_status(self):
        response = requests.get(self.database_url, headers=self.headers)
        if response.status_code != 200:
            print("Error: HTTP Response Code - ", response.status_code)
            print(response.text)

    # Posts the results from the game to the Notion database.
    def post_results(self):
        pages_url = "https://api.notion.com/v1/pages"

        # Creates a new data entry in the format required to correctly integrate with the Notion Database
        new_data_entry = {
            "parent": {
                "type": "database_id",
                "database_id": self.database_id
                },
            "properties": {
                "Winner": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": self.winner,
                            },
                            "plain_text": self.winner,
                        }
                    ]
                },
                "CPU Input": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": self.cpu_choice,
                            },
                            "plain_text": self.cpu_choice,
                        }
                    ]
                },
                "User Input": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": self.user_choice,
                            },
                            "plain_text": self.user_choice,
                        }
                    ]
                }
            }
        }

        # Add the outcome of the game to the database
        res = requests.post(pages_url, headers=self.headers, json=new_data_entry)
        if res.status_code != 200:
            print("Error: HTTP Response Code - ", res.status_code)
            print(res.text)

    def get_score(self, condition):
        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"

        # Filters the Winner property in the database
        search = {
            "page_size": 100,
            "filter": {
                "property": "Winner",
                "rich_text": {
                    "contains": condition
                }
            }
        }

        # Queries the database based on the winner condition that was passed into the method.
        res = requests.post(url, json=search, headers=self.headers)
        data = res.json()
    
        # Updates the total score based on which condition was queried
        if condition == self.player1_name:
            self.player_score = len(data['results'])
        elif condition == self.player2_name:
            self.cpu_score = len(data['results'])
        else:
            self.tie_score = len(data['results'])

    def show_game_summary(self):
        super().show_game_summary()
        print(f"Your total wins are: {self.player_score}")
        print(f"The CPU's total wins are: {self.cpu_score}")
        print (f"There have been {self.tie_score} tied games in total.")

    def play_game(self):
        # This is the main method that runs the game
        while True:
            os.system("clear")
            self.collect_input()
            self.random_selector()
            self.determine_winner()
            self.print_winner()
            self.get_database_status()
            self.post_results()
            self.replay_game()
            if self.play_again in ("n", "no"):
                self.get_score(self.player1_name)
                self.get_score(self.player2_name)
                self.get_score("Tie")
                self.show_game_summary()
                break
