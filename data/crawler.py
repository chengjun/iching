# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 19:22:16 2015

@author: Administrator
"""

#http://baike.fututa.com/zhouyi64gua/

import urllib2
from bs4 import BeautifulSoup
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# set work directory
os.chdir('D:/gua/')

dt = {'111111':'乾','011111':'夬','000000':'坤','010001':'屯','100010':'蒙','010111':'需','111010':'讼','000010':'师',
    '010000':'比','110111':'小畜','111011':'履','000111':'泰','111000':'否','111101':'同人','10111':'大有','000100':'谦',
    '001000':'豫','011001':'随','100110':'蛊','000011':'临','110000':'观','101001':'噬嗑','100101':'贲','100000':'剥',
    '000001':'复','111001':'无妄','100111':'大畜','100001':'颐','011110':'大过','010010':'坎','101101':'离','011100':'咸',
    '001110':'恒','111100':'遁','001111':'大壮','101000':'晋','000101':'明夷','110101':'家人','101011':'睽','010100':'蹇',
    '001010':'解','100011':'损','110001':'益','111110':'姤','011000':'萃','000110':'升','011010':'困','010110':'井',
    '011101':'革','101110':'鼎','001001':'震','100100':'艮','110100':'渐','001011':'归妹','001101':'丰','101100':'旅',
    '110110':'巽','011011':'兑','110010':'涣','010011':'节','110011':'中孚','001100':'小过','010101':'既济','101010':'未济'}


dr = {}
for i, j in dt.iteritems():
    dr[unicode(j, 'utf8')]= i

url = "http://baike.fututa.com/zhouyi64gua/"
content = urllib2.urlopen(url).read() #获取网页的html文本
soup = BeautifulSoup(content) 
articles = soup.find_all('div', {'class', 'gualist'})[0].find_all('a')
links = [i['href'] for i in articles]


for j in links:
    print j
    ghtml = urllib2.urlopen(j).read() #获取网页的html文本
    gua = BeautifulSoup(ghtml) 
    guaName =  gua.title.text.split('_')[1].split(u'卦')[0]
    guaId = dr[guaName]
    guawen = gua.find_all('div', {'class', 'gua_wen'})
    for i in guawen:
        with open(guaId + '.text', 'a') as f:
            f.write(i.get_text() + '\n\n')
    f.close()