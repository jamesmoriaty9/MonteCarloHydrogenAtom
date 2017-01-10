#!/usr/bin/env python
__author__ = 'Till'

import math
import numpy

"""
The task is to choose whether a new state is chosen or not depending on the new energystate.
If the energystate is lower than the previous the new state is automatically excepted
else the state is excepted by a given probability depending on the temperature
"""


def probability(temperature, energydifference):
    """
    :param temperature: the temperature at which the system is currently running. (in Kelvin)
    :param energydifference: the difference between the previous and new energy state. (in Hartrees (Atomic units))
    :return: a probability with which the new value will be accepted even if the energy is higher than the previous one
    """
    k = 3.16681*10**(-6)
    print numpy.exp(-energydifference/(temperature*k)), energydifference
    return numpy.exp(-energydifference/(temperature*k))


def metropolisalgorithm(temperature=1, energydifference=0):
    """
    :param temperature: the temperature at which the system is running in Kelvin
    :param energydifference: the difference between the previous and new energy state in Hartrees (Atomic units)
    :return:1 if the State should be passed and 0 if not
    """
    # accepted = probability(temperature, energydifference)
    # you can not define the prob. first, because the exponential function might give an overflow at 0 energydifference
    if energydifference <= 0:
        return 1
    elif numpy.random.choice(numpy.arange(1, 3), p=[probability(temperature, energydifference), 1-probability(temperature, energydifference)]) == 1:
        return 1
    else:
        return 0
