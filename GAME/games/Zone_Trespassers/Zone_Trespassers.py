import pygame


class ZoneTrespassers:
    def __init__(self):
        self.game_name = "Zone Trespassers"
        self.author = "Cherie"

    def load(self):
        # This is the first thing thats called, load stuff here or just call update your call. Must return a boolean
        return True

    def update(self, surface):
        # This methods gets called every frame so be careful with this one.
        pass

    def mousebutton_down(self):
        # If you need to do an action on mousebutton while it's in the down position then use this
        pass

    def mousebutton_up(self):
        # If you need to do an action on mousebutton while it's in the up position (after a down) then use this
        pass

    def key_input(self, key):
        # If you need to do an action on key inputs use this access key codes
        pass

    def stop_game(self):
        pass
