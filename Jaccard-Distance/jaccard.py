
'''
Created 2014

@author: Kulsoom Abdullah

Python 2.7
'''
import math

# This python code has functions needed to calculate the Jaccard index (or
# similiarity) which is used as a measure of distance.
# https://en.wikipedia.org/wiki/Jaccard_index

# Generally, the set functions in Python, such as intersection and union run
# quickly, but I was having very long running times.
# Using python profile to find out the bottleneck, I found it was the set
# operation, specifically for when I had a very large set of items in the
# 400,000 and above length, being compared.  Using this code below sped
# things up considerably.

# The functions take x and y - the two sets being compared


def intersect(x, y):  # faster than set intersection method
    incommon = 0.0
    if len(x) < len(y):
        for ip in x:
            if ip in y:
                incommon += 1
    if len(y) <= len(x):
        for ip in y:
            if ip in x:
                incommon += 1
    intersection = incommon
    return intersection


def jaccard(x, y):
    itxn = intersect(x, y)
    union = len(x) + len(y) - itxn
    return 1.0 * (itxn / union)

# this is a "modified jaccard"  One can use a sigmoid factor to normalize the
# jaccard value for when you have a wide variety of set lengths you are
# calculating distances for. This is commented out.
# The other method I had used for when comparing sets of
# a small to a comparible large set, for example, 100 elements to 1000, if
# that 100 was contained in the 1000, then I wanted the distance to be a
# value of 1.  This is how the factor of dividing by the minimum length of
# the two sets being compared was decided on.


def jaccard_mod(x, y):
    itxn = intersect(x, y)
    # sig_val = sig_factor(x,y)
    return 1.0 * (itxn / min(len(x), len(y)))
    # return 1.0*(itxn/min(len(x),len(y)) )*sig_val

# for most purposes, comment out the if cIPflag condition below.  This was
# a boolean I used to decide whether to normalize jaccard or not.


def jaccard_dist(x, y, cIPflag):
    # only using sigmoid with cIP calc
    if cIPflag:
        return 1.0 - (jaccard(x, y) * sig_factor(x, y))
    else:
        return 1.0 - jaccard(x, y)


def sig_factor(x, y):
    # factor to increase similiarity for more IP addresses
    alpha = 14
    minIPset = min(len(x), len(y))
    return 1 / (1 + math.exp(alpha - minIPset))
