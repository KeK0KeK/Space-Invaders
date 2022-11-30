import pygame


# Class Enemy was created to describe the functions of the bullet
class Enemy(pygame.sprite.Sprite):
    # Main function for bullet
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        # Enemies are a picture that moves across the screen every time interval
        self.image = pygame.image.load('Image/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Function for drawing the body of an enemy
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # The function of drawing the movement of the enemy on the screen
    def update(self):
        self.y += 0.1
        self.rect.y = self.y
