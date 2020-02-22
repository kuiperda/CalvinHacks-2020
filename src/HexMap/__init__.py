from HexMap import hex, hex_render

class HexMap:
    def __init__(self, **kwargs):
        if (kwargs.get("xmax")):
            self._xmin = kwargs.get("xmin")
            self._xmax = kwargs.get("xmax")
        else:
            self._xmin = -1 * kwargs.get("xrad")
            self._xmax = kwargs.get("xrad")
        if (kwargs.get("ymax")):
            self._ymin = kwargs.get("ymin")
            self._ymax = kwargs.get("ymax")
        else:
            self._ymin = -1 * kwargs.get("yrad")
            self._ymax = kwargs.get("yrad")
        if (kwargs.get("zmax")):
            self._zmin = kwargs.get("zmin")
            self._zmax = kwargs.get("zmax")
        else:
            self._zmin = -1 * kwargs.get("zrad")
            self._zmax = kwargs.get("zrad")

        # width and height (in number of hexagons)
        self._width = abs(self._xmin) + abs(self._xmax) + 1
        self._height = abs(self._ymin) + abs(self._ymax) + 1

        self._renderer = hex_render.HexRenderer(size=kwargs.get("size"), width_scale=kwargs.get("width_scale"),
                                                height_scale=kwargs.get("height_scale"))

        self._startpix = None  # pixel coordinates for upper left hex

    def get_width(self):
        return self._width

    def get_width_px(self):
        return (self._width - 1) * self._renderer.get_x_dist()

    def get_height(self):
        return self._height

    def get_height_px(self):
        return (self._height - 1) * self._renderer.get_y_dist()*2

    def get_startpix(self):
        return self._startpix

    def get_hexsize(self):
        return self._renderer.get_size()

    def get_corner(self, cornertype):
        """

        :param cornertype:
        :return: coordinates (hex), coordinates (pixel)
        """
        if self._startpix is None:
            return None
        if cornertype == "NW":
            return hex.Hex(self._xmin, self._ymax, 0), self._startpix
        elif cornertype == "NE":
            return hex.Hex(self._xmax, 0, self._zmin), (self._startpix[0] + self.get_width_px(), self._startpix[1])
        elif cornertype == "SW":
            return hex.Hex(self._xmin, 0, self._zmax), (self._startpix[0], self._startpix[1] + self.get_height_px())
        elif cornertype == "SE":
            return hex.Hex(self._xmax, self._ymin, 0), (self._startpix[0] + self.get_width_px(), self._startpix[1] + self.get_height_px())

    def draw_hex_rect(self, startpix, image, surface):
        self._renderer.draw_hex_rect(self._width, self._height, startpix, image, surface)
        self._startpix = startpix

    def get_neighbor(self, start_hex, dir):
        """

        :param start_hex: starting hex
        :type start_hex: Hex (with x, y, z)
        :param dir: direction to move. 0 is upper right, and from there we go clockwise
        :return: tuple of new location, or None if the move is out of bounds
        """
        neighbor = hex.hex_neighbor(start_hex, dir)
        if self._xmin <= neighbor.q <= self._xmax \
                and self._ymin <= neighbor.r <= self._ymax \
                and self._zmin <= neighbor.s <= self._zmax:
            return neighbor
        # if we get here then neighbor is out of bounds
        return None
    
    def draw_neighbor(self, start_pix, dir, image, surface, offset=None):
        return self._renderer.draw_neighbor(start_pix, dir, image, surface, offset)
