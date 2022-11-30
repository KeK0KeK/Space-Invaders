import pygame
from pygame.sprite import Sprite


# Class Gun created to describe the functions of the gun
class Gun(Sprite):

    # Main function in this class
    def __init__(self, screen):

        super(Gun, self).__init__()
        self.screen = screen
        # Gun represents a picture that moves left/right
        self.image = pygame.image.load('Image/ImageGun.png')
        self.rect = self.image.get_rect()
        # Initial appearance in the game
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # Move left/right action
        self.mright = False
        self.mleft = False

    # Function to drawing a gun
    def output(self):
        self.screen.blit(self.image, self.rect)

    # Function to describe the speed of the gun in different directions
    def update_gun(self):

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5
        self.rect.centerx = self.center

    # The function of creating a gun in the game
    def create_gun(self):
        self.center = self.screen_rect.centerx
