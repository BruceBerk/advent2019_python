"""fuel_required_01 - calculate fuel required to launch a given mass
Calculated as mass divided by 3 rounded down, less 2
Using math.floor() to round down
"""

import math


def fuel_required(mass):
    return (math.floor(mass/3)) - 2
