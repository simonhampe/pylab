from LabyrinthConstants import LAB_WALL, LAB_FLOOR
import random
from pygame.locals import Rect
from GridMatrix import GridMatrix
from Labyrinth import Labyrinth


class DungeonData:
    def __init__(self, data, valid):
        self.data = data
        self.valid = valid


"""
Contains the definition of a Labyrinth generator, which generates dungeon-style labyrinths
(i.e. lots of rectangular rooms with straight labyrinthine passages)
"""


class DungeonLabGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.min_room_dims = (int(width / 10), int(height / 10))
        self.max_room_dims = (int(width / 5), int(width / 5))
        avg_room_size = (self.min_room_dims[0] + self.max_room_dims[0]) * (
        self.min_room_dims[1] + self.max_room_dims[1]) * 1 / 4
        self.room_tries = int(width * height / (avg_room_size))
        self.boundary_buffer = 1
        self.room_boundary_buffer = 1

    def _count_alive_neighbours(self, node):
        return len([x for x in node.neighbours() if x.data.data == LAB_FLOOR])

    def _is_valid(self, node):
        return self._count_alive_neighbours(node) == 0

    def _build_corridors(self, GM):
        while True:
            # Find valid point
            current_point = None
            for node in GM.rowwise_iterator():
                if node.data.valid:
                    current_point = node
                    break
            if not current_point:
                return
            Direction = None
            while current_point:
                candidates = [x for x in ["n", "e", "s", "w"] if current_point.nb(x).data.valid]
                for nb in current_point.straight_neighbours():
                    nb.data.valid = False

                current_point.data = DungeonData(LAB_FLOOR, False)
                # Pick a random neighbour (or stop if there is no valid neighbour)
                if len(candidates) == 0:
                    current_point = None
                else:
                    if Direction and Direction in candidates and random.randint(0, 100) <= 75:
                        current_point = current_point.nb(Direction)
                    else:
                        Direction = random.choice(candidates)
                        current_point = current_point.nb(Direction)

    def _cleanup_corridors(self, GM):
        def selector(node):
            return node.data.data == LAB_FLOOR

        comps = GM.connected_components(selector, True)
        bigcomps = []
        # Remove small corridors
        for c in comps:
            if len(c) < 10:
                for nd in c:
                    nd.data.data = LAB_WALL
            else:
                bigcomps.append(c)
        # Find dead ends for each component
        dead_ends = []
        for c in bigcomps:
            bc_ends = []
            for nd in c:
                if len([x for x in c.straight_neighbours() if x.data.data = LAB_FLOOR]) <= 1:
                    bc_ends.append(nd)
            dead_ends.append(bc_ends)

    def generate_labyrinth(self):
        roomlist = []
        for t in range(self.room_tries):
            rlft = random.randint(self.boundary_buffer, self.width - self.min_room_dims[0] - self.boundary_buffer - 1)
            rtop = random.randint(self.boundary_buffer, self.height - self.min_room_dims[1] - self.boundary_buffer - 1)
            rwdt = random.randint(self.min_room_dims[0] - 1,
                                  min(self.max_room_dims[0], self.width - rlft - self.boundary_buffer) - 2)
            rhgt = random.randint(self.min_room_dims[1] - 1,
                                  min(self.max_room_dims[1], self.height - rtop - self.boundary_buffer - 2))
            nextroom = Rect(rlft, rtop, rwdt, rhgt)
            if nextroom.collidelist(roomlist) == -1:
                roomlist += [nextroom]

        def GridFiller(r, c):
            validity = True
            if not Rect(self.boundary_buffer, self.boundary_buffer, self.width - 2 * self.boundary_buffer,
                        self.height - 2 * self.boundary_buffer).collidepoint(c, r):
                return DungeonData(LAB_WALL, False)
            for rm in roomlist:
                if rm.collidepoint(c, r):
                    return DungeonData(LAB_FLOOR, False)
                if validity:
                    if Rect(rm.left - 1, rm.top - 1, rm.width + 2, rm.height + 2).collidepoint(c, r):
                        validity = False
            return DungeonData(LAB_WALL, validity)

        GM = GridMatrix(self.width, self.height, GridFiller)
        self._build_corridors(GM)
        self._cleanup_corridors(GM)
        rdict = {}
        for node in GM.rowwise_iterator():
            if node.data.data == LAB_FLOOR:
                rdict[node.column, node.row] = LAB_FLOOR
        start_point, end_point = (0, 0), (0, 0)
        # start_point = random.choice(list(rdict))
        # end_point = random.choice(list(rdict))


        return Labyrinth(self.width, self.height, start_point, rdict)
