import pygame

from handlers import config_handler, game_load_handler
from helpers import menu_helper, settings_helper, log_helper

# Creating the objects for the configuration handler, game loading, and menu.
conf = config_handler.ConfigHandler()
games = game_load_handler.GameLoadHandler()
menu = menu_helper.MenuHelper()
logger = log_helper.LogHelper()

pygame.init()

done = False
game_loaded = False
menu_drawn = False
game_loaded_name = None
menu_items = ["PLAY", "ABOUT", "SETTINGS", "CREDITS", "QUIT"]

# Here we initialize a window for the game itself, in the future we'll check the settings if its fullscreen or not
screen = pygame.display.set_mode([int(conf.get_value("game", "width")), int(conf.get_value("game", "height"))])
pygame.display.set_caption(conf.get_value("game", "caption"))

# This is all pre-game loading so here we just set the surface to the correct screen size and set it to an
# background colour
# The clock creates an object to help track time
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert(background)
background.fill((255, 255, 255))

# Drawing the buttons of the menu outside of the while loop to prevent it from repeated draws.
for i in range(len(menu_items)):
    menu.create_button(background, (255, 255, 255), int(conf.get_value("game", "width")) // 2 - 55, 10 + (40 * i), 85, 30, menu_items[i])
    logger.write_log("DEBUG", "Drawing button: " + menu_items[i])

# Everything in this while loop is called once per frame. So be careful!
while not done:
    # Here we call the clock to tick, if we set this to '60' we delay the runtime game speed. This subsequently also
    # Limits the game to 60fps (as it should, if you say 30fps is more 'cinematic' please, kill yourself.)
    clock.tick(60)

    if game_loaded:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_loaded_name = "Gets the currently loaded game and then use that to access the class where all the logic is"
            elif event.type == pygame.QUIT:
                done = True
    else:
        # This pretty much means that we're in the main menu.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if button is pressed here.
                menu_selection = menu.button_pressed(event.pos)
                logger.write_log("DEBUG", "Button pressed: " + str(menu_selection))
                # TODO: make a if statement for all menu selections
                if menu_selection == "PLAY":
                    menu.reset(background, (255, 255, 255))
                    for i in range(len(games.games_in_path)):
                        menu.create_button(background, (255, 255, 255), int(conf.get_value("game", "width")) // 2 - 55, 10 + (40 * i), 85, 30, games.games_in_path[i])
                        if i == len(games.games_in_path) - 1:
                            menu.create_button(background, (255, 255, 255), 10, 10 + (80 * i), 85, 30, "BACK")
                if menu_selection == "QUIT":
                    # Now the quit button works, no more SAO flashbacks 8).
                    # TODO: make a confirmation message "Do you really wanna quit"
                    done = True
                if menu_selection == "BACK":
                    print("You wanna go back ayy?")
            elif event.type == pygame.QUIT:
                logger.write_log("DEBUG", "Quitting...")
                done = True

    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
