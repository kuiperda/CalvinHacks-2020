"""
main.py
Runs the main loop
For CalvinHacks 2020
"""

# Initialize pygame
import pygame
import TurnTimer as tt
from HexMap import HexMap
from Player import Player

def move_item(item, direction, offset, image, distance=1):
    start_hex = item.get_position()
    start_pix = item.get_pixels()
    neighbor = hexgrid.get_neighbor(start_hex, direction)
    neighbor_pix = None
    if neighbor:
        neighbor_pix = hexgrid.draw_neighbor(start_pix, direction, image, screen, offset=offset)
        print("moved to", neighbor, neighbor_pix)
        item.set_position(neighbor)
        item.set_pixels(neighbor_pix)
        screen.blit(hex_image, start_pix)
    return neighbor_pix

def move_player(player, direction, distance=1):
    return move_item(player, direction=direction, offset=wizard_offsets, image=player.get_image(), distance=distance)

def check_collisions_player():
    if abs(player1.get_pixels()[0] - player2.get_pixels()[0]) < 10 \
            and abs(player1.get_pixels()[1] - player2.get_pixels()[1]) < 10:
        return True

screen = pygame.display.set_mode((1000,1000))
screen.fill((255, 255, 255))  # set the screen to white
pygame.display.set_caption("Caster Blaster")

clock = pygame.time.Clock()

timer = tt.TurnTimer(300, 50)

hex_dims = (390 // 3, 338 // 3)
hexgrid = HexMap(xrad=3, yrad=3, zrad=3, size=hex_dims[0])
hex_image = pygame.image.load("HexMap/regular_hex_white.png")
hex_image = pygame.transform.scale(hex_image, hex_dims)
hex_startpix = (40, 150)
hexgrid.draw_hex_rect(hex_startpix, hex_image, screen)

# pixel offsets for wizards compared to the pixel location of the hex
# wizard_offsets = (hexgrid.get_hexsize() // 4, hexgrid.get_hexsize() // 8)
wizard_offsets = (0, 0)

start1_hex, start1_pix = hexgrid.get_corner("NW")
start2_hex, start2_pix = hexgrid.get_corner("SE")

p1_img = pygame.image.load("imgs/blueWiz_center.png")
p1_img = pygame.transform.scale(p1_img, (p1_img.get_width() // 3, p1_img.get_height() // 3))
p2_img = pygame.image.load("imgs/redWiz_center.png")
p2_img = pygame.transform.scale(p2_img, (p2_img.get_width() // 3, p2_img.get_height() // 3))

player1 = Player(hp=10, position=start1_hex, pixels=start1_pix, spells=[], image=p1_img)
player2 = Player(hp=10, position=start2_hex, pixels=start2_pix, spells=[], image=p2_img)

# TODO: use player1 and player2
screen.blit(p1_img, (start1_pix[0] + wizard_offsets[0], start1_pix[1] + wizard_offsets[1]))
screen.blit(p2_img, (start2_pix[0] + wizard_offsets[0], start2_pix[1] + wizard_offsets[1]))

direction_keybindings_1 = {pygame.K_q: (-1, 1, 0), pygame.K_w: (0, 1, -1), pygame.K_e: (1, 0, -1),
                         pygame.K_a: (-1, 0, 1), pygame.K_s: (0, -1, 1), pygame.K_d: (1, -1, 0)}
direction_keybindings_2 = {pygame.K_i: (-1, 1, 0), pygame.K_o: (0, 1, -1), pygame.K_p: (1, 0, -1),
                         pygame.K_k: (-1, 0, 1), pygame.K_l: (0, -1, 1), pygame.K_SEMICOLON: (1, -1, 0)}

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
                    print("moving player 1", player1.get_position(), "player 2 at", player2.get_position())
                    move_player(player1, direction)
                elif event.key in direction_keybindings_2:
                    direction = direction_keybindings_2[event.key]
                    print("moving player 2", player2.get_position(), "player 1 at", player1.get_position())
                    move_player(player2, direction)
                if check_collisions_player():
                    print("Player collision!")
                    return
        if timer.tick():        # tick the timer (must be before timer blit)
            # TODO: This is a new turn
            print("New turn!")
        screen.blit(timer.getSurface(), (20, 20))
        pygame.display.flip()   # update the screen
        clock.tick()            # tick the clock

mainLoop()
