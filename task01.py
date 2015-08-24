# -*- coding: utf-8 -*-
# @NatanJMai - natan.mai@hotmail.com

import xlrd
from Fish import Fish

robalo = []
salmao = []
fishes = []

def getFishesFromXLS():
  lines = 132

  workbook  = xlrd.open_workbook('Task001.xls')
  worksheet = workbook.sheet_by_name('IA')

  for i in range(1, lines):
    fish = Fish() 
    fish.createFish(worksheet.cell(i,0).value, worksheet.cell(i, 1).value, worksheet.cell(i, 2).value, worksheet.cell(i,3).value, 0, 0)

    #fish.createFish(worksheet.cell(i,0).value, worksheet.cell(i, 1).value, worksheet.cell(i, 2).value)
    
    if 'robalo' in fish.descr:
      robalo.append(fish)
    else:
      salmao.append(fish)
    fishes.append(fish)


def taskMain():
  getFishesFromXLS()
  
  return fishes

if __name__ == "__main__":
  taskMain()
