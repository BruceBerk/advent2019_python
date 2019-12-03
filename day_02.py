"""Advent of Code 2019 - Day 02 - Intcode Computer"""

import IntCode as computer

test_prog_01 = [1,9,10,3,2,3,11,0,99,30,40,50]

"""
Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""
test_prog_02 = [1,0,0,0,99]
test_prog_03 = [2,3,0,3,99]
test_prog_04 = [2,4,4,5,99,0]
test_prog_05 = [1,1,1,4,99,5,6,0,99]


def read_file_as_list():
    """Read the data file and convert to a list of ints"""
    with open('data/input_02.txt') as inp:
        str_dat = inp.read()

    # convert string data into a list of ints
    prog = str_dat.split(',')
    return [int(x) for x in prog]


def part1():
    """Replace loc 1 and 2 in a program and run it"""
    ic = computer.IntCode()
    ic.load_prog_from_file('data/input_02.txt')
    ic.poke(1, 12)
    ic.poke(2, 2)
    ic.run_program()
    print("\nPart 1 result at addr 0 = {}".format(ic.peek(0)))


def part2(result):
    """Determine which noun (addr 1) and verb (addr 2) pair will yield a desired result in addr 0
       Noun and verb are between 0 and 99 inclusive"""
    prog = read_file_as_list()
    for noun in range(100):
        for verb in range(100):
            ic = computer.IntCode()
            ic.load_prog_from_buffer(prog)
            ic.poke(1, noun)
            ic.poke(2, verb)
            ic.run_program()
            if ic.peek(0) == result:
                return (100 * noun) + verb

    # if we got here, we never found our result so return -1
    return -1


def main():
    """Shout out to Kernighan & Ritchie"""
    ic = computer.IntCode()

    ic.load_prog_from_buffer(test_prog_01)
    ic.run_program()
    print("Test prog 01 result -", ic.memory)

    ic.clear_program()
    ic.load_prog_from_buffer(test_prog_02)
    ic.run_program()
    print("Test prog 02 result -", ic.memory)

    ic.clear_program()
    ic.load_prog_from_buffer(test_prog_03)
    ic.run_program()
    print("Test prog 03 result -", ic.memory)

    ic.clear_program()
    ic.load_prog_from_buffer(test_prog_04)
    ic.run_program()
    print("Test prog 04 result -", ic.memory)

    ic.clear_program()
    ic.load_prog_from_buffer(test_prog_05)
    ic.run_program()
    print("Test prog 05 result -", ic.memory)

    part1()

    # Day 2 what noun and verb resolve to 19690720?
    ans = part2(19690720)
    print("\nPart 2 result is {}".format(ans))


if __name__ == "__main__":
    main()
