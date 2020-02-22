"""
main.py
Runs the main loop
For CalvinHacks 2020
"""

# Initialize pygame
import pygame
import TurnTimer as tt
from HexMap import HexMap

screen = pygame.display.set_mode((1000,1000))
screen.fill((255, 255, 255))  # set the screen to white
pygame.display.set_caption("Caster Blaster")

clock = pygame.time.Clock()

timer = tt.TurnTimer(300, 50)

hex_dims = (390 // 3, 338 // 3)
hexgrid = HexMap(xrad=4, yrad=3, zrad=2, size=hex_dims[0])
hex_image = pygame.image.load("HexMap/regular_hex.png")
hex_image = pygame.transform.scale(hex_image, hex_dims)
hex_startpix = (40, 150)
hexgrid.draw_hex_rect(hex_startpix, hex_image, screen)

# The main loop
def mainLoop():
    while True:
        eventList = pygame.event.get()
        
        for event in eventList:
            if event.type == pygame.QUIT:
                return
        timer.tick()            # tick the timer (must be before timer blit)
        screen.blit(timer.getSurface(), (20, 20))
        pygame.display.flip()   # update the screen
        clock.tick()            # tick the clock

mainLoop()
