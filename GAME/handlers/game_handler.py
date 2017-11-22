from games.DRON import DRON
from games.Galaxy_Trespassers import Galaxy_Trespassers
from games.race import race
from games.dodge_fangirls import dodge_fangirls
from helpers import log_helper


class GameHandler:
    def __init__(self):
        self.loaded_game = None
        self.game = None
        self.surface = None
        self.log = log_helper.LogHelper()
        self.DRON = DRON.Dron()
        self.GT = Galaxy_Trespassers.ZoneTrespassers()
        self.race = race.Race()
        self.DF = dodge_fangirls.DodgeFangirls()

        self.game_names = [
            self.DRON.game_name,
            self.GT.game_name,
            self.race.game_name,
            self.DF.game_name
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
                self.game = self.GT
                self.game.load()
            elif game_name == "Race":
                self.game = self.race
                self.game.load()
            elif game_name == "Dodge the Fangirls":
                self.game = self.DF
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
        self.loaded_game = None
        self.game.stop_game()

