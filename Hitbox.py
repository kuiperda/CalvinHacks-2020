
class Hitbox():
    def __init__(self, damage, position, heading, speed):
        self.damage = damage
        self.position = position
        self.heading = heading
        self.speed = speed

    #def hit():
        #check if hitbox has hit a player (pos = playerPos)
        #deal damage
        #(probably) dissipate
        #(possibly) redraw next turn... call this again with updated position