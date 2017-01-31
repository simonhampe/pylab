import GridTools, TileLibrary
from MatrixTools import *

class PlayerViewRenderer :

    def __init__(self, game_state, radius, graphic_settings) :
        """
        game_state: A GameState object encoding the state of the game
        radius: Defines the size of the square displayed in grid units. Side length is 2*radius+1
        graphic_settings: Contains all graphical settings
        """
        self.game_state = game_state
        self.radius = max(radius,1)
        self.side_length = 2*self.radius+1
        self.settings = graphic_settings

    def get_size(self) :
        return (self.side_length * self.settings.sprite_width, self.side_length * self.settings.sprite_height)

    def draw(self, surface) :
        """
        Draws the player view on a given surface.
        Always starts drawing at (0,0)
        """
        player_pixel_pos = self.game_state.player.get_position()
        player_grid_pos = GridTools.pixel_to_grid(player_pixel_pos, self.settings.sprite_size)
        player_grid_upper_pixel = GridTools.grid_to_pixel(player_grid_pos, self.settings.sprite_size)
        drawing_delta = vector_sum( player_grid_upper_pixel, vector_neg(player_pixel_pos))
        start_x = max(0, player_grid_pos[0] - self.radius)
        start_y = max(1, player_grid_pos[1] - self.radius)
        end_x = min(self.game_state.labyrinth.width, start_x + self.side_length + 1)
        end_y = min(self.game_state.labyrinth.height, start_y + self.side_length + 1)
        for x_coord in range(start_x, end_x) :
            for y_coord in range(start_y, end_y) :
                image = TileLibrary.map_value_to_sprite(self.settings.tile_library, self.game_state.labyrinth.value_at( x_coord, y_coord))
                pixel_coord = vector_sum(GridTools.grid_to_pixel( (x_coord - start_x, y_coord - start_y), self.settings.sprite_size), drawing_delta)
                surface.blit(image, pixel_coord)
        #Draw player
        player_image = self.settings.tile_library.player
        player_draw_coord = vector_sum(GridTools.grid_to_pixel( (player_grid_pos[0] - start_x, player_grid_pos[1] - start_y), self.settings.sprite_size), drawing_delta)
        surface.blit(player_image, player_draw_coord)







