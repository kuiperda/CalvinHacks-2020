"""
TurnTimer.py
Keep track of turns and show bar on screen.
For CalvinHacks 2020
"""

INTERVAL = 1000             # Length of turn in miliseconds
FILL = (0, 0, 0)            # Fill color
BORDER = (255, 255, 255)    # Border color

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
        self._clock = pygame.time.Clock()

        self.drawBar()

    def getSurface(self):
        return self._surface
    
    """
    Increase the tick timer.
    Should be called on every frame.
    Returns True when a new turn is hit, False otherwise.
    """
    def tick(self):
        self._current_tick += self._clock.tick()
        if self._current_tick > self._interval:
            self._current_tick = 0
            self.drawBar()
            return True
        else:
            self.updateBar()
            return False

    """
    Draw the empty bar.
    Called when the timer is reset.
    Should not be called by an external function.
    """
    def drawBar(self):
        pygame.draw.rect(self._surface, BORDER, self._border_rect)
        pygame.draw.rect(self._surface, FILL, self._fill_rect)

    """
    Updates the bar with the current timer value.
    Called by tick().
    Should not be called by an external function.
    """
    def updateBar(self):
        updateRect = pygame.Rect(0, 0, (self._width / self._interval) * self._current_tick, self._height)
        pygame.draw.rect(self._surface, BORDER, updateRect)
