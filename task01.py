# -*- coding: utf-8 -*-
# @NatanJMai - natan.mai@hotmail.com

import xlrd

class Fish (object):
  def createFish(self, name, light, length, descr):
    self.name   = name
    self.light  = light
    self.length = length
    self.descr  = descr

global lines, fishs
fishs = []
lines = 132

robalo = []
salmao = []

workbook  = xlrd.open_workbook('Task001.xls')
worksheet = workbook.sheet_by_name('IA')

for i in range(1, lines):
  fish = Fish() 
  fish.createFish(worksheet.cell(i,0).value, worksheet.cell(i, 1).value, worksheet.cell(i, 2).value, worksheet.cell(i,3).value)
  if 'robalo' in fish.descr:
    robalo.append(fish)
  else:
    salmao.append(fish)
  fishs.append(fish)

for i in fishs:
  print(i.name, i.light, i.length, i.descr)


