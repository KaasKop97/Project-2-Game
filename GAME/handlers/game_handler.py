from games.DRON import DRON
from games.Galaxy_Trespassers import Galaxy_Trespassers
from games.race import race
from games.dodge_fangirls import dodge_fangirls
from helpers import log_helper


class GameHandler:
    def __init__(self, surface):
        self.loaded_game = None
        self.game = None
        self.surface = surface

        self.log = log_helper.LogHelper()
        # self.DRON = DRON.Dron(self.surface)
        # self.GT = Galaxy_Trespassers.GalaxyTrespassers(self.surface)
        # self.race = race.race(self.surface)
        # self.DF = dodge_fangirls.DodgeFangirls(self.surface)
        #
        # self.game_names = [
        #     self.DRON.game_name,
        #     self.GT.game_name,
        #     self.race.game_name,
        #     self.DF.game_name
        # ]

        self.game_names = [
            "DRON",
            "Galaxy Trespassers",
            "Race",
            "Dodge the Fangirls"
        ]

    def load_game(self, game_name):
        # This will load a specific game from the games directory
        if game_name in self.game_names:
            self.loaded_game = game_name
            self.log.write_log("INFO", "GAME: " + self.loaded_game + " loaded.")
            if game_name == "DRON":
                self.game = DRON.Dron(self.surface)
                self.game.load()
            elif game_name == "Galaxy Trespassers":
                self.game = Galaxy_Trespassers.GalaxyTrespassers(self.surface)
                self.game.load()
            elif game_name == "Race":
                self.game = race.race(self.surface)
                self.game.load()
            elif game_name == "Dodge the Fangirls":
                self.game = dodge_fangirls.DodgeFangirls(self.surface)
                self.game.load()
            else:
                print("Game does not exist")

    def main_loop(self):
        try:
            self.game.update()
        except AttributeError as e:
            self.log.write_log("ERROR", "update error: " + str(e))

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

    def key_down(self, event):
        try:
            self.game.key_down(event)
        except AttributeError as e:
            self.log.write_log("ERROR", "key_input error: " + str(e))

    def key_up(self, event):
        try:
            self.game.key_up(event)
        except AttributeError as e:
            self.log.write_log("ERROR", "key_input error: " + str(e))

    def unload_game(self):
        self.loaded_game = None
        self.game.stop_game()

