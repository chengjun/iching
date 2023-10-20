# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 14:19:41 2015

@author: chengjun
"""

import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import json
import pkg_resources
from collections import defaultdict
from datetime import date
from datetime import timedelta

def ichingDate(d):
    random.seed(d)
    print('Your birthday & your prediction time: ', str(d))

def sepSkyEarth(data):
    sky =  random.randint(1, data-2)
    earth = data - sky
    earth -= 1
    return sky , earth


def getRemainder(num):
    rm = num % 4
    if rm == 0:
        rm = 4
    return rm

def getChange(data):
    sky, earth = sepSkyEarth(data)
    skyRemainder = getRemainder(sky)
    earthRemainder = getRemainder(earth)
    change = skyRemainder + earthRemainder + 1
    data = data - change
    return sky, earth, change, data

def getYao(data):
    sky, earth, firstChange, data = getChange(data)
    sky, earth, secondChange, data = getChange(data)
    sky, earth, thirdChange, data = getChange(data)
    yao  = int(data/4)
    return yao, firstChange, secondChange, thirdChange

def sixYao():
    yao1 = getYao(data = 50 - 1)[0]
    yao2 = getYao(data = 50 - 1)[0]
    yao3 = getYao(data = 50 - 1)[0]
    yao4 = getYao(data = 50 - 1)[0]
    yao5 = getYao(data = 50 - 1)[0]
    yao6 = getYao(data = 50 - 1)[0]
    return[yao1, yao2, yao3, yao4, yao5, yao6]

def fixYao(num):
    if num == 6 or num == 9:
        print("there is a changing predict! Also run changePredict()")
    return num % 2


def changeYao(num):
    if num == 6:
        num = 1
    elif num == 9:
        num = 2
    num = num % 2
    return(num)

def fixPredict(pred):
    fixprd = [fixYao(i) for i in pred]
    fixprd = list2str(fixprd)
    return fixprd

def list2str(l):
    si = ''
    for i in l:
        si = si +  str(i)
    return si

def changePredict(pred):
    changeprd = [changeYao(i) for i in pred]
    changeprd = list2str(changeprd)
    return changeprd

def getPredict():
    pred = sixYao()
    fixPred = fixPredict(pred)
    if 6 in pred or 9 in pred:
        changePred = changePredict(pred)
    else:
        changePred = None
    return fixPred, changePred

def ichingName(now, future):
    dt = {'111111':u'乾','011111':u'夬','000000':u'坤','010001':u'屯','100010':u'蒙','010111':u'需','111010':u'讼','000010': u'师',
'010000':u'比','110111':u'小畜','111011':u'履','000111':u'泰','111000':u'否','111101':u'同人','101111':u'大有','000100':u'谦',
'001000':u'豫','011001':u'随','100110':u'蛊','000011':u'临','110000':u'观','101001':u'噬嗑','100101':u'贲','100000':u'剥',
'000001':u'复','111001':u'无妄','100111':u'大畜','100001':u'颐','011110':u'大过','010010':u'坎','101101':u'离','011100':u'咸',
'001110':u'恒','111100':u'遁','001111':u'大壮','101000':u'晋','000101':u'明夷','110101':u'家人','101011':u'睽','010100':u'蹇',
'001010':u'解','100011':u'损','110001':u'益','111110':u'姤','011000':u'萃','000110':u'升','011010':u'困','010110':u'井',
'011101':u'革','101110':u'鼎','001001':u'震','100100':u'艮','110100':u'渐','001011':u'归妹','001101':u'丰','101100':u'旅',
'110110':u'巽','011011':u'兑','110010':u'涣','010011':u'节','110011':u'中孚','001100':u'小过','010101':u'既济','101010':u'未济'}
    if future:
        name = dt[now] + ' & ' + dt[future]
    else:
        name = dt[now]
    return name

def ichingText(k):
    path = pkg_resources.resource_filename('iching', 'package_data.dat')
    dat = json.load(open(path, encoding = 'utf-8'))
    return dat[k]



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
    

def predict(birthday, today):
    # birthday and today could be 19990526 and 20201023
    day = str(birthday)+str(today)
    dayStr = day.replace('-', '').replace('/', '')
    dayInt = int(dayStr) 
    ichingDate(dayInt)
    fixPred, changePred   = getPredict()
    plotTransition(6, w = 15)
    guaNames = ichingName(fixPred, changePred) 
    fixText = ichingText(fixPred) # 
    if changePred:
        changeText = ichingText(changePred) # 
    else:
        changeText = None
    sepline1 = '\n                (O--__/\__--O)'
    sepline2 = '\n(-------------(O---- |__|----O)----------------)'
    sepline4 = '\n         (-------(O-/_--_\-O)-------)'
    sepline3 = '\n(-----------(O-----/-|__|-\------O)------------)'
    print(guaNames, '\n', u'本卦: ', fixText, sepline1,sepline2,sepline3,sepline4,'\n\n\n', u'变卦: ', changeText)
