#!/usr/bin/python3
# Calculate the Z Scores of a set of data
# z = (X – μ) / σ
# X : Single Data Value
# μ : Population mean    -> μ = ( Σ Xi ) / N
# σ : Standard Deviatiom  -> σ = √ (Σ(Xi -μ )^2/N)
# N: Sample Count
import math
xData = [1, 2, 3, 4, 5]  # Your list of samples


def zScore(xData):
    """ Calculate the Z-Score of an array of data"""
    dev = stdDev(xData)
    print(dev)
    avg = popMean(xData)
    # print(avg)
    zscr = []
    for xi in xData:
        X = ((xi - avg) / dev)
        zscr.append(X)
    return zscr


def popMean(xData):
    sum = 0
    count = len(xData)
    for xi in xData:
        sum = sum + xi
    return sum/count


def stdDev(xData):
    dev = 0
    count = len(xData)
    sum = 0
    mean = popMean(xData)
    for xi in xData:
        sum = sum + ((xi - mean)**2)
    dev = math.sqrt(sum/count)
    return dev


print(zScore(xData))
# 