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

    def draw_hex_circle(self, center, image, surface, **kwargs):
        """
        Draw a group of hexes starting with a hex that has a center at the coordinates given in center and radiating outward
        :param center: coordinates of the center of the center hex
        :param image: the hexagon image
        :param surface: the pygame surface to draw on
        :param **kwargs: TODO: minimum x and y, nrings, etc.
        :return:
        """
        coords = (center[0] - self._center_dist[0], center[1] - self._center_dist[1])
        surface.blit(image, coords)
        nrings = kwargs.get("nrings")
        n = 1
        ringstart = self.get_pix((0, 1, -1), coords)
        while True:
            surface.blit(image, ringstart)
            coords = ringstart
            for dir in self._dirs[:5]:
                for j in range(n):  # as we get to further rings, the rings get bigger
                    coords = self.get_pix(dir, coords)
                    surface.blit(image, coords)
            for k in range(n - 1):  # we already drew the first hex, so in the last direction do one fewer hexes
                coords = self.get_pix(self._dirs[-1], coords)
                surface.blit(image, coords)
            ringstart = self.get_pix((0, 1, -1), ringstart)  # go "up" a hex
            n += 1
            if n > nrings:
                break
