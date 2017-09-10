class CellularState:
    """
    Describes the state and state history of a cell in a cellular automaton
    """

    def __init__(self, state):
        """
        Initializes a cell state
        :param state: Boolean, true if ALIVE
        """
        self.states = [state]

    def set_next_state(self, state):
        """
        Sets the state of this cell for the next iteration
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
