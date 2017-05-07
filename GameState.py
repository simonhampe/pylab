import GridTools
import LabyrinthConstants
import Player
from MatrixTools import *


class GameState:
    def __init__(self, generator, settings):
        self.labyrinth = generator.generate_labyrinth()
        self.settings = settings
        (x, y) = self.labyrinth.get_start()
        self.player = Player.Player((x * settings.sprite_width, y * settings.sprite_height))
        self.player_speed = 1
        self.max_player_speed = 5
        self.update_listeners = []

    def move_player(self, direction, speed=None):
        if speed is None:
            speed = self.player_speed

        delta = tuple([speed * x for x in list(direction.value)])
        (sw, sh) = self.settings.sprite_size
        newpos = list(vector_sum(self.player.get_position(), delta))
        # Calculate all four corners of player icon
        pos_list = [newpos, vector_sum(newpos, (sw - 1, 0)), vector_sum(newpos, (0, sh - 1)),
                    vector_sum(newpos, (sw - 1, sh - 1))]
        # Check if any corner lies in a wall.

        for p in pos_list:
            pos_grid = GridTools.pixel_to_grid(p, (sw, sh))
            if self.labyrinth.value_at(*pos_grid) == LabyrinthConstants.LAB_WALL:
                last_valid_grid = vector_sum(pos_grid, vector_neg(direction.value))
                last_valid_pixel = GridTools.grid_to_pixel(last_valid_grid, (sw, sh))
                newpos[direction.get_relevant_coordinate()] = last_valid_pixel[direction.get_relevant_coordinate()]

        self.player.position = tuple(newpos)
        self.notify_player_moved()

    def set_player_speed(self, new_player_speed):
        self.player_speed = new_player_speed
        self.check_player_speed()

    def change_player_speed_by(self, delta):
        self.player_speed += delta
        self.check_player_speed()

    def check_player_speed(self):
        self.player_speed = max(0, self.player_speed)
        self.player_speed = min(self.max_player_speed, self.player_speed)
        print(self.player_speed, self.player.position)

    def add_update_listener(self, listener):
        self.update_listeners.append(listener)

    def remove_update_listener(self, listener):
        while listener in self.update_listeners:
            self.update_listeners.remove(listener)

    def notify_player_moved(self):
        for l in self.update_listeners:
            l.player_moved(self)
