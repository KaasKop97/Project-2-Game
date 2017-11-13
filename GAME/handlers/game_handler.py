import os
from games.DRON import DRON
from games.memes import memes
from helpers import log_helper


class GameHandler:
    def __init__(self):
        self.games_path = os.path.join(os.getcwd(), "games/")
        self.games_in_path = os.listdir(self.games_path)
        self.loaded_game = None
        self.game = None
        self.surface = None
        self.log = log_helper.LogHelper()

        if not os.path.exists(self.games_path):
            raise IOError

    def load_game(self, game_name, surface):
        # This will load a specific game from the games directory
        self.surface = surface
        if game_name in self.games_in_path and not None:
            self.loaded_game = game_name
            self.log.write_log("INFO", "GAME: " + self.loaded_game + " loaded.")
            if game_name == "DRON":
                self.game = DRON.Dron()
            elif game_name == "memes":
                self.game = memes.Memes()
        else:
            print("Game does not exist nigge")

    def main_loop(self):
        self.game.update(self.surface)

    def mousebutton_down(self, event):
        try:
            self.game.mousebutton_down(self.surface, event)
        except AttributeError as e:
            self.log.write_log("ERROR", "mousebutton_down error: " + str(e))

    def mousebutton_up(self, event):
        try:
            self.game.mousebutton_up(self.surface, event)
        except AttributeError as e:
            self.log.write_log("ERROR", "mousebutton_up error: " + str(e))

    def key_input(self, event):
        try:
            self.game.key_input(self.surface, event)
        except AttributeError as e:
            self.log.write_log("ERROR", "key_input error: " + str(e))

    # def mousemotion(self, event):
    #     try:
    #         self.game.mousemotion(event)
    #     except AttributeError as e:
    #         self.log.write_log("ERROR", "mousemotion error: " + str(e))

    def unload_game(self):
        # This unloads the current running game
        print("Unload game ayy?")
        # This will revert the game back to the original while loop which is the main menu
        self.loaded_game = None
