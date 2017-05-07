import GridTools
import LabyrinthConstants
import Player
from MatrixTools import *


class GameState:
    def __init__(self, generator, settings):
        self.labyrinth = generator.generate_labyrinth()
        self.settings = settings
        (x, y) = self.labyrinth.get_start()
        self.player = Player.Player(x * settings.sprite_width, y * settings.sprite_height)
        self.update_listeners = []

    def move_player(self, delta):
        (sw, sh) = self.settings.sprite_size
        newpos = vector_sum((self.player.x, self.player.y), delta)
        # Calculate all four corners of player icon
        pos_list = [newpos, vector_sum(newpos, (sw - 1, 0)), vector_sum(newpos, (0, sh - 1)),
                    vector_sum(newpos, (sw - 1, sh - 1))]
        # Check if any corner lies in a wall.
        for p in pos_list:
            (gx, gy) = GridTools.pixel_to_grid(p, (sw, sh))
            if self.labyrinth.value_at(gx, gy) == LabyrinthConstants.LAB_WALL:
                return
        (self.player.x, self.player.y) = newpos
        self.notify_player_moved()

    def add_update_listener(self, listener):
        self.update_listeners.append(listener)

    def remove_update_listener(self, listener):
        while listener in self.update_listeners:
            self.update_listeners.remove(listener)

    def notify_player_moved(self):
        for l in self.update_listeners:
            l.player_moved(self)
