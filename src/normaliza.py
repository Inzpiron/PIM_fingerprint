import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import os
import math
from mylib.convolucao import *

def filtroContraste(mapa, operator, i, j):
    valor = 0
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            if(mapa[i][j] != -1):
                valor += operator[i][j] * mapa[i][j]
    valor = valor/3
    valor = min([valor, 255])
    valor = max([0,   valor])
    return valor

def filtroMediana(mapa, operator, i, j):
    vet = []
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            if(mapa[i][j] != -1):
                vet.append(mapa[i][j])

    return int(np.median(vet))

def filtroGaussiano(mapa, operator, i, j):
    vet = []
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            vet.append(mapa[i][j])

    return int(np.average(vet))

operator = [(-1,-1,-1,-1,-1),
            (-1, 2, 2, 2,-1),
            (-1, 2, 3, 2,-1),
            (-1, 2, 2, 2,-1),
            (-1,-1,-1,-1,-1)]

operator1 = [(1, 1, 1),
             (1, 1, 1),
             (1, 1, 1)]

operator2 = initMatrix(5, 5, 1)


nomeImg = "img*/" + sys.argv[2]
tipoImg = sys.argv[1]
img     = scipy.misc.imread(nomeImg + "." + tipoImg)
'''
process(img)
#data0 = convoluir(img, operator, filtroContraste)
media = imgMedia(img)
variancia = imgVariancia(img)
print media, variancia
data1 = filtroVariancia(img, media, variancia)
scipy.misc.imsave(nomeImg + "lol." + tipoImg, data1)
'''

print "->Filtro contraste"
data0 = convoluir(img, operator, filtroContraste)
print "->Filtro mediana"
data1 = convoluir(data0, operator1, filtroMediana)
print "->Filtro gaussiano"
data2 = convoluir(data1, operator2, filtroGaussiano)
scipy.misc.imsave(nomeImg + "." + tipoImg, data1)
print "OK!"
