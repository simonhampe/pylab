class GridNode:
    def __init__(self, row, column, data):
        self.row = row
        self.column = column
        self.data = data
        self.n = None
        self.ne = None
        self.e = None
        self.se = None
        self.s = None
        self.sw = None
        self.w = None
        self.nw = None

    def connect(self, nw_node, w_node, n_node, ne_node):
        self.nw = nw_node
        if nw_node:
            nw_node.se = self
        self.w = w_node
        if w_node:
            w_node.e = self
        self.n = n_node
        if n_node:
            n_node.s = self
        self.ne = ne_node
        if ne_node:
            ne_node.sw = self

    def neighbours(self):
        return [x for x in [self.n, self.ne, self.e, self.se, self.s, self.sw, self.w, self.nw] if x]

    def straight_neighbours(self):
        return [x for x in [self.n, self.e, self.s, self.w] if x]

    def nb(self, direction):
        return {"n": self.n, "ne": self.ne, "e": self.e, "se": self.se, "s": self.s, "sw": self.sw, "w": self.w,
                "nw": self.nw}[direction]


class GridMatrix:
    def __init__(self, width, height, content_generator=None):
        self.width = width
        self.height = height
        self.row_heads = []
        self.col_heads = []
        self.row_tails = []
        self.col_tails = []
        nw_node = None
        w_node = None
        n_node = None
        ne_node = None
        for r in range(0, self.height):
            for c in range(0, self.width):
                node = GridNode(r, c, None if not content_generator else content_generator(r, c))
                if r == 0:
                    self.col_heads += [node]
                if r == self.height - 1:
                    self.col_tails += [node]
                if c == 0:
                    self.row_heads += [node]
                if c == self.width - 1:
                    self.row_tails += [node]
                node.connect(nw_node, w_node, n_node, ne_node)
                w_node = node
                nw_node = n_node
                n_node = ne_node
                if ne_node:
                    ne_node = ne_node.e
            w_node = None
            nw_node = None
            n_node = self.row_heads[-1]
            ne_node = n_node.e

    def node(self, row, column):
        rh = self.row_heads[row]
        for i in range(0, column):
            rh = rh.e
        return rh

    def square(self, from_row, to_row, from_col, to_col):
        ll = []
        for rh in self.row_heads[from_row: to_row + 1]:
            for i in range(0, to_col):
                if i >= from_col:
                    ll.append(rh)
                rh = rh.e
        return ll

    def rowwise_iterator(self):
        for rh in self.row_heads:
            node = rh
            while node:
                yield node
                node = node.e

    def colwise_iterator(self):
        for ch in self.col_heads:
            node = ch
            while node:
                yield node
                node = node.s

    def connected_components(self, selector, only_straight_nbs=False):
        """
        Computes connected components of the grid according to a certain selector.
        The selector returns True or False, when selector(node) is called.
        Connected component of "True" nodes are returned.
        If only_straight_nbs is True, then nodes are only connected to their straight neighbours.
        The result is returned as a list of lists.
        """
        result = []
        visited = []
        node_it = self.rowwise_iterator()
        node = next(node_it)
        while len(visited) < self.width * self.height:
            while node in visited:
                node = next(node_it)
            visited.append(node)
            if selector(node):
                queue = [node]
                component = [node]
                while len(queue) > 0:
                    front, queue = queue[0], queue[1:]
                    candidates = front.straight_neighbours() if only_straight_nbs else front.neighbours()
                    candidates = [c for c in candidates if c not in visited]
                    for c in candidates:
                        visited.append(c)
                        if selector(c):
                            component.append(c)
                            queue.append(c)
                result.append(component)
        return result
