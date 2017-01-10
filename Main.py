#!/usr/bin/env python
__author__ = 'Till'
import math
import Metropolis_Algorithm
import numpy
import pylab as plt


def wavefunctionsquare(radius, alpha):
    """
    :param alpha: a variable for my Ansatz
    :param radius: The position of the electron is defined by the radius
    :return:
    """
    return numpy.exp(-alpha*radius)*numpy.conjugate((numpy.exp(-alpha*radius)))


def integral(function, alpha, xmin=0, xmax=1, ymin=0, ymax=1, steps=1000):
    liste = [[(xmax-xmin)*x+xmin, (ymax-ymin)*y+ymin] for x, y in numpy.random.rand(steps, 2)]
    hit = 0
    for x, y in liste:
        if y < function(x, alpha):
            hit += 1.
    return (xmax-xmin)*(ymax-ymin)*hit/steps


def desity(radius, alpha):
    return wavefunctionsquare(alpha, radius)/(integral(wavefunctionsquare, alpha, 0, 5, 0, 1))


def intermediate(radius, alpha):
    return desity(radius, alpha)*((-alpha**2/2)+(alpha/radius)-(1/radius))


def energystate(alpha):
    return integral(intermediate, alpha, 0.1, 3, -3, 3)


#print energystate(7)
x = [i for i in numpy.arange(0,2,0.05)]
y = [energystate(i) for i in x]
print y
plt.plot(x,y)
plt.show()

def montecarlo(temperature, steps):
    """
    :param temperature: the temperature where the program will run the montecarlo algorithm
    :param steps: how many steps it will take
    :return: the groundstate energy of the hydrogen atom and the groundstate radius
    """
    randomwalker = numpy.random.randn(steps)
    alpha = 2
    for delr in randomwalker:
        energydiff = energystate(alpha + delr) - energystate(alpha)
        if Metropolis_Algorithm.metropolisalgorithm(temperature, energydiff) == 1:
            alpha += delr
            print alpha
    return "The groundstate energy is ", energystate(alpha), " at the alpha of ", alpha

#print montecarlo(1,1000)