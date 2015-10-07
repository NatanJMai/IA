#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as MATH

class Graph(object):
  def init(self, name, bias):
    self.name  = name
    self.bias  = bias
    self.vList = []
    self.vMatx = [[]]

class Vertex(object):
  def newVertex(self, name, level, numberM, numberL, bias):
    self.name   = name
    self.level  = level
    self.numberM = numberM
    self.numberL = numberL
    self.value   = 0
    self.weight = 0
    self.bias   = bias
    self.eList  = []


#################################################3

def initMatx(vertex, graph):
  l = []
  for i in range(0, vertex):
    x = []
    for j in range(0, vertex):
      x.append(-1)
    l.append(x)
  graph.vMatx = l


def makeNewGraph(vertex, edges, bias):
  vertx = Vertex()
  vertx.newVertex("BIAS", -1, 0, -1, 0)
  vertx.value = bias
  graph = Graph()
  graph.init("G", vertx)
  bias  = 1.0
  initMatx(vertex, graph)

  for i in range(1, vertex):
    vertx = Vertex()
    if i < 5:
      vertx.newVertex(str(i), 0, i, i - 1, bias)
    elif i < 8:
      vertx.newVertex(str(i), 1, i, i - 1, bias)
    else:
      vertx.newVertex(str(i), 2, i, i - 1, bias)
    graph.vList.append(vertx)
  return graph


def displayVertex(graph, number):
  vert = graph.vList[number]

  print("Name => %s" % vert.name)
  for i in vert.eList:
    print(i.name, i.source.name, i.target.name, i.weight)
  print("-------------------------------\n")


def assignValues(vList, graph):

  entry = [0.5, 3, 5, 3, 6]
  outp  = [8, 49]

  w0 = [1.00, 0.22, 0.77, 0.73, 0.56]
  w1 = [1.00, 0.72, 0.28, 0.95, 0.95]
  w2 = [1.00, 0.34, 0.86, 0.37, 0.48]
  w3 = [1.00, 0.71, 0.52, 0.77]
  w4 = [1.00, 0.35, 0.08, 0.37]
  
  w  = [w0, w1, w2, w3, w4]

  nivel2 = []
  nivel1 = []
  nivel0 = []
  for i in vList:
    if i.level == 2:
      nivel2.append(i)
    elif i.level == 1:
      nivel1.append(i)
    elif i.level == 0:
      nivel0.append(i)
 
  # BIAS
  graph.vMatx[0][5] = 1.00
  graph.vMatx[0][6] = 1.00
  graph.vMatx[0][7] = 1.00
  graph.vMatx[0][8] = 1.00
  graph.vMatx[0][9] = 1.00

  graph.vMatx[5][0] = 1.00
  graph.vMatx[6][0] = 1.00
  graph.vMatx[7][0] = 1.00
  graph.vMatx[8][0] = 1.00
  graph.vMatx[9][0] = 1.00

  ####################
  graph.vMatx[5][1] = 0.22
  graph.vMatx[5][2] = 0.77
  graph.vMatx[5][3] = 0.73
  graph.vMatx[5][4] = 0.56
  for i in range(1, 5):
    graph.vList[4].eList.append(i)

  graph.vMatx[1][5] = 0.22
  graph.vMatx[2][5] = 0.77
  graph.vMatx[3][5] = 0.73
  graph.vMatx[4][5] = 0.56
  for i in range(0, 4):
    graph.vList[i].eList.append(5)

  ####################
  graph.vMatx[6][1] = 0.72
  graph.vMatx[6][2] = 0.28
  graph.vMatx[6][3] = 0.95
  graph.vMatx[6][4] = 0.95
  for i in range(1, 5): 
    graph.vList[5].eList.append(i)
    graph.vList[i - 1].eList.append(6)

  graph.vMatx[1][6] = 0.72
  graph.vMatx[2][6] = 0.28
  graph.vMatx[3][6] = 0.95
  graph.vMatx[4][6] = 0.95

  ####################
  graph.vMatx[7][1] = 0.34
  graph.vMatx[7][2] = 0.86
  graph.vMatx[7][3] = 0.37
  graph.vMatx[7][4] = 0.48
  for i in range(1, 5):
    graph.vList[6].eList.append(i)
    graph.vList[i - 1].eList.append(7)

  graph.vMatx[1][7] = 0.34
  graph.vMatx[2][7] = 0.86
  graph.vMatx[3][7] = 0.37
  graph.vMatx[4][7] = 0.48

  ####################
  graph.vMatx[8][5] = 0.71
  graph.vMatx[8][6] = 0.52
  graph.vMatx[8][7] = 0.77
  for i in range(5, 8):
    graph.vList[7].eList.append(i)
    graph.vList[i - 1].eList.append(8)

  graph.vMatx[5][8] = 0.71
  graph.vMatx[6][8] = 0.52
  graph.vMatx[7][8] = 0.77

  ####################
  graph.vMatx[9][5] = 0.35
  graph.vMatx[9][6] = 0.08
  graph.vMatx[9][7] = 0.37
  for i in range(5, 8):
    graph.vList[8].eList.append(i)
    graph.vList[i - 1].eList.append(9)

  graph.vMatx[5][9] = 0.35
  graph.vMatx[6][9] = 0.08
  graph.vMatx[7][9] = 0.37
  printM(graph)

def printM(graph):
  for i in graph.vList:
    print(i.name, i.value)

  print("\n")
  for j in range(0, len(graph.vMatx)):
    print("%d =>    %s" % (j, graph.vMatx[j]))

  #for j in graph.vList:
  #  print(j.name, j.weight, j.numberM, j.eList)



