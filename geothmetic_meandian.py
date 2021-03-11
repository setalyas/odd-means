# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 03:10:11 2021

@author: setat

Geothmetic meandian: calculate the arithmetic mean, median, and geometric mean
for a list of numbers, until they converge.

From https://xkcd.com/2435/
"""

from scipy.stats import gmean
import numpy as np

trial = np.array([1, 1, 2, 3, 5])

print(np.mean(trial))
print(np.median(trial))
print(gmean(trial))


def gmdn_step(a_list):
    """Take a list one step towards the geothmetic meandian.
    
    Parameters
    ----------
    a_list : list
        A list of positive numbers.
    
    Returns
    -------
    g_mean : float
        Geometric mean of the list
    a_mean : float
        Arithmetic mean of the list
    medn : float
        Median of the list
    gmdned : list
        A list of g_mean, a_mean, and medn"""
    if sum(np.array(a_list) > 0) != len(a_list):
        raise Exception("Sorry, only positive number lists allowed.")
    a_mean = np.mean(a_list)
    g_mean = gmean(a_list)
    medn = np.median(a_list)
    gmdned = np.array([g_mean, a_mean, medn])
    return sorted(gmdned)

print(gmdn_step(trial))
print(gmdn_step(gmdn_step(trial)))

def gmdn(a_list, places):
    """Take a list to its geothmethic meandian.
    
    Parameters
    ----------
    a_list : list
        A list of numbers.
    places : int
        Desired precision for how many decimal places the averages should match
        to.
    
    Returns
    -------
    geothmetic_meandian : float
        The convergence of the averages"""
    counter = 0
    gmdned = a_list
    while max(gmdned) - min(gmdned) > 10 ** (-places):
        gmdned = gmdn_step(gmdned)
        counter += 1
    print("Converged within {} steps.".format(counter))
    return gmdned

gmdn(trial, 3)
