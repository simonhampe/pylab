import Labyrinth, Player, Settings

class GameState :

    def __init__(self,generator) :
        self.labyrinth = generator.generate_labyrinth()
        (x,y) = self.labyrinth.get_start()
        self.player = Player.Player( x*Settings.sprite_width, y*Settings.sprite_height)
        self.update_listeners = []

    def move_player(self, delta) :
        self.player.x, self.player.y = map(sum, zip( (self.player.x,self.player.y), delta))
        self.fire_player_moved()

    def add_update_listener(self, listener) :
        self.update_listeners.append(listener)

    def remove_update_listener(self, listener) :
        # Make sure to remove all occurrences and avoid errors if it doesnt exist
        update_listeners = [x for x in update_listeners if x != listener]

    def fire_player_moved(self) :
        for l in self.update_listeners :
            l.player_moved(self)


