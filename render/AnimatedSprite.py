class AnimatedSprite:
    """
    This class represents a sprite with various frames that make up an
    animation.
    Each animated sprite is tied to a TileMatrix, which contains all sprites
    needed for animation.
    The animated sprite can be in various states (e.g., up, down, left right, still),
    which determine the animation cycle.
    """

    def __init__(self, tile_matrix, animation_configuration):
        """
        Creates a new animated sprite.
        :param tile_matrix: The tile matrix which contains all relevant sprites.
        :param animation_configuration: The configuration for this animated sprite.
        """
        self.tile_matrix = tile_matrix
        self.configuration = animation_configuration
        self.current_state = self.configuration.initial_state
        self.current_tile_sequence = self.configuration.state_to_tile_mapping[self.state]
        self.current_tile_index = 0

    def update(self, time_delta_in_ms):
        """
        Updates the animation sequence state
        :param time_delta_in_ms: How much time has passed in ms since the last update.
        """
        animation_step = int(time_delta_in_ms / self.configuration.animation_step_in_ms)
        self.current_tile_index = (self.current_tile_index + animation_step) % len(self.current_tile_sequence)

    def draw(self, surface):
        """
        Draw the current animation image onto the given surface at (0,0).
        :param surface: A pygame surface
        """
        current_image = self.tile_matrix.get_tile(self.current_tile_sequence[self.current_tile_index])
        surface.blit(current_image, (0, 0))
