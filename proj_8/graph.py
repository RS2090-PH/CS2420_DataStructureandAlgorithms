import math

class Graph(object):
    def __init__(self):
        self.graph = {}
        self.vertices = 0

    def __str__(self):
        temp = ""

        temp += "numVertices:%2d    \n"%(self.vertices)
        temp += "Vertex   Adjacency List\n"

        for item in self.graph:
            temp += "%s"%(self.graph[item])

        return temp

    def add_vertex(self, label):
        if isinstance(label, str) != True:
            raise ValueError("Label must be a string.")
        else:
            if label in self.graph:
                raise ValueError("Vertex already present.")
            else:
                self.graph[label] = Vertex(label)
                self.vertices += 1
            return self

    def add_edge(self, src, dest, w):
        if isinstance(w, (float, int)) != True:
            raise ValueError("Weight must ve a decimal value.")

        if src in self.graph:
            if dest not in self.graph:
                raise ValueError("Destination '%s' not in graph."%(dest))

            if dest not in self.get_vertex(src).edges:
                self.get_vertex(src).add_edge(dest, w)
            else:
                raise ValueError("Edge already present.")
        else:
            raise ValueError("Source '%s' not in graph."%(src))
        return self

    def get_vertex(self, label):
        if label in self.graph:
            return self.graph[label]

    def get_weight(self, src, dest) :
        if src in self.graph:
            return self.graph[src].get_edge_weight(dest)
        else:
            raise ValueError("Source vertex not present.")

    def dfs(self, starting_vertex):
        return list()

    def bfs(self, starting_vertex):
        return list()

    def dijkstra_shortest_path(self, src, dest=None):
        return list()


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = list()
        self.visited = False

    def __str__(self):
        temp = ""
        flag = 0

        temp += "%1s       ["%(self.label)
        
        for item in self.edges:
            if flag == 0:
                temp += "%s"%(item)
                flag += 1
            else:
                temp += ", %s"%(item)

        temp +="]\n"
        return temp

    def add_edge(self, dest, wgt):
        self.edges.append(Edge(self, dest, wgt))

    def set_visit(self, status):
        self.visited = status

    def set_label(self, label):
        self.label = label

    def get_edge_weight(self, dest):
        for item in self.edges:
            if item.destination == dest:
                return int(item.weight)
        return math.inf

class Edge(object):
    def __init__(self, src, dest, wgt, dir=None):
        self.source = src
        self.destination = dest
        self.weight = float(wgt)
        self.direction = dir
        self.visited = False

    def __str__(self):
        return "('%s', %2.1f)"%(self.destination,self.weight)

    def set_source(self, source):
        self.source = source

    def set_destination(self, dest):
        self.destination = dest

    def set_weight(self, wgt):
        self.weight = wgt
    
    def get_weight(self):
        return self.weight

def main():
    test = Graph()

    test.add_edge

    test.add_vertex("A")
    test.add_vertex("B")
    test.add_vertex("C")
    test.add_vertex("D")
    test.add_vertex("E")
    test.add_vertex("F")

    test.add_edge("A", "B", 1.0)
    test.add_edge("A", "C", 1.0)
    test.add_edge("B", "D", 1.0)
    test.add_edge("C", "E", 1.0)
    test.add_edge("E", "F", 1.0)
    print(test.get_weight("F", "E"))

    print(test)

    output = str(test)
    output[:14]
    print("Expects: numVertices: 6")

    print(test.get_weight("A", "B"))
    test.add_edge

    stupid = test.add_vertex("R")
    print(isinstance(stupid, Graph))
    print(type(stupid))

    ######

    

if __name__ == "__main__":
    main()

