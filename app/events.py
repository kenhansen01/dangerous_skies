from pygame.event import custom_type

# Create custom game loop events limit of 9 custom events
# ADDENEMY event, runs every 250 ms
ADDENEMY = custom_type()
# ADDCLOUD event
ADDCLOUD = custom_type()
# LEVELUP event
LEVELUP = custom_type()