class Graph(object):
  def init(self, name, bias):
    self.name  = name
    self.bias  = bias
    self.vList = []

class Vertex(object):
  def newVertex(self, name, level):
    self.name   = name
    self.level  = level
    self.eList  = []

class Edge(object):
  def newEdge(self, name, weight, source, target):
    self.name   = name
    self.weight = weight
    self.source = source
    self.target = target

#################################################3

def makeNewGraph(vertex, edges):
  vertx = Vertex()
  vertx.newVertex("BIAS", -1)
  graph = Graph()
  graph.init("G", vertx)
  
  for i in range(0, vertex):
    vertx = Vertex()
    if i < 4:
      vertx.newVertex(str(i + 1), 0)
    elif i < 7:
      vertx.newVertex(str(i + 1), 1)
    else:
      vertx.newVertex(str(i + 1), 2)
    graph.vList.append(vertx)
  return graph


def assignValues(vList, nivel):
  w0 = [1.00, 0.22, 0.77, 0.73, 0.56]
  w1 = [1.00, 0.72, 0.28, 0.95, 0.95]
  w2 = [1.00, 0.34, 0.86, 0.37, 0.48]
  w3 = [1.00, 0.71, 0.52, 0.77]
  w4 = [1.00, 0.35, 0.08, 0.37]

  nivel2 = []
  nivel1 = []
  nivel0 = []
  for i in vList:
    if i.level == nivel + 1:
      nivel1.append(i)
    elif i.level == nivel:
      nivel0.append(i)

  for i in range(0, len(nivel1)):
    edge = Edge()
    edge.newEdge("w" + str(i) + str(0), 0, nivel1[i], graph.bias)
    nivel1[i].eList.append(edge)
    for j in range(1, len(nivel0) + 1):
      edge = Edge()
      edge.newEdge("w" + str(i) + str(j), 0, nivel1[i], nivel0[j - 1])
      nivel0[i].eList.append(edge)
      nivel1[i].eList.append(edge)

  for i in nivel1:
    for j in i.eList:
      print(j.name)




if __name__ == "__main__":
  graph = makeNewGraph(9, 0)
  assignValues(graph.vList, 1)
