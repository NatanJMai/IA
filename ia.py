from Fish   import Fish
from task01 import taskMain
from math   import sqrt

global setFish
setFishRobalo = []
setFishSalmao = []
robalo  = []
salmao  = []

def calcDistance(fishA, fishB):
  w1 = 0.7
  w2 = 0.3
  return sqrt((w1 * ((fishA.light - fishB.light) ** 2)) + (w2 * ((fishA.length - fishB.length) ** 2)))

def getDistanceFromSet(fish1):
  distancesRobalo = []
  distancesSalmao = []
  for i in setFishRobalo:
    distancesRobalo.append(calcDistance(i, fish1))

  for j in setFishSalmao:
    distancesSalmao.append(calcDistance(j, fish1))
 
  mediaRobalo = sum(distancesRobalo) / len(distancesRobalo)
  mediaSalmao = sum(distancesSalmao) / len(distancesSalmao)

  if mediaRobalo > mediaSalmao:
    return 'salmao'
  else:
    return 'robalo'


def filterSet(fishes, setR, setS):
  newF = []
  
  for i in fishes:
    if i.descr == 'robalo':
      if i.name in setR:
        setFishRobalo.append(i)
      else:
        newF.append(i)

    if i.descr == 'salmao':
      if i.name in setS:
        setFishSalmao.append(i)
      else:
        newF.append(i)
  return newF


def finalCalc(fishesAx):
  ab = []
  for i in fishesAx:
    result  = getDistanceFromSet(i)
    i.descr = result
    ab.append(i)
  return ab


def sPrint(fish):
  print("__________________________________________________________")
  for i in fish:
    if i.descr == 'salmao':
      print("SS%d = (%s,%s)" % (int(i.name), i.light, i.length))
    else:
      print("RR%d = (%s,%s)" % (int(i.name), i.light, i.length))


def diff(fishSet1, fishSet2):
  cont = 0

  for i in range(0, len(fishSet1)):
    if fishSet1[i].descr != fishSet2[i].descr:
      cont += 1
      print(fishSet1[i].name, fishSet1[i].light, fishSet1[i].length, fishSet1[i].descr)
      print(fishSet2[i].name, fishSet2[i].light, fishSet2[i].length, fishSet2[i].descr)
      print("-----------------------------------------")
  return cont


def main():
  res    = taskMain()
  aux1   = [] 
  cont   = 0
  setS = [13.0,14.0,15.0,22.0,23.0,30.0]
  setR = [29.0,30.0,42.0,43.0,48.0,49.0]
  
  for i in filterSet(res, setR, setS):
    j = Fish()
    j.createFish(i.name, i.light, i.length, i.descr)
    aux1.append(j)
  
  fishes  = filterSet(res, setR, setS)
  fishes1 = finalCalc(fishes)
  
  cont = diff(aux1, fishes1)
  print("%d diferencas" % cont)

if __name__ == "__main__":
 	main()
