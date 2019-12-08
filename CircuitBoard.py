"""Circuit board class"""


class CircuitBoard:
    """Implement a circuit board with 2 wires"""

    def trace_wire(self, wire):
        """Trace the path of the wire"""
        wire_coords = set()
        xpos = 0
        ypos = 0
        step_num = 0
        for path in wire:
            if path[0].upper() == 'R':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    xpos += 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)
            elif path[0].upper() == 'L':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    xpos -= 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)
            elif path[0].upper() == 'U':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    ypos += 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)
            elif path[0].upper() == 'D':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    ypos -= 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)

        return wire_coords

    def __init__(self, in_wires):
        self.wire1 = in_wires[0]
        self.wire2 = in_wires[1]

        # the set of points that each wire visits
        self.wire1_points = self.trace_wire(self.wire1)
        self.wire2_points = self.trace_wire(self.wire2)

    def man_dist(self, point):
        """Return the Manhatten distance for a given point to the origin"""
        return abs(point[0]) + abs(point[1])

    def shortest_path(self):
        """Return the wire crossing distance that is closest to the origin"""
        # where did the wires cross?
        crossed = self.wire1_points & self.wire2_points

        print(crossed)
        manhatten_dist = None
        for point in crossed:
            this_dist = self.man_dist(point)
            if manhatten_dist is None:
                manhatten_dist = this_dist
            elif this_dist < manhatten_dist:
                manhatten_dist = this_dist
        return manhatten_dist
