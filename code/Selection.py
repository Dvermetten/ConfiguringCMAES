__author__ = 'Sander van Rijn <svr003@gmail.com>'

import numpy as np


def best(mu, population):
    """
        Given the population, return the mu best
    """

    pass


def singleBest(population):
    """
        Given the population, return the single best
    """

    pass


def onePlusOneSelection(population, new_population, t, parameters):
    """
        (1+1)-selection (with success history)
    """

    new_individual = new_population[0]
    individual = population[0]

    if new_individual.fitness < individual.fitness:
        best = new_population
        parameters.addToSuccessHistory(t, True)
    else:
        best = population
        parameters.addToSuccessHistory(t, False)

    return best