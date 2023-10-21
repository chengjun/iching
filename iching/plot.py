# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 14:19:41 2015

@author: chengjun
"""

import matplotlib.cm as cm
import matplotlib.pyplot as plt

def plotTransition(N, w):
    changes = {}
    for i in range(N):
        sky, earth, firstChange, data = getChange(data = 50 -1)
        sky, earth, secondChange, data = getChange(data)
        sky, earth, thirdChange, data = getChange(data)
        changes[i]=[firstChange, secondChange, thirdChange, data/4]

    ichanges = changes.values()

    firstTransition = defaultdict(int)
    for i in ichanges:
        firstTransition[i[0], i[1]]+=1

    secondTransition = defaultdict(int)
    for i in ichanges:
        secondTransition[i[1], i[2]]+=1

    thirdTransition = defaultdict(int)
    for i in ichanges:
        thirdTransition[i[2], i[3]]+=1

    cmap = cm.get_cmap('Accent_r', len(ichanges))

    for k, v in firstTransition.items():
        plt.plot([1, 2], k, linewidth = v*w/N)
    for k, v in secondTransition.items():
        plt.plot([2, 3], k, linewidth = v*w/N)
    for k, v in thirdTransition.items():
        plt.plot([3, 4], k, linewidth = v*w/N)
    plt.xlabel(u'Time')
    plt.ylabel(u'Changes')