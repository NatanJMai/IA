# -*- coding: utf-8 -*-
# @NatanJMai - natan.mai@hotmail.com

from Fish   import Fish
from task01 import taskMain
from enum   import Enum
import math

class Type(Enum):
  Robalo = 0
  Salmao = 1
  Nada   = 2

class Cluster(object):
  def createCluster(self, typC, name, setC, center):
    self.typC   = typC
    self.name   = name
    self.setC   = setC
    self.center = center

def main(p1, p2):
  stop = True

  while stop:
    passo1(p1, p2)
    stop = False


def getDistances(fish):
  #Cluster A
  w1 = 0.7
  w2 = 0.3

  dSalmao = sqrt(w1 * ((fish.light - clusterA.center[0] ** 2)) + w2 * ((fish.length - clusterA.center[0]) ** 2))


  return True 

def passo1(p1, p2):
  return True

def passo2():
  for i in setFish:
    getDistances(i)

  return True

def passo3():
  return True

def passo4():
  return True

def passo5():
  return True


if __name__ == "__main__":
  p1 = (2, 3)
  p2 = (3, 4)

  clusterA = Cluster()
  clusterB = Cluster()
  clusterA.createCluster(Type.Nada, "A", [], (0,0))
  clusterB.createCluster(Type.Nada, "B", [], (0,0))

  setFish  = taskMain()
  main(p1, p2)
