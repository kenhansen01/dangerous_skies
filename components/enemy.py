# Import pygame, random
import pygame
import random

from pygame.locals import (
    RLEACCEL
)

# Import constants
from constants import *

# Define the enemy object extending pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMG).convert()
        self.image.set_colorkey(WHITE, RLEACCEL)
        # get the rect for the sprite and randomly set the location 20 - 100 px off the screen to the right and on the screen top to bottom
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        # give the sprite a random speed between 5 - 20
        self.speed = random.randint(5, 20)

    # Move the sprite left across the screen based on speed
    # Remove sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
