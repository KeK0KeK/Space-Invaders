import controller
import pygame
import GameMenu
from pygame.sprite import Group
from gun import Gun
from stats import Stats
from scores import Scores


# File app - is the main file.
# Here the project is launched through to a single function - run()

# Main function
def run():
    pygame.init()
    # Description of the game screen
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space attack")
    # Launch menu and music in the background
    GameMenu.music_in_menu()
    GameMenu.menu_control(screen)
    bg_color = pygame.image.load('Image/fon.jpg')
    # Turning on the display of the gun
    gun = Gun(screen)
    # Grouping Bullets and Army into Groups
    bullets = Group()
    army = Group()
    # Creation of an army
    controller.create_army(screen, army)
    # Battle music start
    controller.play_music()
    # While the game is in progress...
    stats = Stats()
    scores = Scores(screen, stats)
    # ...actions are displayed:
    while True:
        controller.events(screen, gun, bullets)
        if stats.run_game:
            # guns
            gun.update_gun()
            # interface
            controller.update(bg_color, screen, stats, scores, gun, army, bullets)
            # bullets
            controller.update_bullets(screen, stats, scores, army, bullets)
            # armies
            controller.update_army(stats, screen, scores, gun, army, bullets)


run()
