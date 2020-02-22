"""
TurnTimer.py
Keep track of turns and show bar on screen.
For CalvinHacks 2020
"""

INTERVAL = 10   # Length of turn in frames

class TurnTimer:
    def __init__(self):
        this._interval = INTERVAL
        this._current_tick = 0
