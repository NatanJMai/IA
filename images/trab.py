# -*- coding: utf-8 -*-

import xlrd

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


def media(f):
  oldM = f.matx
  newM = []

  for i in range(0, 11):
    for j in range(0, 11):
      p = j + 2
      f = i + 2
      print(oldM[i][j], oldM[i][p], oldM[f][j])


if __name__ == "__main__":
  files = getImagesCSV()
  for i in range(0, 1):
    media(files[i])
    print('\n\n')

  
