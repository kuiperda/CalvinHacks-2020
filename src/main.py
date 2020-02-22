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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("q")
                elif event.key == pygame.K_w:
                    print("w")
                elif event.key == pygame.K_e:
                    print("e")
                elif event.key == pygame.K_a:
                    print("a")
                elif event.key == pygame.K_s:
                    print("s")
                elif event.key == pygame.K_d:
                    print("d")

        timer.tick()            # tick the timer (must be before timer blit)
        screen.blit(timer.getSurface(), (20, 20))
        pygame.display.flip()   # update the screen
        clock.tick()            # tick the clock

mainLoop()
