import pygame
from components.player import Player

from constants import *

if __name__ == "__main__":
    from pygame.locals import (
        K_ESCAPE,
        KEYDOWN,
        QUIT
    )
    pygame.init()

    # Create the screen using constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_CAPTION)

    # Create the player
    player = Player()

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

        screen.fill(BLACK)
        # Get pressed keys send to player update
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        # ALL DRAW CODE BELOW THIS COMMENT
        screen.blit(player.surf, player.rect)
        # ALL DRAW CODE ABOVE THIS COMMENT

        # Set clock to FPS
        clock.tick(FPS)

        # Flip screen
        pygame.display.flip()
    
    # Be IDLE friendly
    pygame.quit()
