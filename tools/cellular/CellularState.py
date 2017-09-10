class CellularState:
    """
    Describes the state and state history of a cell in a cellular automaton.
    In addition, every state has a "visited" boolean marker, which can be set.
    """

    def __init__(self, state):
        """
        Initializes a cell state
        :param state: Boolean, true if ALIVE
        """
        self.states = [state]
        self.visited = False

    def set_next_state(self, state):
        """
        Sets the state of this cell for the next iteration.
        This resets the visited marker to false.
        :param state: Boolean, true if alive
        """
        self.states.append(state)

    def get_state(self, iteration):
        """
        Returns the state of the given iteration.
        :param iteration: Iteration number. 0 means the initial state.
        :return: The corresponding state
        """
        if len(self.states) < iteration or iteration < 0:
            raise IndexError("Iteration " + iteration + " does not exist.")
        return self.states[iteration]

    def get_last_state(self):
        """
        :return: The state from the last iteration (or the initial state, if no iteration was performed).
        """
        return self.states[-1]

    def is_visited(self):
        """
        :return: Whether the visited marker is set to True
        """
        return self.visited

    def mark_as_visited(self):
        """
        Sets the visited marker to true
        """
        self.visited = True