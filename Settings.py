#map and sprite constants
image_path = "images/"

sprite_width = 32
sprite_height = sprite_width

screen_scale = 10

screen_width = screen_scale * 3
screen_heigth = screen_scale * 2

screen_dimensions = screen_width * sprite_width, screen_heigth * sprite_height

map_height = screen_heigth - 6
map_width = map_height


backgroundmap_size = (map_width * sprite_width, map_height * sprite_height)
backgroundmap_position = (sprite_width, sprite_height)
background_width, background_height = 1160, 689

healthbar_position = backgroundmap_position[0] + backgroundmap_size[0] + sprite_width, backgroundmap_position[1]
healthbar_dimensions = sprite_width, sprite_height * map_height * 3 / 4

manabar_position = healthbar_position[0] + sprite_width * 2, healthbar_position[1]
manabar_dimensions = healthbar_dimensions