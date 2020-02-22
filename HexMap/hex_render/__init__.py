"""
For rendering hexes using Python. Created for CalvinHacks 2020 by Catherine DeJager.
Assumes hexes use the cube coordinate system described at https://www.redblobgames.com/grids/hexagons
"""

class HexRenderer:
    def __init__(self, **kwargs):
        self._size = kwargs.get("size")
        self._width_scale = kwargs.get("width_scale", 0.75)
        self._height_scale = kwargs.get("height_scale", 0.43)
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

    # def get_pix_from_hex(self, coords, center_coords):
    #     x_space = coords[0] - center_coords[0]
    #     y_space = coords[1] - center_coords[1]
    #     z_space = coords[2] - center_coords[2]
    #     direction = (int(x_space > 0) - int(x_space < 0), int(y_space > 0) - int(y_space < 0), int(z_space > 0) - int(z_space < 0))


    def draw_ring(self, center, radius, image, surface):
        coords = (center[0], center[1] + radius * 2*self._y_dist)
        for i in range(6):
            for j in range(radius):
                surface.blit(image, coords)
                coords = self.get_pix(self._dirs[i], coords)
        # start = center + radius * 2*self._y_dist
        # surface.blit(image, start)

    def draw_hex_circle(self, center, image, surface, **kwargs):
        """
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
