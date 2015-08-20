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
n0  = 0.3
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
  return True


def verifyNeigh(i, d, z):
  if (((i - d) < z) and (z < (i + d))):
    return True


def updateWeight(neu):
  neu



def getD():
  d = ceil(d0 * (1 - (itAtual / T)))
  return d

def findNeighb(neu):
  for n in neuro:
    d = getD()
    if verifyNeigh(neu.x, d, n.x) and verifyNeigh(neu.y, d, n.y):



def calcDistance(neuro, fish):
  dist = sqrt(((fish.light - neuro.weightL) ** 2) + ((fish.length - neuro.weightC) ** 2))
  return dist


# determina o neurônio com os pesos mais
# similares ao vetor de característica apresentado ao mapa.
def competitive(fish):
  for i in neuros:
    for j in i:
      a = calcDistance(j, fish)
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

