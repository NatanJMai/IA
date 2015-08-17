# -*- coding: utf-8 -*-
# @NatanJMai - natan.mai@hotmail.com

from Fish   import Fish
from task01 import taskMain
from enum   import Enum
from math import sqrt

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
  n    = 0
  j    = 0
  while n < 100 and j < 100:
    if passo2() == 1:
      j += 1
    passo3()
    n += 1
  
  nr1 = 0
  print("A ===========> ")
  for it in setFish:
    if it.tipo == "A":
      nr1 += 1
      print("%f - %f" % (it.light, it.length))

  nr = 0
  print("B ===========> ")
  for it in setFish:
    if it.tipo == "B":
      nr += 1
      print("%f - %f" % (it.light, it.length))


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
  i = 0
  for it in setFish:
    it.distA = getDistances(it, clusterA.center)
    it.distB = getDistances(it, clusterB.center) 

    if it.distA > it.distB:
      if it.tipo == "A":
        i = 1
      it.tipo = "B"
    else:
      if it.tipo == "B":
        i = 1
      it.tipo = "A"
  return i

def passo3():
  totalL = 0
  totalC = 0
  nr     = 0
  a      = 0
  b      = 0
  for i in setFish:
    if i.tipo == "A":
      nr += 1
      totalL += i.light
      totalC += i.length
  
  if nr != 0:
    a = totalL / nr
    b = totalC / nr
    clusterA.center = (a, b)

  totalL = 0
  totalC = 0
  nr     = 0
  a      = 0
  b      = 0
  for i in setFish:
    if i.tipo == "B":
      nr += 1
      totalL += i.light
      totalC += i.length

  if nr != 0:
    a = totalL / nr
    b = totalC / nr
  
    clusterB.center = (a, b)


if __name__ == "__main__":
  p1 = (1.4, 21)
  p2 = (10.2, 17)
  
  global clusterA
  global clusterB
  clusterA = Cluster()
  clusterB = Cluster()
  clusterA.createCluster(Type.Nada, "A", [], p1)
  clusterB.createCluster(Type.Nada, "B", [], p2)

  setFish  = taskMain()
  main(p1, p2)
