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
        surface.fill((255,255,255))
        player_pixel_pos = self.game_state.player.get_position()
        upper_left_pos = vector_sum( player_pixel_pos, (-self.radius * self.settings.sprite_width, -self.radius * self.settings.sprite_height))
        lower_right_pos = vector_sum( upper_left_pos, self.get_size())
        upper_left_pos = tuple([max(0,x) for x in upper_left_pos])
        lower_right_exceed = vector_sum( lower_right_pos, vector_neg(GridTools.grid_to_pixel(self.game_state.labyrinth.get_size(), self.settings.sprite_size))) 
        upper_left_pos = tuple(map( lambda x : x[0] if x[1] <= 0 else x[0] - x[1], zip( upper_left_pos, lower_right_exceed)))
        print("UL ", upper_left_pos)
        
        player_grid_pos = GridTools.pixel_to_grid(player_pixel_pos, self.settings.sprite_size)
        player_grid_upper_pixel = GridTools.grid_to_pixel(player_grid_pos, self.settings.sprite_size)
        if min(player_pixel_pos) == 0 or max(lower_right_exceed) > 0 :
            drawing_delta = (0,0)
        else :
            drawing_delta = vector_sum( player_grid_upper_pixel, vector_neg(player_pixel_pos))

        (start_x, start_y) = GridTools.pixel_to_grid( upper_left_pos, self.settings.sprite_size)
        end_x = min(self.game_state.labyrinth.width, start_x + self.side_length + 1)
        end_y = min(self.game_state.labyrinth.height, start_y + self.side_length + 1)
        draw_x = 0
        draw_y = 0
        for x_coord in range(start_x, end_x) :
            draw_y = 0
            for y_coord in range(start_y, end_y) :
                image = TileLibrary.map_value_to_sprite(self.settings.tile_library, self.game_state.labyrinth.value_at( x_coord, y_coord))
                pixel_coord = vector_sum( (draw_x, draw_y), drawing_delta)
                surface.blit(image, pixel_coord)
                draw_y += self.settings.sprite_height
            draw_x += self.settings.sprite_width
        #Draw player
        player_image = self.settings.tile_library.player
        player_draw_coord = vector_sum( player_pixel_pos, vector_neg(upper_left_pos))
        surface.blit(player_image, player_draw_coord)







