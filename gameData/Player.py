from enum import Enum

from gameData.Entity import Entity


class PlayerState(Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    IDLE_DOWN = 4
    IDLE_RIGHT = 5
    IDLE_UP = 6
    IDLE_LEFT = 7


class Player(Entity):

    def draw(self, surface):
        pass

    def update(self, time_delta_in_ms):
        pass

    def has_changed(self):
        pass

    def __init__(self, position):
        self.position = position
        self.health = 100
        self.mana = 100

    def get_position(self):
        return self.position
