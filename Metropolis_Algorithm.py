#!/usr/bin/env python
__author__ = 'Till'

import math
import scipy


"""
The task is to choose whether a new state is chosen or not depending on the new Energystate.
If the Energystate is lower than the previous the new state is automatically excepted
else the state is excepted by a given Probability depending on the temperature
"""


def probability(temperature,energydifference):
    return math.exp(-energydifference/(temperature))