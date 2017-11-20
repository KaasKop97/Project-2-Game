from games.DRON import DRON
from games.Zone_Trespassers import Zone_Trespassers
from helpers import log_helper


class GameHandler:
    def __init__(self):
        self.loaded_game = None
        self.game = None
        self.surface = None
        self.log = log_helper.LogHelper()
        self.DRON = DRON.Dron()
        self.ZT = Zone_Trespassers.ZoneTrespassers()

        self.game_names = [
            self.DRON.game_name,
            self.ZT.game_name
        ]

    def load_game(self, game_name, surface):
        # This will load a specific game from the games directory
        self.surface = surface
        if game_name in self.game_names:
            self.loaded_game = game_name
            self.log.write_log("INFO", "GAME: " + self.loaded_game + " loaded.")
            if game_name == "DRON":
                self.game = DRON.Dron()
                self.game.load()
            elif game_name == "Zone Trespassers":
                self.game = self.ZT
                self.game.load()
            else:
                print("Game does not exist")

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
            self.game.key_input(event)
        except AttributeError as e:
            self.log.write_log("ERROR", "key_input error: " + str(e))

    # Not sure if i'll keep this in, prob not.
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
