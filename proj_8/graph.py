class Graph(object):
    def __init__(self, graph=None):
        self.graph = graph

    def __str__(self):
        return 0

    def add_vertex(self, label):
        return 0

    def add_edge(self, src, dest, w):
        return 0

    def get_weight(self, src, dest) :
        return 0

    def dfs(self, starting_vertex):
        return 0

    def bfs(self, starting_vertex):
        return 0

    #def dijkstra_shortest_path(self, src):          FIXME: Will be removing
    #    return 0

    def dijkstra_shortest_path(self, src, dest="ALL"):
        return 0


class Vertex(object):
    def __init__(self, label, visited="No"):
        self.label = label
        self.visited = visited

    def __str__(self):
        return self.label

    def set_visit(self, status):
        self.visited = status

    def set_label(self, label):
        self.label = label

class Line(object):
    def __init__(self, src, dest, wgt):
        self.source = src
        self.destination = dest
        self.weight = float(wgt)

    def __str__(self):
        return self.weight

    def set_source(self, source):
        self.source = source

    def set_destination(self, dest):
        self.destination = dest

    def set_weight(self, wgt):
        self.weight = wgt

def main():
    pass

if __name__ == "__main__":
    main()

