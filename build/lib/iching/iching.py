# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 14:19:41 2015

@author: chengjun
"""

import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from collections import defaultdict

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
    yao  = data/4
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
        print "there is a changing predict! Also run changePredict()"
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

def interpretPredict(now, future):
    dt = {'111111':'乾','011111':'夬','000000':'坤','010001':'屯','100010':'蒙','010111':'需','111010':'讼','000010':'师',
'010000':'比','110111':'小畜','111011':'履','000111':'泰','111000':'否','111101':'同人','101111':'大有','000100':'谦',
'001000':'豫','011001':'随','100110':'蛊','000011':'临','110000':'观','101001':'噬嗑','100101':'贲','100000':'剥',
'000001':'复','111001':'无妄','100111':'大畜','100001':'颐','011110':'大过','010010':'坎','101101':'离','011100':'咸',
'001110':'恒','111100':'遁','001111':'大壮','101000':'晋','000101':'明夷','110101':'家人','101011':'睽','010100':'蹇',
'001010':'解','100011':'损','110001':'益','111110':'姤','011000':'萃','000110':'升','011010':'困','010110':'井',
'011101':'革','101110':'鼎','001001':'震','100100':'艮','110100':'渐','001011':'归妹','001101':'丰','101100':'旅',
'110110':'巽','011011':'兑','110010':'涣','010011':'节','110011':'中孚','001100':'小过','010101':'既济','101010':'未济'}
    if future:
        name = dt[now] + ' & ' + dt[future]
    else:
        name = dt[now]
    print name

def ichingText(k, iching):
    path = iching.__file__
    path = path.split('iching')[0]  
    import json
    dat = json.load(open(path + 'iching/package_data.dat'))
    print dat[k]

def plotTransition(N):
    import matplotlib.cm as cm
    import matplotlib.pyplot as plt
    from collections import defaultdict
    
    changes = {}
    for i in range(N):
        sky, earth, firstChange, data = getChange(data = 50 -1)
        sky, earth, secondChange, data = getChange(data)
        sky, earth, thirdChange, data = getChange(data)
        changes[i]=[firstChange, secondChange, thirdChange]

    ichanges = changes.values()

    firstTransition = defaultdict(int)
    for i in ichanges:
        firstTransition[i[0], i[1]]+=1

    secondTransition = defaultdict(int)
    for i in ichanges:
        secondTransition[i[1], i[2]]+=1

    cmap = cm.get_cmap('Accent_r', len(ichanges))

    for k, v in firstTransition.iteritems(): 
        plt.plot([1, 2], k, linewidth = v*100/N)
    for k, v in secondTransition.iteritems(): 
        plt.plot([2, 3], k, linewidth = v*100/N)

    plt.xlabel(u'Time')
    plt.ylabel(u'Changes')







