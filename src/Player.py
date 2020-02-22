class Player:

    def __init__(self, **kwargs):
        self.hp = kwargs.get("hp")
        self.position = kwargs.get("position")
        self.pixels = kwargs.get("pixels")
        self.spells = kwargs.get("spells")
        self.image = kwargs.get("image")

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_image(self):
        return self.image

    def get_pixels(self):
        return self.pixels

    def set_pixels(self, pixels):
        self.pixels = pixels
