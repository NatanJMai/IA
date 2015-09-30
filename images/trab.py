# -*- coding: utf-8 -*-

from scipy.stats import * 
import numpy as np
import xlrd
import matplotlib.pyplot as plt
from matplotlib.pylab import *
import time

class File (object):
  def init(self, name, matx):
    self.name = name
    self.matx = matx

def getImagesCSV():
  files = []
  lines = 13
  coln  = 13

  for i in range(1, 21):
    matriz = []

    if i < 10:
      name = "data0%d.xls" % i
    else:
      name = "data%d.xls" % i
    
    wb = xlrd.open_workbook(name)
    ws = wb.sheet_by_name("Sheet1")
    
    for i in range(0, lines):
      linha = []
      for j in range(0, coln):
        linha.append(ws.cell(i, j).value)
      matriz.append(linha)
    
    f = File()
    f.init(name, matriz)
    
    files.append(f)
  return files


def bordas(mapa, linha, coluna):
  esquerda = 0
  direita  = 0
  cima     = 0
  baixo    = 0
  matrz    = []
  #print("\nTestando => %d" % mapa[linha][coluna])

  if coluna != 0:
    esquerda = 1
  if coluna != 12:
    direita  = 1
  if linha  != 0:
    cima     = 1
  if linha  != 12:
    baixo    = 1
  
  for x in range(linha  - cima, linha + baixo + 1):
    list1 = []
    for j in range(coluna - esquerda, coluna + direita + 1):
      list1.append(mapa[x][j])
    matrz.append(list1)
  return matrz


def calcBaixa(op, kernel):
  #media
  if op == 1:
    soma = 0
    nrs  = 0
    for x in kernel:
      nrs  += len(x)
      soma += sum(x)

    result = round(soma / nrs, 4)
    return result

  #Moda
  elif op == 2:
    ll = []
    for x in kernel:
      for p in x:
        ll.append(p)
    result = mode(ll)[0][0]
    return result

  #Mediana
  elif op == 3:
    ll = []
    for x in kernel:
      for j in x:
        ll.append(j)

    result = np.median(sorted(ll))
    return result


def calcAlta(op, mapa, kernel, x, j):
  if mapa[x][j] < 0:
    c = -1
  else:
    c = 1

  result = mapa[x][j] + (c * sum(kernel))
  return result

def bordasA(oldM, x, j):
  lista = []

  if x + 1 > 12:
    lista.append(0)
  else:
    lista.append(oldM[x + 1][j])

  if x - 1 < 0:
    lista.append(0)
  else:
    lista.append(oldM[x - 1][j])

  if j + 1 > 12:
    lista.append(0)
  else:
    lista.append(oldM[x][j + 1])

  if j - 1 < 0:
    lista.append(0)
  else:
    lista.append(oldM[x][j - 1])

  lista.append((-4) * oldM[x][j])
  return lista


def get(f, op, altaBaixa):
  newM = []
  for i in range(0, 13):
    l = []
    for j in range(0, 13):
      l.append(0)
    newM.append(l)

  oldM = f.matx
  lits = []
  
  if altaBaixa == 1:
    for i in range(0, 13):
      for j in range(0, 13):
        lits = bordas(oldM, i, j)
        newM[i][j] = calcBaixa(op, lits)
  
    for i in newM:
      print(i)
    print('\n\n')

  else:
    for i in range(0, 13):
      for j in range(0, 13):
        lits       = bordasA(oldM, i, j)
        newM[i][j] = calcAlta(op, oldM, lits, i, j)
    
    matshow(newM, fignum=101, cmap=cm.gray)
    show()
    for j in newM:
      print(j)
    print('\n\n')

def passaBaixa():
  files = getImagesCSV()
  
  nr = int(input("Arquivo nr => "))
  ab = int(input("Alta (0), Baixa (1) => "))
  nr -= 1
  
  print("\n\n ############### ARQUIVO %s ###############\n\n\n" % files[nr].name)

  for i in files[nr].matx:
    print(i)
  
  if ab == 1:
    opb = int(input("\nMedia(1)\nModa(2)\nMediana(3)\n=> "))
    print('\n') 
    get(files[nr], opb, 1)

    '''
    print("\nMEDIA =>\n")
    get(files[nr], 1, 1)

    print("\nMODA =>\n")
    get(files[nr], 2, 1)

    print("\nMEDIANA =>\n")
    get(files[nr], 3, 1)
    '''
    print('\n\n')

  else:
    opa = int(input("\nLaplaciano(1)\n=> "))
    print('\n')
    get(files[nr], 1, 0)


def samplemat(dims):
  """Make a matrix with all zeros and increasing elements on the diagonal"""
  aa = zeros(dims)
  for i in range(min(dims)):
    aa[i, i] = i
  return aa

def teste():

  # Display 2 matrices of different sizes
  #dimlist = [(12, 12), (15, 35)]
  #for d in dimlist:
  #  matshow(samplemat(d))

  # Display a random matrix with a specified figure number and a grayscale
  # colormap
  matshow(rand(64, 64), fignum=100, cmap=cm.gray)
  show()


if __name__ == "__main__":
  passaBaixa() 
