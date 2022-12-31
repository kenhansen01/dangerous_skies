# Import pygame
import pygame

# Import needed key names from pygame.locals
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Import all constants
from constants import *

# Import Level and Player Components
from components import levels
from components.player import Player

def main():
    # Setup for sounds - init pygame.mixer

    # Main program
    pygame.init()

    # Create the screen using constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_CAPTION)

    # Create the player
    player = Player()
    
    # Create all the levels and add to level_list 
    level_list = []
    level_list.append(levels.Level_01(player))
    
    # Set the current_level_number to 0, then set current_level, set difficulty
    current_level_number = 0
    current_level: levels.Level = level_list[current_level_number]
    current_level.set_difficulty(ADDENEMY, 250)
    current_level.set_difficulty(ADDCLOUD, 1000)

    # Create active_sprite_list, set player level, add player to list
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    active_sprite_list.add(player)

    pygame.mixer.music.load(GAME_MUSIC)
    pygame.mixer.music.play(loops=-1)

    # Setup the clock to manage framerate
    clock = pygame.time.Clock()

    # Loop until player lose or quit
    running = True

    # ------------ Main Program Loop ----------
    while running:
        # Look at every event
        for event in pygame.event.get():
            # Did user hit a key?
            if event.type == KEYDOWN:
                # Stop loop if it was escape key
                if event.key == K_ESCAPE:
                    running = False

            # Did the user hit close button?
            elif event.type == QUIT:
                running = False

            # Custom events 
            # ADDENEMY level.addenemy
            elif event.type == ADDENEMY:
                current_level.add_enemy()
            # ADDCLOUD level.addcloud
            elif event.type == ADDCLOUD:
                current_level.add_cloud()
            # LEVELUP
            elif event.type == LEVELUP:
                current_level_number += 1
                current_level = level_list[current_level_number]
                current_level.set_difficulty(ADDENEMY, 250)
                current_level.set_difficulty(ADDCLOUD, 1000)
        
        # Get pressed keys send to player update
        pressed_keys = pygame.key.get_pressed()
        # player.update(pressed_keys)
        active_sprite_list.update(pressed_keys)
        
        # Update level
        current_level.update()

        # ALL DRAW CODE BELOW THIS COMMENT
        # screen.fill(BLACK)
        # Draw current_level
        current_level.draw(screen)
        
        # Draw active_sprite_list
        active_sprite_list.draw(screen)

        # ALL DRAW CODE ABOVE THIS COMMENT

        # End the game after 500 ms pause for sound
        if len(active_sprite_list) < 1:
            pygame.mixer.music.stop()
            pygame.time.delay(500)
            pygame.mixer.quit()
            running = False

        # Set clock to FPS
        clock.tick(FPS)

        # Flip screen
        pygame.display.flip()
    
    # Be IDLE friendly
    pygame.quit()

if __name__ == "__main__":
    main()