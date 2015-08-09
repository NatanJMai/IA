from Fish   import Fish
from task01 import taskMain
from math   import sqrt

global setFish
setFishRobalo = []
setFishSalmao = []
robalo  = []
salmao  = []
fishes  = []

def calcDistance(fishA, fishB):
  w1 = 0.7
  w2 = 0.3
  return sqrt((w1 * ((fishA.light - fishB.light) ** 2)) - (w2 * ((fishA.length - fishB.length) ** 2)))

def getDistanceFromSet(fish1):
  distancesRobalo = []
  distancesSalmao = []
  for i in setFishRobalo:
    distancesRobalo.append(calcDistance(i, fish1))

  for j in setFishSalmao:
    distancesSalmao.append(calcDistance(j, fish1))
  
  return ((sum(distancesRobalo) / len(distancesRobalo)), (sum(distancesSalmao) / len(distancesSalmao)))

def main():
  res    = taskMain()
  fishes = res
  
  print(fishes[0].name, fishes[1].name)
  print(calcDistance(fishes[0], fishes[1]))

if __name__ == "__main__":
 	main()
