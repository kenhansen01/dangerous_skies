# Import pygame
import pygame

# Game imports, constants, enemies, clouds
from constants import *
from components.enemy import Enemy
from components.cloud import Cloud

# Base level class, all levels inherit
class Level():
    
    def __init__(self, player):
        # Constructor. Pass in the player. Needed for collision with enemies

        # Lists of sprites used in all levels
        self.cloud_list = None
        self.enemy_list = None

        # Background image
        self.background = None

        # Level objects
        self.cloud_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # Level difficulty
        self.difficulty = 0
    
    # Update the level
    def update(self):
        self.cloud_list.update()
        self.enemy_list.update()

    # Draw level to screen
    def draw(self, screen: pygame.Surface):

        # Draw the background
        screen.fill(BLACK)
        screen.blit(self.background, (0,0))

        # Draw all the sprite lists
        self.cloud_list.draw(screen)
        self.enemy_list.draw(screen)

    # TODO: method to add enemies to level and method to add clouds to level
    
    def set_difficulty(self, ev: pygame.USEREVENT, baseline: int):
        pygame.time.set_timer(ev, baseline // self.difficulty)

    def add_enemy(self):
        new_enemy = Enemy()
        self.enemy_list.add(new_enemy)

    def add_cloud(self):
        new_cloud = Cloud()
        self.cloud_list.add(new_cloud)

# Create level 1
class Level_01(Level):

    def __init__(self, player):
        super().__init__(player)

        # Level specific info below
        self.background = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.background.fill(SKY_BLUE)
        # self.background.set_colorkey(WHITE)

        self.difficulty = 1
# level 2
# Create level 1
class Level_01(Level):

    def __init__(self, player):
        super().__init__(player)

        # Level specific info below
        self.background = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.background.fill(SKY_BLUE)
        # self.background.set_colorkey(WHITE)

        self.difficulty = 2