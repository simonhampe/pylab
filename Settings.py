#map and sprite constants
image_path = "images/"

#Size of sprites in pixel
sprite_size = 32, 32
sprite_width, sprite_height = sprite_size

#Initial size of screen
screen_size = 47 * sprite_size[0], 32 * sprite_size[1]
screen_width, screen_height = screen_size

#Initial size of map
map_size_displayed = 45 * sprite_size[0], 30 * sprite_size[1]
map_width_displayed, map_height_displayed = map_size_displayed

#Initial map scaling factor
map_scaling_factor = 1

#Position of map
map_position = (sprite_size[0], sprite_size[1])

#Bar positions and sizes
standard_bar_size = sprite_size[0], int(map_size_displayed[1] * 3 / 4)
standard_bar_width, standard_bar_height = standard_bar_size

healthbar_position = map_position[0] + map_size_displayed[0] + sprite_size[0], map_position[1]
healthbar_size = standard_bar_size
healthbar_width, healtbar_height = healthbar_size

manabar_position = healthbar_position[0] + sprite_size[0] * 2, map_position[1]
manabar_size = standard_bar_size
manabar_width, manabar_height = manabar_size