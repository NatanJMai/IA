# -*- coding: utf-8 -*-
# natan.mai@hotmail.com

from math   import *
from Fish   import Fish
from task01 import taskMain
from random import uniform

neuros = [[],[],[],[],[],[],[],[]]
global distances
distances = []

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
  a = n0 * (1 - (itA / T))
  return a

def main(entry):  
  itA = 0.0      # Iteracao atual
  n   = 8        # n x n
  n0  = 0.2      # Aprendizado
  d0  = 4.0      # Vizinhanca
  T   = 110.0    # Total do treinamento

  while itA < 130 and n0 > 0.0000000000001:
    for i in entry:
      neuSimilar = competitive(i)
      findNeighb(neuSimilar, d0, n0)

    c  = updateN0(n0, itA, T)
    d  = updateD0(d0, itA, T)
    d0 = d
    n0 = c
    print(n0, d0)
    itA = itA + 1

  print(itA)
  return True


def verifyNeigh(i, d, z):
  if (((i - d) < z) and (z < (i + d))):
    return True


def getKnow():
  res = n0 * (1 - (itA / T))
  return res


def updateWeight(neu, mini, n0):
  neu.weightL = neu.weightL + (n0 * (calcDistanceNN(mini, neu)))
  neu.weightC = neu.weightC + (n0 * (calcDistanceNN(mini, neu)))


def updateD0(d0, itA, T):
  b = ceil(d0 * (1 - (itA / T)))
  return b

def findNeighb(neu, d0, n0):
  for it in neuros:
    for n in it: 
      if verifyNeigh(neu.x, d0, n.x) and verifyNeigh(neu.y, d0, n.y):
        #print("-------------------------------------------------------------------\n")
#        print("neigh  ==> %d - %d, para D => %f" % (n.x, n.y, d0))
#        print("before ==> %d - %d, => %f - %f" % (n.x, n.y, n.weightL, n.weightC))
        updateWeight(n, neu, n0)
#        print("after  ==> %d - %d, => %f - %f" % (n.x, n.y, n.weightL, n.weightC))
#        print("-------------------------------------------------------------------\n")


def calcDistanceNN(neu1, neu2):
  dist = sqrt(((neu1.weightL - neu2.weightL) ** 2) + ((neu1.weightC - neu2.weightC) ** 2))
  return dist


def calcDistanceNF(neuro, fish):
  dist = sqrt(((fish.light - neuro.weightL) ** 2) + ((fish.length - neuro.weightC) ** 2))
  return dist


# determina o neurônio com os pesos mais
# similares ao vetor de característica apresentado ao mapa.
def competitive(fish):
  for i in neuros:
    for j in i:
      a = calcDistanceNF(j, fish)
      j.distance = a
      distances.append(a)
      if j.distance == min(distances):
        menor = j

  print(min(distances))
  print(menor.x, menor.y)
  print("menor => %f - %f" % (menor.weightL, menor.weightC))
  return menor


def colaborative():
  return True


if __name__ == "__main__":
  setFish   = taskMain()

  for i in range(0, 8):
    for j in range(0, 8):
      neu = neuro()
      neu.createNeuro(uniform(0, 1), uniform(0, 1), i, j)
      neuros[i].append(neu)
 
  main([setFish[0]])

