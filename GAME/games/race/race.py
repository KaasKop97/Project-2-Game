import pygame


class Race:
    def __init__(self):
        self.game_name = "Race"
        self.author = "Aman"

    def load(self, surface):
        # This is the first thing that's called, load stuff here. Must return a boolean!!
        return True

    def update(self, surface):
        # This method gets called every frame so be careful with this one.
        pass

    def mousebutton_down(self, surface, event):
        # If you need to do an action on mouse button while it's in the down position then use this
        pass

    def mousebutton_up(self, surface, event):
        # If you need to do an action on mouse button while it's in the up position (after a down) then use this
        pass

    def key_input(self, key):
        # If you need to do an action on key inputs use this access key codes, check DRON.py for examples
        # For example: key A = keycode 97 so to check this do 'if key == 97'
        pass

    def stop_game(self):
        pass
