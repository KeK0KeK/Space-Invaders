import pygame.font
from gun import Gun
from pygame.sprite import Group


# The class was created to inform the user during the game.
# The class contains functions for displaying the current score,
# the best score for all games and the number of "lives" of the game gun
class Scores:

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        # Font color and size
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        # Show score, best score and lives
        self.image_score()
        self.image_high_score()
        self.image_guns()

    # Score display function
    def image_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    # Gun life rendering function
    def image_guns(self):
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    # Best score display function
    def image_high_score(self):
        self.the_best_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.the_best_score_rect = self.the_best_score_image.get_rect()
        self.the_best_score_rect.centerx = self.screen_rect.centerx
        self.the_best_score_rect.top = self.screen_rect.top + 20

    # The function of drawing scores and gun lives
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.the_best_score_image, self.the_best_score_rect)
        self.guns.draw(self.screen)
