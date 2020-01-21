# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:06:58 2020

@author: setat
"""

"""To take the ditherer’s mean of n numbers, we want an iterative process
that gives us n numbers at each step. So at each step, we replace the
smallest number from the previous list of numbers with the geometric mean
of the previous numbers and the largest number with the arithmetic mean of
the numbers. - Evelyn Lamb"""
 
from scipy.stats import gmean
import numpy as np

trial = [5, 1, 20, 26]

def dither(a_list):
    """Take a list one step towards the ditherer's mean.
    
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
    dithered : list
        A copy of a_list, with the largest number replaced with the arithmetic
        mean, and the smallest number replaced with the geometric mean."""
    if sum(np.array(a_list) > 0) != len(a_list):
        raise Exception("Sorry, only positive number lists allowed.")
    a_mean = np.mean(a_list)
    g_mean = gmean(a_list)
    dithered = [g_mean] + sorted(a_list)[1:-1] + [a_mean]
    return (g_mean, a_mean, sorted(dithered))

dither(trial)
dither([1, -5])

def d_mean(a_list, places):
    """Take a list one step towards the ditherer's mean.
    
    Parameters
    ----------
    a_list : list
        A list of numbers.
    places : int
        Desired precision for how many decimal places the arithmetic and 
        geometric means should match to.
    
    Returns
    -------
    g_mean : float
        Geometric mean of the list
    a_mean : float
        Arithmetic mean of the list
    to_dither : list
        The final list, with a sufficiently close a-mean and g-mean"""
    to_dither = a_list
    a_mean = np.mean(to_dither)
    g_mean = gmean(to_dither)
    while round(a_mean, places) != round(g_mean, places):
        g_mean, a_mean, to_dither = dither(to_dither)
    return (g_mean, a_mean, sorted(to_dither))

d_mean(trial, 3)
