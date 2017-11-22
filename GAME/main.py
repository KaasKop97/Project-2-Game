import pygame

from handlers import config_handler, game_handler
from helpers import menu_helper, settings_helper, log_helper

# Creating the objects for the configuration handler, game loading, and menu.
conf = config_handler.ConfigHandler()
game_handler = game_handler.GameHandler()
menu = menu_helper.MenuHelper()
logger = log_helper.LogHelper()

pygame.init()

done = False

# Here we initialize a window for the game itself, in the future we'll check the settings if its fullscreen or not
screen = pygame.display.set_mode([int(conf.get_value("game", "width")), int(conf.get_value("game", "height"))])
pygame.display.set_caption(conf.get_value("game", "caption"))

# This is all pre-game loading so here we just set the surface to the correct screen size and set it to an
# background colour
# The clock creates an object to help track time
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert(background)

menu.draw_main_menu(background)

# Everything in this while loop is called once per frame. So be careful!
while not done:
    # Limit the fps and resources used to 60 times a second
    clock.tick(60)

    if game_handler.loaded_game is not None:
        game_handler.main_loop()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_handler.mousebutton_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                game_handler.mousebutton_up(event.pos)
            elif event.type == pygame.KEYDOWN:
                game_handler.key_input(event.key)
                if event.key == 27:
                    game_handler.unload_game()
                    menu.draw_main_menu(background)
                    break
            elif event.type == pygame.QUIT:
                done = True
    else:
        # This pretty much means that we're in the main menu.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_selection = menu.button_pressed(event.pos)
                logger.write_log("DEBUG", "Button pressed: " + str(menu_selection))

                # TODO: make an if statement for all menu selections
                if menu_selection == "PLAY":
                    menu.draw_game_selection(background)
                elif menu_selection == "QUIT GAME":
                    # TODO: make a confirmation message "Do you really wanna quit"
                    done = True
                elif menu_selection == "BACK":
                    # Should save somewhere where we came from and then return to that.
                    menu.go_back(background)
                elif menu_selection == "DRON":
                    menu.reset(background)
                    game_handler.load_game("DRON", background)
                    game_loaded = True
                elif menu_selection == "Zone Trespassers":
                    menu.reset(background)
                    game_handler.load_game("Zone Trespassers", background)
                    game_loaded = True
            elif event.type == pygame.QUIT:
                logger.write_log("DEBUG", "Quitting...")
                done = True
    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()
