# -*- coding: utf-8 -*-
# natan.mai@hotmail.com

from math   import *
from Fish   import Fish
from task01 import taskMain
from random import uniform

neuros = [[],[],[],[],[],[],[],[]]

class neuro(object):
  def createNeuro(self, weightL, weightC):
    self.weightL = weightL
    self.weightC = weightC


def main():
  calcWeights(setFish[0])
  return True



def calcWeights(fish):
  for i in neuros:
    for j in i:
      calcDistance(j, fish)


def calcDistance(neuro, fish):
  dist = sqrt(((fish.light - neuro.weightL) ** 2) + ((fish.length - neuro.weightC) ** 2))
  print(dist)


if __name__ == "__main__":
  setFish   = taskMain()

  for i in range(0, 8):
    for j in range(0, 8):
      neu = neuro()
      neu.createNeuro(uniform(0, 1), uniform(0, 1))
      neuros[i].append(neu)
  
  for i in neuros:
    for j in i:
      print(j.weightL, j.weightC)
  main()
