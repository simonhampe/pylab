class Player:
    def __init__(self, position):
        self.position = position
        self.health = 100
        self.mana = 100

    def get_position(self):
        return self.position
