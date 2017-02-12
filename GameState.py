import Labyrinth, Player, Settings, GridTools, LabyrinthConstants
from MatrixTools import *

class GameState :

    def __init__(self,generator, settings) :
        self.labyrinth = generator.generate_labyrinth()
        self.settings = settings
        (x,y) = self.labyrinth.get_start()
        self.player = Player.Player( x*settings.sprite_width, y*settings.sprite_height)
        self.update_listeners = []

    def move_player(self, delta) :
        (sw,sh) = self.settings.sprite_size
        newpos = tuple(map(sum, zip( (self.player.x,self.player.y), delta)))
        pos_list = [newpos, vector_sum(newpos, (sw-1,0)), vector_sum(newpos, (0,sh-1)), vector_sum(newpos, (sw-1,sh-1))]
        for p in pos_list :
            (gx,gy) = GridTools.pixel_to_grid(p ,(sw,sh))
            if self.labyrinth.value_at(gx,gy) == LabyrinthConstants.LAB_WALL :
                return False
        (self.player.x, self.player.y) = newpos
        self.fire_player_moved()
        return True

    def add_update_listener(self, listener) :
        self.update_listeners.append(listener)

    def remove_update_listener(self, listener) :
        # Make sure to remove all occurrences and avoid errors if it doesnt exist
        update_listeners = [x for x in update_listeners if x != listener]

    def fire_player_moved(self) :
        for l in self.update_listeners :
            l.player_moved(self)


