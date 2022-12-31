# Import pygame
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    RLEACCEL
)

# Import constants
from constants import *
from components.levels import Level

# Define a Player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load(PLAYER_IMG).convert()
        self.image.set_colorkey(WHITE, RLEACCEL)
        self.rect = self.image.get_rect()
        
        self.level: Level = None

        self.fly_up = pygame.mixer.Sound(FLY_UP_SOUND)
        self.fly_down = pygame.mixer.Sound(FLY_DOWN_SOUND)
        self.crash = pygame.mixer.Sound(CRASH_SOUND)

        self.fly_up.set_volume(0.5)
        self.fly_down.set_volume(0.5)
        self.crash.set_volume(0.8)

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.fly_up.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.fly_down.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        
        # See if we hit an enemy
        if pygame.sprite.spritecollideany(self, self.level.enemy_list):
            self.fly_up.stop()
            self.fly_down.stop()
            self.crash.play()
            self.kill()
        
        if self.rect.right >= SCREEN_WIDTH:
            pygame.event.post(LEVELUP)