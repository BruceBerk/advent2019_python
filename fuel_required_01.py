"""fuel_required_01 - calculate fuel required to launch a given mass
Calculated as mass divided by 3 rounded down, less 2
Using math.floor() to round down
"""

import math


def fuel_required(mass):
    """Return fuel required for stated mass"""
    return (math.floor(mass/3)) - 2

def fuel_required_extra(mass):
    """Include fuel required for the fuel"""
    module_fuel = fuel_required(mass)
    needed_extra_fuel = 0
    extra_fuel = fuel_required(module_fuel)
    while extra_fuel > 0:
        needed_extra_fuel += extra_fuel
        extra_fuel = fuel_required(extra_fuel)
    return module_fuel + needed_extra_fuel
