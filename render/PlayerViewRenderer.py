from render import TileLibrary
from render.AnimationConfiguration import AnimationConfiguration
from render.TileMatrix import TileMatrix
from tools import GridTools
from tools.MatrixTools import *


class PlayerViewRenderer:
    def __init__(self, game_state, radius, graphic_settings):
        """
        game_state: A GameState object encoding the state of the game
        radius: Defines the size of the square displayed in grid units. Side length is 2*radius+1
        graphic_settings: Contains all graphical settings
        """
        self.game_state = game_state
        self.radius = max(radius, 1)
        self.side_length = 2 * self.radius + 1
        self.settings = graphic_settings
        self.player_tiles = TileMatrix('images/player_sprites.png', (24, 32))
        self.player_config = AnimationConfiguration(player_tile_mapping, player_initial_state, player_animation_step)

    def get_size(self):
        return self.side_length * self.settings.sprite_width, self.side_length * self.settings.sprite_height

    def draw(self, surface):
        """
        Draws the player view on a given surface.
        Always starts drawing at (0,0)
        """
        surface.fill((255, 255, 255))
        maxdim = (self.game_state.labyrinth.width * self.settings.sprite_width,
                  self.game_state.labyrinth.height * self.settings.sprite_height)
        player_pixel_pos = tuple(map(int, self.game_state.player.get_position()))
        upper_left_pos = list(vector_sum(player_pixel_pos, (
            -self.radius * self.settings.sprite_width, -self.radius * self.settings.sprite_height)))
        lower_right_pos = list(vector_sum(upper_left_pos, self.get_size()))
        for i in range(0, 2):
            if upper_left_pos[i] < 0:
                lower_right_pos[i] -= upper_left_pos[i]
                upper_left_pos[i] = 0
            if lower_right_pos[i] > maxdim[i]:
                upper_left_pos[i] -= (lower_right_pos[i] - maxdim[i])
                lower_right_pos[i] = maxdim[i]

        upper_left_grid = GridTools.pixel_to_grid(upper_left_pos, self.settings.sprite_size)
        upper_left_outside_pixel = GridTools.grid_to_pixel(upper_left_grid, self.settings.sprite_size)
        drawing_delta = vector_sum(upper_left_outside_pixel, vector_neg(upper_left_pos))

        (start_x, start_y) = upper_left_grid
        end_x = min(self.game_state.labyrinth.width, start_x + self.side_length + 1)
        end_y = min(self.game_state.labyrinth.height, start_y + self.side_length + 1)
        draw_x = 0
        for x_coord in range(start_x, end_x):
            draw_y = 0
            for y_coord in range(start_y, end_y):
                image = TileLibrary.map_value_to_sprite(self.settings.tile_library,
                                                        self.game_state.labyrinth.value_at(x_coord, y_coord))
                pixel_coord = vector_sum((draw_x, draw_y), drawing_delta)
                surface.blit(image, pixel_coord)
                draw_y += self.settings.sprite_height
            draw_x += self.settings.sprite_width
        # Draw player
        player_image = self.settings.tile_library.player
        player_draw_coord = vector_sum(player_pixel_pos, vector_neg(upper_left_pos))
        surface.blit(player_image, player_draw_coord)
