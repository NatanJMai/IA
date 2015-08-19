# -*- coding: utf-8 -*-
# natan.mai@hotmail.com

from math   import *
from Fish   import Fish
from task01 import taskMain
from random import uniform

neuros = [[],[],[],[],[],[],[],[]]
global distances
distances = []

class neuro(object):
  def createNeuro(self, weightL, weightC):
    self.weightL  = weightL
    self.weightC  = weightC
    self.distance = 0


def main():
  neuSimilar = competitive(setFish[0])

  return True



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
  return menor


def colaborative():
  return True


if __name__ == "__main__":
  setFish   = taskMain()

  for i in range(0, 8):
    for j in range(0, 8):
      neu = neuro()
      neu.createNeuro(uniform(0, 1), uniform(0, 1))
      neuros[i].append(neu)
 
  main()

