import pygame

from handlers import config_handler, game_handler
from helpers import menu_helper, log_helper


class Main:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.logger = log_helper.LogHelper()

        pygame.init()

        self.screen = pygame.display.set_mode(
            [int(self.conf.get_value("game", "width")), int(self.conf.get_value("game", "height"))])
        pygame.display.set_caption(self.conf.get_value("game", "caption"))

        self.running = True
        self.game_loaded = False
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert(self.background)
        self.bg_rect = self.background.get_rect()
        self.clock = pygame.time.Clock()

        self.menu = menu_helper.MenuHelper(self.background)
        self.game_handler = game_handler.GameHandler(self.background)

    def main_loop(self):
        menu_to_draw = "main"
        self.menu.draw_menu(menu_to_draw)
        while self.running:
            self.clock.tick(60)
            if not self.game_handler.loaded_game:
                pygame.mouse.set_visible(True)
                if not menu_to_draw == "":
                    self.menu.draw_menu(menu_to_draw)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button_pressed = self.menu.get_button_pressed(event.pos)
                        if not button_pressed == self.menu.currently_drawn:
                            if button_pressed == "PLAY" and not menu_to_draw == "PLAY":
                                menu_to_draw = "PLAY"
                            elif button_pressed == "QUIT":
                                self.running = False
                                pygame.quit()
                            elif button_pressed == "DRON":
                                self.game_handler.load_game("DRON")
                                menu_to_draw = ""
                                self.menu.reset_menu()
                                self.menu = None
                            elif button_pressed == "Dodge the Fangirls":
                                self.game_handler.load_game("Dodge the Fangirls")
                                menu_to_draw = ""
                                self.menu.reset_menu()
                                self.menu = None
                            elif button_pressed == "Race":
                                self.game_handler.load_game("Race")
                                menu_to_draw = ""
                                self.menu.reset_menu()
                                self.menu = None
                            elif button_pressed == "Galaxy Trespassers":
                                self.game_handler.load_game("Galaxy Trespassers")
                                menu_to_draw = ""
                                self.menu.reset_menu()
                                self.menu = None
                            else:
                                print("ERROR: Can't load button since there is no definition for it.")
                    elif event.type == pygame.KEYDOWN:
                        if event.key == 27 and menu_to_draw == "PLAY":
                            menu_to_draw = "main"
                    elif event.type == pygame.QUIT:
                        print("Quitting")
                        self.running = False
                if self.menu:
                    self.menu.get_hover(pygame.mouse.get_pos())
            else:
                pygame.mouse.set_visible(False)
                self.game_handler.main_loop()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_handler.mousebutton_down(event.pos)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.game_handler.mousebutton_up(event.pos)
                    elif event.type == pygame.KEYDOWN:
                        self.game_handler.key_down(event.key)
                        if event.key == 27:
                            self.game_handler.unload_game()
                            menu_to_draw = "main"
                            self.menu = menu_helper.MenuHelper(self.background)
                            # self.menu.draw_menu("main")
                    elif event.type == pygame.KEYUP:
                        self.game_handler.key_up(event.key)
                    elif event.type == pygame.QUIT:
                        print("Quitting")
                        self.running = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.update()


game = Main()
game.main_loop()
