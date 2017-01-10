#!/usr/bin/env python
__author__ = 'Till'
import math
import Metropolis_Algorithm
import numpy


"""here you can see that the implementation of other pythonscripts within the main script works perfectly :)"""
#print Metropolis_Algorithm.metropolisalgorithm(1000000, 1), Metropolis_Algorithm.probability(1000000, 1)

def energystate(radius):
    """
    :param radius: the radius where the energystate will be calculated
    :return: the energystate of the atom
    """
    return -0.5*math.log(radius)


def montecarlo(temperature, steps):
    """
    :param temperature: the temperature where the program will run the montecarlo algorithm
    :param steps: how many steps it will take
    :return: the groundstate energy of the hydrogen atom and the groundstate radius
    """
    randomwalker = numpy.random.randn(steps)
    radius = 2
    for delr in randomwalker:
        energydiff = energystate(radius + delr) - energystate(radius)
        if Metropolis_Algorithm.metropolisalgorithm(temperature, energydiff) == 1:
            radius += delr
    return "The groundstate energy is ", energystate(radius), " at the radius of ", radius

print montecarlo(100, 10)