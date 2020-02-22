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
hexgrid = HexMap(xrad=3, yrad=3, zrad=3, size=hex_dims[0])
hex_image = pygame.image.load("HexMap/regular_hex.png")
hex_image = pygame.transform.scale(hex_image, hex_dims)
hex_startpix = (40, 150)
hexgrid.draw_hex_rect(hex_startpix, hex_image, screen)

# pixel offsets for wizards compared to the pixel location of the hex
wizard_offsets = (hexgrid.get_hexsize() // 4, hexgrid.get_hexsize() // 8)

start1_hex, start1_pix = hexgrid.get_corner("NW")
start2_hex, start2_pix = hexgrid.get_corner("SE")

p1_img = pygame.image.load("imgs/blueWiz.png")
p1_img = pygame.transform.scale(p1_img, (p1_img.get_width() * (round(hex_dims[1] * 3/4) // p1_img.get_height()),  round(hex_dims[1] * 3/4)))
p2_img = pygame.image.load("imgs/redWiz.png")
p2_img = pygame.transform.scale(p2_img, (p2_img.get_width() * (round(hex_dims[1] * 3/4) // p2_img.get_height()),  round(hex_dims[1] * 3/4)))
screen.blit(p1_img, (start1_pix[0] + wizard_offsets[0], start1_pix[1] + wizard_offsets[1]))
screen.blit(p2_img, (start2_pix[0] + wizard_offsets[0], start2_pix[1] + wizard_offsets[1]))

direction_keybindings_1 = {pygame.K_q: (-1, 1, 0), pygame.K_w: (0, 1, -1), pygame.K_e: (1, 0, -1),
                         pygame.K_a: (-1, 0, 1), pygame.K_s: (0, -1, 1), pygame.K_d: (1, -1, 0)}
direction_keybindings_2 = {pygame.K_i: (-1, 1, 0), pygame.K_o: (0, 1, -1), pygame.K_p: (1, 0, -1),
                         pygame.K_k: (-1, 0, 1), pygame.K_l: (0, -1, 1), pygame.K_SEMICOLON: (1, -1, 0)}
# direction_keybindings_1 = {pygame.K_q: 4, pygame.K_w: 5, pygame.K_e: 0,
#                          pygame.K_a: 3, pygame.K_s: 2, pygame.K_d: 1}
# direction_keybindings_2 = {pygame.K_i: 4, pygame.K_o: 5, pygame.K_p: 0,
#                          pygame.K_k: 3, pygame.K_l: 2, pygame.K_SEMICOLON: 1}

# The main loop
def mainLoop():
    while True:
        eventList = pygame.event.get()
        
        for event in eventList:
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key in direction_keybindings_1:
                    direction = direction_keybindings_1[event.key]
                    neighbor = hexgrid.get_neighbor(start1_hex, direction)
                    if neighbor:
                        neighbor_pix = hexgrid.draw_neighbor(start1_pix, direction, p1_img, screen, offset=wizard_offsets)
                elif event.key in direction_keybindings_2:
                    direction = direction_keybindings_2[event.key]
                    neighbor = hexgrid.get_neighbor(start2_hex, direction)
                    if neighbor:
                        neighbor_pix = hexgrid.draw_neighbor(start2_pix, direction, p2_img, screen, offset=wizard_offsets)
        timer.tick()            # tick the timer (must be before timer blit)
        screen.blit(timer.getSurface(), (20, 20))
        pygame.display.flip()   # update the screen
        clock.tick()            # tick the clock

mainLoop()
