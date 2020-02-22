
class Spell():

    def __init__(self, **kwargs):
        self.channelTime = kwargs.get("channelTime")
        self.cooldown = kwargs.get("cooldown")
        self.image = kwargs.get("image")
        self.pixels = kwargs.get("pixels")
        self.position = kwargs.get("position")
        self.spells = kwargs.get("spells")
        self.damage = kwargs.get("damage")

    def get_channelTime(self):
        return self.channelTime

    def set_channelTime(self, newVal):
        self.channelTime = newVal

    def get_cooldown(self):
        return self.cooldown

    def set_cooldown(self, newVal):
        self.cooldown = newVal

    def get_image(self):
        return self.image

    def set_image(self, newVal):
        self.image = newVal

    def get_pixels(self):
        return self.pixels

    def set_pixels(self, newVal):
        self.pixels = newVal

    def get_position(self):
        return self.position

    def set_position(self, newVal):
        self.position = newVal

    def get_spells(self):
        return self.spells

    def set_spells(self, newVal):
        self.spells = newVal

    def get_damage(self):
        return self.damage

    def set_damage(self, newVal):
        self.damage = newVal


class Blast(Spell):
    def __init__(self, **kwargs):
        super().__init__()

    def cast(self, position, direction):
        return self

    def onCollision(self): 
        #player.hp -= 1
        # return collision image
        pass

class Lance(Spell):
    def __init__(self, **kwargs):
        super().__init__()

    def cast(self, position, direction):
        return self

    def onCollision(self): 
        # damage player
        # return collision image
        pass

class Gust(Spell):
    def __init__(self, **kwargs):
        super().__init__()

    def cast(self, position, direction):
        return self

    def onCollision(self): 
        # damage player
        # return collision image
        pass

class Block(Spell):
    def __init__(self, **kwargs):
        super().__init__()

    def cast(self, position, direction):
        return self

    def onCollision(self): 
        # damage player
        # return collision image
        pass

class Sear(Spell):
    def __init__(self, **kwargs):
        super().__init__()

    def cast(self, position, direction):
        return self

    def onCollision(self): 
        # damage player
        # return collision image
        pass
