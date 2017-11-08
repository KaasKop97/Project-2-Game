# This file will load all the games in the ../games directory.
import os


class GameLoadHandler:
    loaded_game = None

    def __init__(self):
        self.games_path = os.path.join(os.getcwd(), "games/")
        self.games_in_path = os.listdir(self.games_path)
        # Gets the game directory ^ and below here checks if it exists if not raise IOError
        if not os.path.exists(self.games_path):
            raise IOError

    def load_game(self, game_name):
        # This will load a specific game from the games directory.
        if game_name in self.games_in_path:
            # I could make it that every game should have an python file that corresponds to their game name and
            # that we then execute that which then in turn draws onto the main pygame window
            game_dir = os.path.join(self.games_path, game_name)
        else:
            print("Game does not exist nigge")

    def unload_game(self):
        # This unloads the current running game

        # This will revert the game back to the original while loop which is the main menu
        print(self.games_path)

