
    # __init__(self, **kwargs)
    # self.damage = kwargs.get("damage")


class Spell():

    def __init__(self, channelTime, cooldown, damage, playerPos, directionInput, spellType):
        self.channelTime = channelTime
        self.cooldown = cooldown
        self.damage = damage
        self.playerPos = playerPos
        self.directionInput = directionInput
        self.type = spellType

class Blast(Spell):
    def __init__(self, pos, dir):
        super().__init__(0, 0, 1, pos, dir, 'basic')

        # pos = playerPos + (direction add)
        # heading = direction?

        #blast = Hitbox(self.damage, pos, heading, 1)
        #hitbox should probably do the drawing/updating part, too...

class Gust(Spell):
    def __init__(self, pos, dir):
        super().__init__(0, 2, 0, pos, dir, 'cantrip')
        #call player move function twice, passing (dir)

class Block(Spell):
    def __init__(self, pos, dir):
        super().__init__(0, 4, 0, pos, dir, 'cantrip')
        # add 1 temporary hp to player this turn only

class Sear(Spell):
    def __init__(self, pos, dir):
        super().__init__(0, 2, 1, pos, dir, 'cantrip')
        # see (or inherit from?) blast just with higher speed 

class Lance(Spell):
    def __init__(self, pos, dir):
        super().__init__(1, 4, 2, pos, dir, 'lesser')
        #make line of 1 turn hitboxes until hit a wall

        