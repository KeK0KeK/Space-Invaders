import pygame


# Class Bullet was created to describe the functions of the bullet
class Bullet(pygame.sprite.Sprite):

    # Main function for bullet
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        # Bullet size
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 232, 200, 42
        self.speed = 4.5
        # Description of where the bullets come from
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    # Function for drawing the flight path of a bullet
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    # Function for drawing the body of a bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
