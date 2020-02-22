from HexMap import hex_render
import pygame

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("hexgrid test")

    hex_image = pygame.image.load("HexMap/regular_hex.png")
    # scale image to half its original size
    hex_dims = (390 // 3, 338 // 3)  # (195, 169)
    hex_image = pygame.transform.scale(hex_image, hex_dims)

    screen = pygame.display.set_mode((800, 1000))
    screen.fill((255, 255, 255))

    hr = hex_render.HexRenderer(size=hex_dims[0])
    # hr.draw_hex_circle((x, y), hex_image, screen, radius=2)
    hr.draw_hex_rect(7, 7, (40, 150), hex_image, screen)

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
