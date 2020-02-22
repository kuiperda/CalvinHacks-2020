import hex

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

    def get_neighbor(self, start, dir):
        """

        :param start: starting hex
        :type start: Hex (with x, y, z)
        :param dir: direction to move. 0 is upper right, and from there we go clockwise
        :return: tuple of new location, or None if the move is out of bounds
        """
        start_hex = hex.Hex(*start)
        neighbor = hex.hex_neighbor(start_hex, dir)
        if self._xmin <= neighbor.q <= self._xmax \
                and self._ymin <= neighbor.r <= self._ymax \
                and self._zmin <= neighbor.s <= self._zmax:
            return neighbor
        # if we get here then neighbor is out of bounds
        return None
