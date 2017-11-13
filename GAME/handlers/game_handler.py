import os
from games.clicker import clicker
from games.memes import memes
from helpers import log_helper


class GameLoadHandler:
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
            if game_name == "clicker":
                self.game = clicker.Clicker()
            elif game_name == "memes":
                self.game = memes.Memes()
        else:
            print("Game does not exist nigge")
        self.game.main(surface)

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

    # def mousemotion(self, event):
    #     try:
    #         self.game.mousemotion(event)
    #     except AttributeError as e:
    #         self.log.write_log("ERROR", "mousemotion error: " + str(e))

    def unload_game(self):
        # This unloads the current running game
        print("Unload game ayy?")
        # This will revert the game back to the original while loop which is the main menu

