

class Player :

    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.health = 100
        self.mana = 100

    def get_position(self) :
        return (self.x, self.y)
