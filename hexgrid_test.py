from HexMap import hex_render
import pygame

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("hexgrid test")

    hex_image = pygame.image.load("HexMap/regular_hex.png")
    # scale image to half its original size
    hex_dims = (195, 169)  # (195, 169)
    hex_image = pygame.transform.scale(hex_image, hex_dims)

    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))

    x = 400
    y = 400

    hr = hex_render.HexRenderer(size=hex_dims[0])
    hr.draw_hex_circle((x, y), hex_image, screen, nrings=2)

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
