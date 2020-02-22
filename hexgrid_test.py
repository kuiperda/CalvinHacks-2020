import pygame
import HexMap

# import the pygame module, so you can use it
import pygame


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("hexgrid test")

    hex_image = pygame.image.load("HexMap/regular_hex.png")
    # scale image to half its original size
    hex_image = pygame.transform.scale(hex_image, (195, 169))

    # hex_width = 338
    hex_width = 169
    width_scale = 0.86
    height_scale = 0.5
    x_dist = hex_width * width_scale
    y_dist = hex_width * height_scale

    # hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]
    # maps direction to change in x and y
    dir_dict = {(1, 0, -1): (x_dist, -y_dist),
                (1, -1, 0): (x_dist, y_dist),
                (0, -1, 1): (0, y_dist * 2),
                (-1, 0, 1): (-x_dist, y_dist),
                (-1, 1, 0): (-x_dist, -y_dist),
                (0, 1, -1): (0, -y_dist*2)
                }
    dirs = list(dir_dict.keys())

    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))

    x = 200
    y = 200

    screen.blit(hex_image, (x, y))
    for dir in dirs:
        delta_x, delta_y = dir_dict[dir]
        screen.blit(hex_image, (x + delta_x, y + delta_y))

    # screen.blit(hex_image, (0, hex_width * height_scale))

    # screen.blit(hex_image, (hex_width * width_scale, 0))
    # screen.blit(hex_image, (hex_width * width_scale, hex_width))
    # screen.blit(hex_image, (0, hex_width * height_scale + hex_width))

    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
