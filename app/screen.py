from pygame import display, Surface, OPENGL, RESIZABLE, SCALED, FULLSCREEN

from .constants import *

class Screen(display):
    
    def __init__(self) -> None:
        super().__init__()

        self.flags = OPENGL | RESIZABLE | SCALED
        
        self.main_window = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), self.flags, vsync=1)