# -*- coding: utf-8 -*-
# @NatanJMai - natan.mai@hotmail.com

from Fish   import Fish
from task01 import taskMain
from enum   import Enum
from math import sqrt

global i
i = 0

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
  n    = 0
  j    = 0
  while n < 100 and j < 10:
    passo2()
    if i == 1:
      j += 1
    passo3()
    n += 1
  
  nr1 = 0
  print("A ===========> ")
  for it in setFish:
    if it.tipo == "A":
      nr1 += 1
      print(it.light, it.length)

  print(nr1)

  nr = 0
  print("B ===========> ")
  for it in setFish:
    if it.tipo == "B":
      nr += 1
      print(it.light, it.length)

  print(nr)
  print(len(setFish), nr + nr1)
#  for i in clusterB.setC:
 #   print(i.light, i.length)

#    print("A => %f - %f" % (clusterA.center[0], clusterA.center[1]))
#    print("B => %f - %f" % (clusterB.center[0], clusterB.center[1]))


def getDistances(fish, cluster):
  #Cluster A
  w1 = 0.7
  w2 = 0.3
  
  #print(cluster)
  d = sqrt((w1 * ((fish.light - cluster[0]) ** 2)) + (w2 * ((fish.length - cluster[1]) ** 2)))
  return d 

def passo1(p1, p2):
  passo2()

def passo2():
  for it in setFish:
    it.distA = getDistances(it, clusterA.center)
    it.distB = getDistances(it, clusterB.center) 

    if it.distA > it.distB:
      if it.tipo == "A":
        print("s")
        i = 1
      it.tipo = "B"
    else:
      if it.tipo == "B":
        print("a")
        i = 1
      it.tipo = "A"

#  passo3()

def passo3():
  #novos centroides
  
  totalL = 0
  totalC = 0
  nr     = 0
  for i in setFish:
    if i.tipo == "A":
      nr += 1
      totalL += i.light
      totalC += i.length

  a = totalL / nr
  b = totalC / nr
  clusterA.center = (a, b)

  totalL = 0
  totalC = 0
  nr     = 0
  for i in setFish:
    if i.tipo == "B":
      nr += 1
      totalL += i.light
      totalC += i.length

  a = totalL / nr
  b = totalC / nr
  
  clusterB.center = (a, b)
  
#  print("------------------------------------------------\n")
#  print(clusterA.center)
#  print(clusterB.center)


def passo4():
  return True

def passo5():
  return True


if __name__ == "__main__":
  p1 = (1.0, 14)
  p2 = (1, 17)
  
  global clusterA
  global clusterB
  clusterA = Cluster()
  clusterB = Cluster()
  clusterA.createCluster(Type.Nada, "A", [], p1)
  clusterB.createCluster(Type.Nada, "B", [], p2)

  setFish  = taskMain()
  main(p1, p2)
