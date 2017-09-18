from abc import ABC, abstractmethod


class Entity(ABC):
    """
    This abstract base class (ABC) represents a dynamic entity in the game, such as the player or an enemy.
    It defines the common methods that all these entities must implement to be managed during the event loop.
    """

    @abstractmethod
    def update(self, time_delta_in_ms):
        """
        This method is called every frame. It allows the entity to compute its new state.
        :param time_delta_in_ms: The time that has passed since the last frame, in milliseconds.
        """
        pass

    @abstractmethod
    def has_changed(self):
        """
        :return: Whether the entity has changed its internal state during the last call to update(...) and
        needs to be redrawn.
        """
        pass

    @abstractmethod
    def draw(self, surface):
        """
        This draw the entity onto a given surface into the top-left corner at position (0,0).
        :param surface: A pygame surface
        """
        pass


