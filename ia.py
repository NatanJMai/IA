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


def filterSet(fishes):
  newF = []
  setS = [13.0,14.0,15.0,22.0,23.0,30.0]
  setR = [29.0,30.0,42.0,43.0,48.0,49.0]
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
#    print(i.name, result, i.light, i.length)
  return ab

def sPrint(fish):
  print("__________________________________________________________")
  for i in fish:
    if i.descr == 'salmao':
      print("SS%d = (%s,%s)" % (int(i.name), i.light, i.length))
    else:
      print("RR%d = (%s,%s)" % (int(i.name), i.light, i.length))

  for j in setFishRobalo:
    print("RRRR_%d = (%s,%s)" % (int(j.name), j.light, j.length))

  for j in setFishSalmao:
    print("SSSS_%d = (%s,%s)" % (int(j.name), j.light, j.length))

def main():
  res    = taskMain()
  fishes = filterSet(res)
  sPrint(fishes)  
  fishes1 = finalCalc(fishes)
  
#  sPrint(fishes)
#  sPrint(fishes1)


if __name__ == "__main__":
 	main()
