# -*- coding: utf-8 -*-
# natan.mai@hotmail.com

from math   import *
from Fish   import Fish
from task01 import taskMain
from random import uniform
from numpy  import *
from pylab  import *

global neuros
neuros = [[],[],[],[],[],[],[],[]]

'''
n   = 8
n0  = 0.2
d0  = n / 2
T   = 110

#It atual
itA = 0
'''

class neuro(object):
  def createNeuro(self, weightL, weightC, x, y):
    self.weightL  = weightL
    self.weightC  = weightC
    self.distance = 0
    self.x        = x
    self.y        = y


def updateN0(n0, itA, T):
  a = n0 * (1.0 - (itA / T))
  return a


def printF():
  listaX = []
  listaY = []
  for i in neuros:  
    for it in range(0, len(i)):
      listaX.append(i[it].x)
      listaY.append(i[it].y)
   
  plot(listaX, listaY, 'ro')
  axis([-1,9,-1,9])
  show()


def printF2(entry):
  listaX = []
  listaY = []

  for i in entry:
    listaX.append(i.xNeu)
    listaY.append(i.yNeu)

  plot(listaX, listaY, 'ro')
  axis([-1, 9, -1, 9])
  show()


def main(entry, entryTest):  
  itA = 0        # Iteracao atual
  n   = 8        # n x n
  n0  = 0.2      # Aprendizado
  d0  = 4.0      # Vizinhanca
  T   = len(entry)      # Total do treinamento
   
  while itA < 70:
    for i in entry:
      neuSimilar = competitive(i)
      findNeighb(neuSimilar, d0, n0)

    c  = updateN0(n0, itA, T)
    d  = updateD0(d0, itA, T)
    d0 = d
    n0 = c
    itA = itA + 1
  
  
  application(entryTest)
  
  for i in entryTest:
    print(i.light, i.length)
    print(i.xNeu, i.yNeu)


  printF2(entryTest)
  return True


def application(entry):
  for i in entry:
    similar = competitive2(i)
  

def competitive2(i):
  distances = []

  for ne in neuros:
    for j in ne:
      a = calcDistanceNF(j, i)
      j.distance = a
      distances.append(a)
      if j.distance == min(distances):
        menor = j

  i.xNeu = menor.x
  i.yNeu = menor.y
  return menor    
  

def verifyNeigh(i, d, z):
  if (((i - d) < z) and (z < (i + d))):
    return True
  else:
    return False


def getKnow():
  res = n0 * (1 - (itA / T))
  return res


def updateWeight(neu, mini, n0):
  a = neu.weightL + (n0 * (calcDistanceNN(mini, neu)))
  b = neu.weightC + (n0 * (calcDistanceNN(mini, neu)))
  neu.weightL = a
  neu.weightC = b


def updateD0(d0, itA, T):
  b = ceil(d0 * (1 - (itA / T)))
  return b


def findNeighb(neu, d0, n0):
  for it in neuros:
    for n in it: 
      if verifyNeigh(neu.x, d0, n.x) and verifyNeigh(neu.y, d0, n.y):
        updateWeight(n, neu, n0)


def calcDistanceNN(neu1, neu2):
  dist = double(sqrt(((neu1.weightL - neu2.weightL) ** 2) + ((neu1.weightC - neu2.weightC) ** 2)))
  return dist


def calcDistanceNF(neuro, fish):
  dist = double(sqrt(((fish.light - neuro.weightL) ** 2) + ((fish.length - neuro.weightC) ** 2)))

  return dist


# determina o neurônio com os pesos mais
# similares ao vetor de característica apresentado ao mapa.
def competitive(fish):
  distances = []

  for i in neuros:
    for j in i:
      a = calcDistanceNF(j, fish)
      j.distance = a
      distances.append(a)
      if j.distance == min(distances):
        menor = j
  return menor


def colaborative():
  return True


if __name__ == "__main__":
  entry     = []
  entryTest = []
  setFish   = taskMain()
  entries   = [9, 10, 11, 12, 13, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]

  for i in range(0, 8):
    for j in range(0, 8):
      neu = neuro()
      neu.createNeuro(uniform(0, 1), uniform(0, 1), i, j)
      neuros[i].append(neu)
 
  for i in range(0, len(setFish)):
    if i in entries:
      entryTest.append(setFish[i])
    else:
      entry.append(setFish[i])
  
  main(entry, entryTest)

  for i in range(0, len(setFish)):
    it = setFish[i]
    print(i, it.light, it.length, it.descr, it.xNeu, it.yNeu)

