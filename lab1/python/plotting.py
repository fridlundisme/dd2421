from PyQt5 import QtWidgets,uic
from pyqtgraph import PlotWidget, plot, QtGui,QtCore
import pyqtgraph as pg 
import sys 
import os 
import statistics as stat
import pruning
import time
import numpy as np
import matplotlib.pyplot as plt

def test():
    fig = plt.figure()
    x = np.array(pruning.getOliverData())
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 6)
    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                label='uplims=True, lolims=True')
    upperlimits = [True, False] * 5
    lowerlimits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
                label='subsets of uplims and lolims')
    plt.legend(loc='lower right')
    plt.show()

if __name__ == "__main__":
    fraction = np.array([0.3,0.4,0.5,0.6,0.7,0.8])
    start_time = time.time()
    error = np.array(pruning.getOliverData())
    
    print("\n---- %s [Oliver] seconds ----\n" % (time.time() - start_time))
    errorMean = np.array([None] * len(error))
    errorMedian = [None] * len(error)
    topMed = [None] * len(error)
    botMed = [None] * len(error)
    topMean = [None] * len(error)
    botMean = [None] * len(error)
    errMed = [topMed,botMed]
    errMean = [topMean, botMean]
    for i, x in enumerate(error):
        errorMean[i] = stat.mean(x)
        errorMedian[i] = stat.median(x)
        topMed[i] = abs(stat.median([y for y in x if y > errorMean[i]]) - errorMean[i])
        botMed[i] = abs(stat.median([y for y in x if y <= errorMean[i]]) - errorMean[i])

        topMean[i] = abs(stat.mean([y for y in x if y > errorMean[i]]) - errorMean[i])
        botMean[i] = abs(stat.mean([y for y in x if y <= errorMean[i]]) - errorMean[i])

    plt.errorbar(fraction,errorMean,yerr=errMean,color='#49abc2',fmt='--o')
    plt.xlabel('Fraction')
    plt.ylabel('Mean of correctly classified samples')
    plt.title('Fraction vs Mean Monk1')

    plt.show()

    plt.errorbar(fraction,errorMedian,yerr=errMed,color='red',fmt='--o')
    plt.xlabel('Fraction')
    plt.ylabel('Median of correctly classified samples')
    plt.title('Fraction vs Median Monk1')

    plt.show()