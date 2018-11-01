#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:55:09 2018

@author: cristiano
"""

import os
import numpy as np
import random
from scipy.io import mminfo, mmread


nTest = int(round(150*0.3))
allIds = list(range(150))
random.shuffle(allIds)

print 'Numero de treinos:', len(allIds[:nTest])
print 'Number de testes:',len(allIds[nTest:])


with open('iris_teste.txt','w') as f:
    for i in allIds[:nTest]:
        f.write(str(i)+'\n')
        
with open('iris_treino.txt','w') as f:
    for i in allIds[nTest:]:
        f.write(str(i)+'\n')
        
with open('iris_classe_teste.txt','w') as f:
    for i in allIds[:nTest]:
        f.write(str(i)+'\n')        
     
        

cmd = 'aLine --classifier --algorithm knn --features iris_data.mtx --train iris_treino.txt --test iris_teste.txt --labels iris_class.txt -k 3 -o iris_class_predicao.txt'
os.system(cmd)

cmd = 'aLine --similarity --features iris_data.mtx -o similaridade.mtx'
os.system(cmd)


mat = mmread('similaridade.mtx').astype('float32')
den = mat.toarray()
soma = np.sum(den)
print '\nDensidade do dataset:', soma

media = np.mean(den)
print '\nMédia da densidade:', media
     

