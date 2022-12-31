import pygame
# Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CAPTION = "Dangerous Skies"
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
TRANSPARENT = (0, 0, 0, 0)

# Images
CLOUD_IMG = "assets/images/cloud.png"
PLAYER_IMG = "assets/images/jet.png"
ENEMY_IMG = "assets/images/missile.png"

# Music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
GAME_MUSIC = "assets/sounds/Apoxode_-_Electric_1.mp3"

# Sounds
# Sound sources: Jon Fincher
CRASH_SOUND = "assets/sounds/Collision.ogg"
FLY_UP_SOUND = "assets/sounds/Rising_putter.ogg"
FLY_DOWN_SOUND = "assets/sounds/Rising_putter.ogg"

# Create custom game loop events limit of 9 custom events
# ADDENEMY event, runs every 250 ms
ADDENEMY = pygame.event.custom_type()
# ADDCLOUD event
ADDCLOUD = pygame.event.custom_type()
# LEVELUP event
LEVELUP = pygame.event.custom_type()

if __name__ == "__main__":
    print("Sky blue RGB code is", SKY_BLUE)
    print(SCREEN_CAPTION)