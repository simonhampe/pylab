class GridNode :

    def __init__(self, row, column, data) :
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

    def connect(self, nw_node, w_node, n_node, ne_node) :
        self.nw = nw_node
        if nw_node :
            nw_node.se = self
        self.w = w_node
        if w_node :
            w_node.e = self
        self.n = n_node
        if n_node :
            n_node.s = self
        self.ne = ne_node
        if ne_node :
            ne_node.sw = self

    def neighbours(self) :
        return [x for x in [self.n, self.ne, self.e, self.se, self.s, self.sw, self.w, self.nw] if x]


class GridMatrix :

    def __init__(self, width, height, content_generator = None) :
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
        for r in range(0,self.height) :
            for c in range(0,self.width) :
                node = GridNode(r,c, None if not content_generator else content_generator(r,c))
                if r == 0:
                    self.col_heads += [node]
                if r == self.height -1 :
                    self.col_tails += [node]
                if c == 0:
                    self.row_heads += [node]
                if c == self.width -1 :
                    self.row_tails += [node]
                node.connect(nw_node, w_node, n_node, ne_node)
                w_node = node
                nw_node = n_node
                n_node = ne_node
                if ne_node :
                    ne_node = ne_node.e
            w_node = None
            nw_node = None
            n_node = self.row_heads[-1]
            ne_node = n_node.e

    def rowwise_iterator(self) :
        for rh in self.row_heads :
            node = rh
            while node :
                yield node
                node = node.e

    def colwise_iterator(self) :
        for ch in self.col_heads :
            node = ch
            while node :
                yield node
                node = node.s


