"""Advent of Code 2019 Day 01: Fuel Counter Upper"""

import fuel_required_01 as fr

TEST_DATA = [12, 14, 1969, 100756]
TEST_ANSWER = [2, 2, 654, 33583]


def test_run():
    for i in range(len(TEST_DATA)):
        print("Mass {} - expected {} - got {}".format(TEST_DATA[i], TEST_ANSWER[i], fr.fuel_required(TEST_DATA[i])))


if __name__ == "__main__":
    test_run()

    # read the data file into a list
    mass_data = []
    with open("data/input_01.txt") as inp:
        mass_data = inp.readlines()

    # use a list comprehension to get the fuel required for each mass in the list
    ans_list = [fr.fuel_required(int(x)) for x in mass_data]

    module_fuel = sum(ans_list)
    print("\nTotal fuel required is {}".format(module_fuel))

    # now get the fuel needed taking into account the weight of the fuel
    extra_ans_list = [fr.fuel_required_extra(int(x)) for x in mass_data]
    extra_module_fuel = sum(extra_ans_list)

    print("\nPart 2 fuel required is {}".format(extra_module_fuel))
