"""
Advent of Code 2019 - Day 03

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

"""
import CircuitBoard


def test1():
    """A few tests for the circuit board"""

    wire1 = ['R8','U5','L5','D3']
    wire2 = ['U7','R6','D4','L4']

    cboard = CircuitBoard.CircuitBoard([wire1, wire2])
    manhatten_dist = cboard.shortest_path()

    print("Shortest distance is {}".format(manhatten_dist))
    print("\nTest 1: expected 6 and got {}".format(manhatten_dist))

    wire3 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    wire4 = ['U62','R66','U55','R34','D71','R55','D58','R83']  # = distance 159

    cboard = CircuitBoard.CircuitBoard([wire3, wire4])
    manhatten_dist = cboard.shortest_path()

    print("Shortest distance is {}".format(manhatten_dist))
    print("\nTest 1: expected 159 and got {}".format(manhatten_dist))

    wire5 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire6 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']  # = distance 135

    cboard = CircuitBoard.CircuitBoard([wire5, wire6])
    manhatten_dist = cboard.shortest_path()

    print("Shortest distance is {}".format(manhatten_dist))
    print("\nTest 1: expected 135 and got {}".format(manhatten_dist))


def part1():
    """Part 1 - determine the intersection point that is closest to the central port"""
    test1()
    with open('data/input_03.txt') as inp:
        indat = inp.readlines()
        wire1 = (indat[0]).split(',')
        wire2 = (indat[1]).split(',')

        cboard = CircuitBoard.CircuitBoard([wire1, wire2])
        manhatten_dist = cboard.shortest_path()

        print("Shortest distance is {}".format(manhatten_dist))


def main():
    part1()


if __name__ == "__main__":
    main()
