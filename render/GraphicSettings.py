from render import TileLibrary


class GraphicSettings:
    """
    A collection of various graphical parameters
    """

    def __init__(self, library_path="images/", sprite_size=(32, 32), screen_size=None):
        """
        library_path : The path to the tile image library
        sprite_size : A tuple giving the size of a tile in pixels.
        """
        self.library_path = library_path
        self.sprite_size = sprite_size
        self.sprite_width, self.sprite_height = sprite_size
        if screen_size is None:
            screen_size = (47 * sprite_size[0], 32 * sprite_size[1])
        self.screen_size = screen_size
        self.screen_width, self.screen_height = screen_size
        self.tile_library = TileLibrary.TileLibraryFromPath(library_path, sprite_size)
