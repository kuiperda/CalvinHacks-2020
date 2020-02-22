"""
TurnTimer.py
Keep track of turns and show bar on screen.
For CalvinHacks 2020
"""

INTERVAL = 10   # Length of turn in frames
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

import pygame

class TurnTimer:
    """
    Constructor.
    Takes width and height params as the size of the bar.
    """
    def __init__(self, width, height):
        self._interval = INTERVAL
        self._current_tick = 0
        self._width = width
        self._height = height
        self._surface = pygame.Surface((width,height))
        self._border_rect = pygame.Rect(0, 0, self._width, self._height)
        self._fill_rect = pygame.Rect(5, 5, self._width - 10, self._height - 10)

        self.drawBar()

    def getSurface(self):
        return self._surface
    
    """
    Increase the tick timer.
    Should be called on every frame.
    """
    def tick(self):
        self._current_tick += 1
        if self._interaval == self._current_tick:
            # TODO: Throw an event or something
            self._current_tick = 0

    """
    Draw the empty bar.
    Should not be called by an external function.
    """
    def drawBar(self):
        pygame.draw.rect(self._surface, WHITE, self._border_rect)
        pygame.draw.rect(self._surface, BLACK, self._fill_rect)
