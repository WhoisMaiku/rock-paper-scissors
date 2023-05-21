from game_inputs import DictionaryInputStrategy, TerminalInputStrategy, TextInputStrategy
from game_builder import BuildGame, OnlineGame

# Creates a simple RPS game using a dictionary
def build_dict_game():
  rps_options = ["rock", "paper", "scissors"]

  rps_logic = {
    "rock": {"scissors": "Rock crushes Scissors"},
    "paper": {"rock": "Paper covers Rock"},
    "scissors": {"paper": "Scissors cuts Paper"},
  }
  rps = BuildGame()
  rps.create_game_logic(DictionaryInputStrategy(), rps_options, rps_logic)
  rps.play_game()

# Creates a game from scratch using the Terminal
def build_terminal_game():
  term = BuildGame()
  term.create_game_logic(TerminalInputStrategy())
  term.play_game()

# Builds a Online dict RPSLS Game
def build_online_dict_game():
  # API Key & Database ID for Notion Integration
  NOTION_TOKEN = "secret_IFLCcxS0monkUFU8I6d0MCJeuPvhj0lelhP4aGCEgoY"
  DATABASE_ID = "0f4bcb23853444088d286837b8cf3f2a"

  # Inputs for a RPSLS Game
  pos_options = ["rock", "paper", "scissors", "lizard", "spock"]

  # This nested dictionary contains each game option as a key, followed by each win condition as a nested key and the value being the win message.
  win_logic = {
    "rock": {"scissors": "Rock crushes Scissors", "lizard": "Rock crushes Lizard"},
    "paper": {"rock": "Paper covers Rock", "spock": "Paper disproves Spock"},
    "scissors": {"paper": "Scissors cuts Paper", "lizard": "Scissors decapitates Lizard"},
    "lizard": {"paper": "Lizard eats Paper", "spock": "Lizard poisons Spock"},
    "spock": {"scissors": "Spock smashes Scissors", "rock": "Spock vaporises Rock"},
  }

  # Creates RPSLS game object
  online = OnlineGame(NOTION_TOKEN, DATABASE_ID)
  online.create_game_logic(DictionaryInputStrategy(), pos_options, win_logic)
  online.play_game()

def build_text_game():
  txt_game = BuildGame()
  txt_game.create_game_logic(TextInputStrategy())
  txt_game.play_game()

# Runs the different types of games
# build_dict_game()
# build_terminal_game()
# build_online_dict_game()
build_text_game()
