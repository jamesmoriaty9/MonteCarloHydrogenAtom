#!/usr/bin/env python
__author__ = 'Till'

import numpy


def wavefunctionsquare(radius, alpha):
    """
    :param alpha: a variable for my Ansatz
    :param radius: The position of the electron is defined by the radius
    :return:
    """
    return numpy.exp(-alpha*radius)*numpy.conjugate((numpy.exp(-alpha*radius)))


def integral(function, alpha, xmin=0, xmax=1, ymin=0, ymax=1, steps=5000):
    liste = [[(xmax-xmin)*x+xmin, (ymax-ymin)*y+ymin] for x, y in numpy.random.rand(steps, 2)]
    poshit = 0
    neghit = 0
    posdot = 0
    negdot = 0
    for x, y in liste:
        if y > 0:
            posdot += 1
        else:
            negdot += 1
        if 0 < function(x, alpha):
            if y < function(x, alpha) and y > 0:
                poshit += 1.
        elif 0 > function(x, alpha):
            if y > function(x, alpha) and y < 0:
                neghit += 1.
    if ymin < 0:
        return (xmax-xmin)*(ymax)*poshit/posdot-((xmax-xmin)*(0-ymin)*neghit/negdot)
        # achtung negdot kann 0 sein wenn ymin nahe 0
    else:
        return (xmax-xmin)*(ymax-ymin)*poshit/steps


def intermediate(radius, alpha):
    return wavefunctionsquare(alpha, radius)*((-alpha**2/2)+(alpha/radius)-(1/radius))


def energystate(alpha):
    return 1/(integral(wavefunctionsquare, alpha, 0, 5))*integral(intermediate, alpha, 0.001, 5, -3, 3)
