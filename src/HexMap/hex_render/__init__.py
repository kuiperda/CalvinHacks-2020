"""
For rendering hexes using Python. Created for CalvinHacks 2020 by Catherine DeJager.
Assumes hexes use the cube coordinate system described at https://www.redblobgames.com/grids/hexagons
"""

class HexRenderer:
    def __init__(self, **kwargs):
        self._size = kwargs.get("size")
        self._width_scale = kwargs.get("width_scale", 0.75)
        if not self._width_scale:
            self._width_scale = 0.75
        self._height_scale = kwargs.get("height_scale", 0.43)
        if not self._height_scale:
            self._height_scale = 0.43
        self._x_dist = self._size * self._width_scale
        self._y_dist = self._size * self._height_scale

        # get the x and y deltas (how far away to draw the neighbor hexagon) in pixels given the direction
        self._dir_delta = {(1, 0, -1): (self._x_dist, -self._y_dist),
                           (1, -1, 0): (self._x_dist, self._y_dist),
                           (0, -1, 1): (0, self._y_dist * 2),
                           (-1, 0, 1): (-self._x_dist, self._y_dist),
                           (-1, 1, 0): (-self._x_dist, -self._y_dist),
                           (0, 1, -1): (0, -self._y_dist*2)}
        self._dirs = list(self._dir_delta.keys())

        # distance from the upper-left point of the image (not of the hexagon) to the center
        self._center_dist = (self._x_dist * 2/3, self._y_dist)

    def get_delta(self, direction):
        return self._dir_delta[direction]

    def get_pix(self, direction, start):
        delta_x, delta_y = self._dir_delta[direction]
        return start[0] + delta_x, start[1] + delta_y

    def draw_neighbor(self, start, direction, image, surface, offset=None):
        delta_x, delta_y = self._dir_delta[direction]
        if offset:
            delta_x += offset[0]
            delta_y += offset[1]
        pixels = (start[0] + delta_x, start[1] + delta_y)
        surface.blit(image, pixels)
        return pixels

    def get_size(self):
        return self._size

    def get_x_dist(self):
        return self._x_dist

    def get_y_dist(self):
        return self._y_dist

    def draw_hex_rect(self, width, height, start, image, surface):
        """

        :param width: width (number horizontal)
        :param height: height (number vertical)
        :param start: starting coordinates
        :return:
        """
        start_x, start_y = start
        for row in range(height):
            for col in range(width):
                x = start_x + col * self._x_dist
                y = start_y + row * self._y_dist*2
                if col % 2 != 0:
                    y += self._y_dist
                surface.blit(image, (x, y))

    def draw_ring(self, center, radius, image, surface):
        # DOES NOT WORK
        coords = (center[0], center[1] + radius * 2*self._y_dist)
        for i in range(6):
            for j in range(radius):
                surface.blit(image, coords)
                coords = self.get_pix(self._dirs[i], coords)
        # start = center + radius * 2*self._y_dist
        # surface.blit(image, start)

    def draw_hex_circle(self, center, image, surface, **kwargs):
        """
        DOES NOT WORK

        Draw a group of hexes starting with a hex that has a center at the coordinates given in center and radiating outward
        :param center: coordinates of the center of the center hex
        :param image: the hexagon image
        :param surface: the pygame surface to draw on
        :param **kwargs: TODO: minimum x and y, nrings, etc.
        :return:
        """
        start = (center[0] - self._center_dist[0], center[1] - self._center_dist[1])
        surface.blit(image, start)
        radius = kwargs.get("radius")
        n = 1
        while True:
            self.draw_ring(start, n, image, surface)
            n += 1
            if n > radius:
                break
