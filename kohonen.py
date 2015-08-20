# -*- coding: utf-8 -*-
# natan.mai@hotmail.com

from math   import *
from Fish   import Fish
from task01 import taskMain
from random import uniform

neuros = [[],[],[],[],[],[],[],[]]
global distances
global itA
global n
global d0
global T
global n0
distances = []


n   = 8
n0  = 0.2
d0  = n / 2
T   = 130

#It atual
itA = 0

class neuro(object):
  def createNeuro(self, weightL, weightC, x, y):
    self.weightL  = weightL
    self.weightC  = weightC
    self.distance = 0
    self.x        = x
    self.y        = y


def main():
  neuSimilar = competitive(setFish[0])
  findNeighb(neuSimilar)
  return True


def verifyNeigh(i, d, z):
  if (((i - d) < z) and (z < (i + d))):
    return True


def getKnow():
  res = n0 * (1 - (itA / T))
  return res


def updateWeight(neu, mini):
  neu.weightL = neu.weightL + (getKnow() * (calcDistanceNN(mini, neu)))
  neu.weightC = neu.weightC + (getKnow() * (calcDistanceNN(mini, neu)))


def getD():
  d = ceil(d0 * (1 - (itA / T)))
  return d


def findNeighb(neu):
  for it in neuros:
    for n in it: 
      d = getD()
      if verifyNeigh(neu.x, d, n.x) and verifyNeigh(neu.y, d, n.y):
        print("-------------------------------------------------------------------\n")
        print("neigh  ==> %d - %d, para D => %f" % (n.x, n.y, d))
        print("before ==> %d - %d, => %f - %f" % (n.x, n.y, n.weightL, n.weightC))
        updateWeight(n, neu)
        print("after  ==> %d - %d, => %f - %f" % (n.x, n.y, n.weightL, n.weightC))
        print("-------------------------------------------------------------------\n")


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
 
  main()

