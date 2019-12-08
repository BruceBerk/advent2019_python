"""Circuit board class"""


class CircuitBoard:
    """Implement a circuit board with 2 wires"""

    def __init__(self, in_wires):
        self.wire1 = in_wires[0]
        self.wire2 = in_wires[1]

        # the set of points that each wire visits
        self.wire1_points, self.wire1_steps = self.trace_wire(self.wire1)
        self.wire2_points, self.wire2_steps = self.trace_wire(self.wire2)

    def trace_wire(self, wire):
        """Trace the path of the wire
        Do this by building a set of x-y points visited.
        For part 2 we need to know how many steps were taken to get to an intersection point.
        Calculated this by creating a dictionary where the key is the x-y point tuple,
        and the value is the number of steps taken to get there
        For part 2 we are returning a tuple: the coords set and the steps dict"""
        wire_coords = set()
        path_steps = {}
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
                    path_steps[new_coord] = step_num
            elif path[0].upper() == 'L':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    xpos -= 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)
                    path_steps[new_coord] = step_num
            elif path[0].upper() == 'U':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    ypos += 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)
                    path_steps[new_coord] = step_num
            elif path[0].upper() == 'D':
                wire_len = int(path[1:])
                for i in range(wire_len):
                    step_num += 1
                    ypos -= 1
                    new_coord = (xpos, ypos)
                    wire_coords.add(new_coord)
                    path_steps[new_coord] = step_num

        return (wire_coords, path_steps)

    def man_dist(self, point):
        """Return the Manhatten distance for a given point to the origin"""
        return abs(point[0]) + abs(point[1])

    def closest_intersect(self):
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

    def shortest_path(self):
        """Return the fewest number of steps to an intersection"""
        crossed = self.wire1_points & self.wire2_points

        fewest_steps = None
        for point in crossed:
            # how many steps in each wire to get to this point?
            steps1 = self.wire1_steps[point]
            steps2 = self.wire2_steps[point]
            if fewest_steps is None:
                fewest_steps = steps1 + steps2
            elif fewest_steps > (steps1+steps2):
                fewest_steps = steps1 + steps2
        return fewest_steps
