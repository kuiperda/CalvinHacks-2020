"""
main.py
Runs the main loop
For CalvinHacks 2020
"""

# Initialize pygame
import pygame
import TurnTimer as tt

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Caster Blaster")

clock = pygame.time.Clock()

timer = tt.TurnTimer(300, 50)

# The main loop
def mainLoop():
    while True:
        eventList = pygame.event.get()
        
        for event in eventList:
            if event.type == pygame.QUIT:
                return
        screen.blit(timer.getSurface(), (20, 20))
        pygame.display.flip()   # update the screen
        clock.tick()            # tick the clock

mainLoop()
