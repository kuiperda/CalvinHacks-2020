"""
TurnTimer.py
Keep track of turns and show bar on screen.
For CalvinHacks 2020
"""

INTERVAL = 10   # Length of turn in frames

class TurnTimer:
    def __init__(self):
        self._interval = INTERVAL
        self._current_tick = 0
    
    """
    Incraese the tick timer.
    Should be called on every frame.
    """
    def tick(self):
        self._current_tick += 1
        if self._interaval == self._current_tick:
            # TODO: Throw an event or something
            self._current_tick = 0
