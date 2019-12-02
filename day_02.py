"""Advent of Code 2019 - Day 02 - Intcode Computer"""

import intcode_02 as amiga

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


def main():
    """Shout out to Kernighan & Ritchie"""
    new_memory = amiga.run_program(test_prog_01)
    print("Test prog 01 result -", new_memory)

    new_memory = amiga.run_program(test_prog_02)
    print("Test prog 02 result -", new_memory)

    new_memory = amiga.run_program(test_prog_03)
    print("Test prog 03 result -", new_memory)

    new_memory = amiga.run_program(test_prog_04)
    print("Test prog 04 result -", new_memory)

    new_memory = amiga.run_program(test_prog_05)
    print("Test prog 05 result -", new_memory)

    with open('data/input_02.txt') as inp:
        str_dat = inp.read()

    # convert string data into a list of ints
    prog_01 = str_dat.split(',')
    prog_01 = [int(x) for x in prog_01]

    # resolve the 1202 alarm and run the program
    prog_01[1] = 12
    prog_01[2] = 2

    print("Program has {} items".format(len(prog_01)))

    prog_run = amiga.run_program(prog_01)
    print("\nResult in addr 0 = {}".format(prog_run[0]))


if __name__ == "__main__":
    main()
