#!/usr/bin/env python
__author__ = 'Till'

import math
import numpy



"""
The task is to choose whether a new state is chosen or not depending on the new Energystate.
If the Energystate is lower than the previous the new state is automatically excepted
else the state is excepted by a given Probability depending on the temperature
"""


def probability(temperature,energydifference):
    """
    :param temperature: the temperature at which the system is currently running in Kelvin
    :param energydifference: the difference between the previous and new energy state in Hartrees (Atomic units)
    :return: a probability with which the new value will be accepted even if the energy is higher than the previous one
    """
    k = 3.16681*10**(-6)
    return math.exp(-energydifference/(temperature*k))

def MetropolisAlgorithm(temperature=1,energydifference=0):
    """
    :param temperature:is the temperature at which the system is running in Kelvin
    :param energydifference: the difference between the previous and new energy state in Hartrees (Atomic units)
    :return:1 if the State should be passed and 0 if not
    """
    accepted = probability(temperature,energydifference)
    if energydifference <= 0:
        return 1
    elif numpy.random.choice(numpy.arange(1, 3), p=[ accepted,1-accepted])==1:
        return 1
    else:
        return 0
