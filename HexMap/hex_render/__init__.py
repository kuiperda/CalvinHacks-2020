"""
For rendering hexes using Python. Created for CalvinHacks 2020 by Catherine DeJager.
Assumes hexes use the cube coordinate system described at https://www.redblobgames.com/grids/hexagons
"""

class HexRenderer:
    def __init__(self, **kwargs):
        self._size = kwargs.get("size")
        self._width_scale = kwargs.get("width_scale", 0.86)
        self._height_scale = kwargs.get("height_scale", 0.5)
        self._x_dist = self._size * self._width_scale
        self._y_dist = self._size * self._height_scale
        # get the x and y deltas (how far away to draw the neighbor hexagon) in pixels given the direction
        self.delta_dict = {(1, 0, -1): (self._x_dist, -self._y_dist),
                (1, -1, 0): (self._x_dist, self._y_dist),
                (0, -1, 1): (0, self._y_dist * 2),
                (-1, 0, 1): (-self._x_dist, self._y_dist),
                (-1, 1, 0): (-self._x_dist, -self._y_dist),
                (0, 1, -1): (0, -self._y_dist*2)}

    def get_delta(self, direction):
        return self.delta_dict[direction]

    def get_pix(self, direction, start):
        delta_x, delta_y = self.delta_dict[direction]
        return start[0] + delta_x, start[1] + delta_y