def sigmoide(x):
  result = 1 / (1 + MATH.exp(-(x)))
  return result


def getSumWeight(numberM, numberL, graph, entry):
  xList = graph.vList[numberL].eList
  soma  = 0.0

  for i in range(0, len(entry)):
    soma += graph.vMatx[xList[i]][numberM] * entry[i]
  
  soma += graph.bias.value * graph.vMatx[0][numberM]
  
  '''
  print("%d -> %s = %0.2f" % (numberM, 'bias', graph.vList[numberL].bias))
  for i in xList:
    print("%d -> %d = %f" % (numberM, i, graph.vMatx[i][numberM]))
  '''
  return sigmoide(soma)


def calcErrorOutput1(out1, out2, graph):
  get1 = graph.vList[7].value
  get2 = graph.vList[8].value
  
  res1 = get1 * (1 - get1) * (out1 - get1)
  res2 = get2 * (1 - get2) * (out2 - get2)
  graph.vList[7].value = res1
  graph.vList[8].value = res2


def calcOtherWeight2(numberM, target, value, graph):
  graph.vMatx[numberM][target] = graph.vMatx[numberM][target] + (value * graph.vList[numberM - 1].value)
  graph.vMatx[target][numberM] = graph.vMatx[numberM][target]
    

def updateInputWeight(numberM, target, graph):
  wei  = graph.vMatx[numberM][target]
  valA = graph.vList[target - 1].value
  valI = graph.vList[numberM - 1].value
  
  graph.vMatx[numberM][target] = wei + (valA * valI)
  graph.vMatx[target][numberM] = graph.vMatx[numberM][target]


def calcValueUpdate3(numberL, targetL, graph):
  nL  = numberL - 1
  vnL = graph.vList[nL].value
  som = 0.0

  for i in targetL:
    som = som + (graph.vList[i - 1].value * graph.vMatx[numberL][i])
 
  graph.vList[nL].value = vnL * (1 - vnL) * som
#  print(graph.vList[nL].name, graph.vList[tL].name)

def printOutputs(out1, out2, graph):
  print("RESULTADO => "),
  print(out1 - graph.vList[7].value, out2 - graph.vList[8].value)

if __name__ == "__main__":
  training = [[0.5, 3.0, 5.0, 3.0, 6.0, 8.0, 49.0], 
              [0.5, 4.0, 6.0, 3.0, 5.0, 8.0, 47.0], 
              [0.5, 7.0, 3.0, 6.0, 8.0, 86.0, 80.0], 
              [0.5, 4.0, 6.0, 4.0, 7.0, 21.0, 70.0], 
              [0.5, 5.0, 7.0, 5.0, 6.0, 22.0, 68.0],
              [0.5, 8.0, 4.0, 7.0, 9.0, 112.0, 107.0], 
              [0.5, 5.0, 7.0, 5.0, 8.0, 38.0, 95.0]]

  #ALTERAR O INDICE PARA TROCAR O TESTE (0 a 6). 
  trainings = [training[0]]

  graph = makeNewGraph(10, 0, 0.5)
  assignValues(graph.vList, graph)
  f = 0 
   
  while(f < 3):
    print("\n### %dº PASSO\n" % (f + 1))
    for i in trainings:
      geral = i
      bias  = geral[0]
      entry = geral[1:5]
      outp1 = geral[5]
      outp2 = geral[6]

      print(outp1, outp2)

      graph.vList[0].value = geral[1]
      graph.vList[1].value = geral[2]
      graph.vList[2].value = geral[3]
      graph.vList[3].value = geral[4]

      graph.vList[4].value = getSumWeight(5, 4, graph, entry)
      graph.vList[5].value = getSumWeight(6, 5, graph, entry)
      graph.vList[6].value = getSumWeight(7, 6, graph, entry)

      entry = []
      entry.append(graph.vList[4].value)
      entry.append(graph.vList[5].value)
      entry.append(graph.vList[6].value)
  
      graph.vList[7].value = getSumWeight(8, 7, graph, entry)
      graph.vList[8].value = getSumWeight(9, 8, graph, entry)
   
      calcErrorOutput1(outp1, outp2, graph)

      calcOtherWeight2(5, 8, graph.vList[7].value, graph)
      calcOtherWeight2(5, 9, graph.vList[8].value, graph)

      calcOtherWeight2(6, 8, graph.vList[7].value, graph)
      calcOtherWeight2(6, 9, graph.vList[8].value, graph)
 
      calcOtherWeight2(7, 8, graph.vList[7].value, graph)
      calcOtherWeight2(7, 9, graph.vList[8].value, graph)
  
      calcValueUpdate3(5, [8,9], graph)
      calcValueUpdate3(6, [8,9], graph)
      calcValueUpdate3(7, [8,9], graph)
   
      updateInputWeight(1, 5, graph)
      updateInputWeight(1, 6, graph)
      updateInputWeight(1, 7, graph)
      updateInputWeight(2, 5, graph)
      updateInputWeight(2, 6, graph)
      updateInputWeight(2, 7, graph)
      updateInputWeight(3, 5, graph)
      updateInputWeight(3, 6, graph)
      updateInputWeight(3, 7, graph)
      updateInputWeight(4, 5, graph)
      updateInputWeight(4, 6, graph)
      updateInputWeight(4, 7, graph)

      printOutputs(outp1, outp2, graph)
    f += 1
