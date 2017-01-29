import Labyrinth, Player, Settings

class GameState :

    def __init__(self,generator) :
        self.labyrinth = generator.generate_labyrinth()
        (x,y) = self.labyrinth.get_start()
        self.player = Player.Player( x*Settings.sprite_width, y*Settings.sprite_height)


