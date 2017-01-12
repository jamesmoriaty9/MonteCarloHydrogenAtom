#!/usr/bin/env python
__author__ = 'Till'
import math
import Metropolis_Algorithm
import numpy
import pylab as plt
import Energycalculations



Alpha = [i for i in numpy.arange(0,100,0.5)]
Energy = []
for i in Alpha:
    Energy.append(Energycalculations.energystate(i))
    print i/200.*100, "% done"
plt.plot(Alpha, Energy, "o")
plt.show()
"""
def montecarlo(temperature, bigsteps, smallsteps, alpha=100):
    bigrandomwalker = [x*2-1 for x in numpy.random.rand(bigsteps)]
    smallrandomwalker = [x/50 - 0.01 for x in numpy.random.rand(smallsteps)]
    enernew = Energycalculations.energystate(alpha)
    alphalist = []
    for step, delr in enumerate(bigrandomwalker):
        enerold = enernew
        enernew = Energycalculations.energystate(alpha + delr)
        energydiff = enernew - enerold
        if Metropolis_Algorithm.metropolisalgorithm(temperature, energydiff) == 1:
            alpha += delr
            alphalist.append(alpha)
            print alpha, step
    for step, delr in enumerate(smallrandomwalker):
        enerold = enernew
        enernew = Energycalculations.energystate(alpha + delr)
        energydiff = enernew - enerold
        if Metropolis_Algorithm.metropolisalgorithm(temperature, energydiff) == 1:
            alpha += delr
            alphalist.append(alpha)
            print alpha
    alphamean = sum(alphalist[-50:])/50
    return "The groundstate energy is ", Energycalculations.energystate(alphamean), " at the alpha of ", alphamean

print montecarlo(10, 100, 1000, 40)
"""