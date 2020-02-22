"""
main.py
Runs the main loop
For CalvinHacks 2020
"""

# Initialize pygame
import pygame

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Caster Blaster")

# The main loop
def mainLoop():
    while True:
        eventList = pygame.event.get()
        
        for event in eventList:
            if event.type == pygame.QUIT:
                return

mainLoop()
