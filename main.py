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
menu_items = ["PLAY", "ABOUT", "CREDITS", "QUIT"]
# menu_items.extend(games.games_in_path)
# print(menu_items)

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
    menu.make_button(background, (255, 255, 255), 10, 10 + (40 * i), 75, 30, menu_items[i])
    logger.write_log("INFO", "Drawing button: " + menu_items[i])

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
                menu.button_pressed(event.pos)
                logger.write_log("DEBUG", "Mouse button pressed.")

            elif event.type == pygame.QUIT:
                print("DEBUG: Event quit fired, stopping program." if conf.get_value("development", "debug") else "")
                done = True

    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
