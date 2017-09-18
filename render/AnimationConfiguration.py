class AnimationConfiguration:
    """
    This class represents a configuration of an animated sprite.
    It maps states to their corresponding animation sequences
    and describes the animation speed.
    """

    def __init__(self, state_to_tile_mapping, initial_state, animation_step_in_ms):
        """
        Creates a new configuration
        :param state_to_tile_mapping: This contains a dictionary, mapping states (which can be arbitrary values)
        to lists of coordinate tuples in the tile matrix. While the sprite is in a certain state,
        it will cycle through the corresponding sequence of images.
        :param initial_state: The initial state of the sprite. Should be a key in state_to_tile_mapping
        :param animation_step_in_ms: After how many ms the next step in an animation cycle is taken.
        """
        self.state_to_tile_mapping = state_to_tile_mapping
        self.inital_state = initial_state
        self.animation_step_in_ms = animation_step_in_ms
