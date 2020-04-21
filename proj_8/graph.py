"""
Author: Robby Stohel
File: graph.py

A graph module to allow the creation and manipulation of graphs.
"""

import math

class Graph():          # Removed "object" at pylint's request. Using python 3+
    """ Graph class to develop and managed graphs. """
    def __init__(self):
        """
        Initializer method to create graph objects.
        Process:
            Creates self.graph and self.vertices.
        Args:
            self(Graph): self
        Returns:
            None(None): None
        """
        self.graph = {}
        self.vertices = 0

    def __str__(self):
        """
        Method to generate a string representation of graphs.
        Process:
            Creates "temp" and concatonates the vertex count,
            and required column data.
        Args:
            self(Graph): self
        Returns:
            temp(str): String representation of graph
        """
        temp = ""

        temp += "numVertices:%2d    \n"%(self.vertices)
        temp += "Vertex   Adjacency List\n"

        for item in self.graph:
            temp += "%s"%(self.graph[item])

        return temp

    def add_vertex(self, label):
        """
        Method to add a vertex to the graph.
        Process:
            Type check's the label. Verifies it isn't already in.
            the graph, then adds the vertex to the graph.
        Args:
            self(Graph): self
            label(str): The label of the vertex
        Returns:
            self(Graph): Returns the graph with new vertex
        """
        if isinstance(label, str) is not True:
            raise ValueError("Label must be a string.")
        else:
            if label in self.graph:
                raise ValueError("Vertex already present.")
            else:
                self.graph[label] = Vertex(label)
                self.vertices += 1
            return self

    def add_edge(self, src, dest, wgt):
        """
        Method to add an edge to the graph.
        Process:
            Type check's the weight. Verifies the source and destination
            exist in the graph already. Adds edge to source and
            destination vertices.
        Args:
            self(Graph): self
            src(str): The source vertex
            dest(str): The destination
            wgt(int/float): The edge weight value
        Returns:
            self(Graph): Returns the graph with new edge
        """
        if isinstance(wgt, (float, int)) is not True:
            raise ValueError("Weight must ve a decimal value.")

        if src in self.graph:
            if dest not in self.graph:
                raise ValueError("Destination '%s' not in graph."%(dest))

            if dest not in self.get_vertex(src).edges:
                self.get_vertex(src).add_edge(dest, wgt)
            else:
                raise ValueError("Edge already present.")
        else:
            raise ValueError("Source '%s' not in graph."%(src))
        return self

    def get_vertex(self, label):
        """
        Method to retrieve specified vertices.
        Process:
            Verifies vertex presence then returns value.
        Args:
            self(Graph): self
            label(str): Label of vertex to be returned
        Returns:
            vertex(Vertex): Returns vertex object
        """
        if label in self.graph:
            return self.graph[label]

    def get_weight(self, src, dest):
        """
        Provides the weight of an edge.
        Process:
            Locates the source, then destination. Returns edge.
        Args:
            self(Graph): self
            src(str): The edge source
            dest(str): The edge destination
        Returns:
            weight(int/float): The edge weight
        """
        if src in self.graph:
            return self.graph[src].get_edge_weight(dest)
        else:
            raise ValueError("Source vertex not present.")

    def dfs(self, starting_vertex):
        """
        Creates iterator for depth-first searches.
        Process:
            Recurses into the graph to provide depth-first results.
        Args:
            self(Graph): self
            starting_vertex(Type): The starting point of the search.
        Returns:
            temp(list): Result of recursion.
        """
        temp = list()
        stack = list()

        def recurse(vertex, lyst, stack):
            """
            Recursive function to dig into graph.
            Process:
                Calls itself repetetively to dig into graph.
            Args:
                vertex(str): Next vertex label
                lyst(list): The result list
                stack(list): The stack for depth
            Returns:
                lyst(list): Returns the modified list when complete
            """
            vert = stack.pop()
            lyst.append(vert)
            for item in self.graph[vert].edges:
                stack.append(item.destination)

            for item in stack:
                return recurse(item, lyst, stack)
            return lyst

        if starting_vertex in self.graph.keys():
            stack.append(starting_vertex)
            temp = recurse(starting_vertex, temp, stack)
        else:
            raise ValueError("Starting vertex not in graph.")

        return temp

    def bfs(self, starting_vertex):
        """
        Creates iterator for breadth-first searches.
        Process:
            Recurses into the graph to provide breadth-first results.
        Args:
            self(Graph): self
            starting_vertex(Type): The starting point of the search.
        Returns:
            temp(list): Result of recursion.
        """
        temp = list()

        def recurse(vertex, lyst, position):
            """
            Recursive function to sequence into graph.
            Process:
                Calls itself repetetively to sequence into graph.
            Args:
                vertex(str): Next vertex label
                lyst(list): The result list
                position(int): Position to allow incrementation
            Returns:
                lyst(list): Returns the modified list when complete
            """
            for item in self.graph[vertex].edges:
                if item is None:
                    pass
                else:
                    lyst.append(item.destination)

            if position + 1 < len(lyst):
                position += 1
                return recurse(lyst[position], lyst, position)
            else:
                return lyst

        if starting_vertex in self.graph.keys():
            temp.append(starting_vertex)
            temp = recurse(starting_vertex, temp, 0)
        else:
            raise ValueError("Starting vertex not in graph.")

        return temp

    def dijkstra_shortest_path(self, src, dest=None):
        """
        Method to use Dijkstra's algorithm to traverse graph.
        Process:
            Checks if "dest" is none. Selects the appropriate function.
        Args:
            self(Graph): self
            src(str): The source label
            dest(str/None)" The destination label
        Returns:
            fuction(func): Returns result of called function
        """
        def dijkstra_no_dest(src):
            """
            Uses Dijksra's algorithm without a destination. Will call
            alternate form to provide a dictionary of all destination
            results.
            Process:
                Verifies "src" as in the graph, then calls dijkstra_dest()
                for every vertex connected to the source.
            Args:
                src(str): The source vertex
            Returns:
                fuctnion(func): Returns the result of the function call
            """
            if src not in self.graph.keys():
                raise ValueError("Source not in graph.")

            result = {}

            for vertex in self.graph.keys():
                result[vertex] = dijkstra_dest(src, vertex)

            return result

        def dijkstra_dest(src, dest):
            """
            Uses Dijksra's algorithm with a destination.
            Process:
                Verifies "src" and "dest" as in the graph, then determine
                the cost and predicessors of each vertex. Lastly it back-tracks
                from the destination to the source and returns the path, length,
                and result.
            Args:
                src(str): The source vertex
                dest(str): The destination vertex
            Returns:
                fuctnion(func): Returns the result of the function call
            """
            if src not in self.graph.keys():
                raise ValueError("Source not in graph.")
            if dest is not None and dest not in self.graph.keys():
                raise ValueError("Destination not in graph.")

            path = list()
            length = 0
            result = None
            self.graph[src].set_cost(0)
            self.graph[src].set_visit(True)
            self.graph[src].set_pred(None)

            def set_path(vertex):
                """
                Works through all the vertices recursively to set the
                cost, predicessor, and visit status.
                Process:
                    Recursively calls itself to travers the graph and
                    update the cost, predicessor and visit accordingly.
                Args:
                    vertex(Vertex): The current vertex to process
                Returns:
                    None(None): None
                """
                for item in vertex.edges:
                    if self.graph[item.destination].get_cost() > (vertex.get_cost() + item.weight):
                        self.graph[item.destination].set_cost(vertex.get_cost() + item.weight)
                        self.graph[item.destination].set_pred(vertex.label)
                        self.graph[item.destination].set_visit(True)
                    if self.graph[item.destination] is not None:
                        set_path(self.graph[item.destination])

            for vertex in self.graph.keys():
                set_path(self.graph[vertex])

            def test_path(src, vertex):
                """
                Tests the Dijkstra's algorithm call to verify a link between
                the source and destination vertices.
                Process:
                    Cycles from the destination to the source. If it reaches False
                    False is returned to signify no link. If the source is met then
                    True is returned.
                Args:
                    src(str): The source label
                    vertex(str): The current vertex being processed
                Returns:
                    bool(bool): True/False depending on whether source connects
                    to the destination
                """
                if vertex is False:
                    return False
                elif vertex is src:
                    return True
                else:
                    return test_path(src, self.graph[vertex].get_pred())

            def get_path(path, src, vertex):
                """
                Retrieves the iteration path once it is ready.
                Process:
                    Works from the destination to the source to reproduce
                    the created path.
                Args:
                    path(list): The resulting path
                    src(str): The source label
                    vertex(str): The vertex label for the currently 
                    processed vertex
                Returns:
                    path(list): Returns the resulting path
                """
                if vertex is not src:
                    path.append(vertex)
                    return get_path(path, src, self.graph[vertex].get_pred())
                else:
                    path.append(src)
                    return path

            if dest is not None:
                test = test_path(src, dest)
                if test is False:
                    result = (math.inf, list())
                else:
                    path = get_path(path, src, dest)
                    length = self.graph[dest].get_cost()
                    result = (length, path)

            self.clear_kijkstra()
            return result

        if dest is None:
            return dijkstra_no_dest(src)
        else:
            return dijkstra_dest(src, dest)

    def clear_kijkstra(self):
        """
        Resets the cost, predecessor, and visit values after
        initial calculations.
        Process:
            Sets the cost to math.inf, the predecessor to False, and
            the visit to False.
        Args:
            self(Graph): self
        Returns:
            None(None): None
        """
        for vertex in self.graph.keys():
            self.graph[vertex].set_cost(math.inf)
            self.graph[vertex].set_pred(False)
            self.graph[vertex].set_visit(False)

class Vertex():          # Removed "object" at pylint's request. Using python 3+
    """ Vertex class to create vertex objects. """
    def __init__(self, label):
        """
        Initializer method to create vertex objects.
        Process:
            Creates a new class object using the provided label
            and preset edges, visit status, cost, and predecessor.
        Args:
            self(Vertex): self
            label(str): The label intended for each Vertex object
        Returns:
            None(None): None
        """
        self.label = label
        self.edges = list()
        self.visited = False
        self.cost = math.inf
        self.pred = False

    def __str__(self):
        """
        A method to provide a string representation of the vertex.
        Process:
            Generates the label and contained edge values of the vertex,
            then returns them..
        Args:
            self(Vertex): self
        Returns:
            temp(str): String representation of the vertex
        """
        temp = ""
        flag = 0

        temp += "%1s       ["%(self.label)

        for item in self.edges:
            if flag == 0:
                temp += "%s"%(item)
                flag += 1
            else:
                temp += ", %s"%(item)

        temp += "]\n"
        return temp

    def add_edge(self, dest, wgt):
        """
        Adds edge to vertex.
        Process:
            Adds an Edge object with the destination and
            weight to the vertex edge list.
        Args:
            self(Vertex): self
            dest(str): The edge destination
            wgt(int/float): The edge weight value
        Returns:
            None(None): None
        """
        self.edges.append(Edge(self, dest, wgt))

    def set_label(self, label):
        """
        Sets the vertex label.
        Process:
            Updates the vertex label using the provided label.
        Args:
            self(Vertex): self
            label(str): New label value
        Returns:
            None(None): None
        """
        self.label = label

    def set_visit(self, value):
        """
        Sets the vertex visit.
        Process:
            Updates the vertex visit using the provided status.
        Args:
            self(Vertex): self
            value(str): New visit value
        Returns:
            None(None): None
        """
        self.visited = value

    def set_cost(self, value):
        """
        Sets the vertex cost.
        Process:
            Updates the vertex cost using the provided value.
        Args:
            self(Vertex): self
            value(int/float): New cost value
        Returns:
            None(None): None
        """
        self.cost = value

    def set_pred(self, value):
        """
        Sets the vertex predecessor.
        Process:
            Updates the vertex predecessor using the provided value.
        Args:
            self(Vertex): self
            value(str): New predecessor value
        Returns:
            None(None): None
        """
        self.pred = value

    def get_label(self):
        """
        Gets vertex label.
        Process:
            returns self.label.
        Args:
            self(Vertex): self
        Returns:
            self.label(str): Returns vertex label
        """
        return self.label

    def get_visit(self):
        """
        Gets vertex visit.
        Process:
            returns self.visited.
        Args:
            self(Vertex): self
        Returns:
            self.visit(bool): Returns vertex visit
        """
        return self.visited

    def get_cost(self):
        """
        Gets vertex cost.
        Process:
            returns self.cost.
        Args:
            self(Vertex): self
        Returns:
            self.cost(int/float): Returns vertex cost
        """
        return self.cost

    def get_pred(self):
        """
        Gets vertex predecessor.
        Process:
            returns self.pred.
        Args:
            self(Vertex): self
        Returns:
            self.pred(str): Returns vertex predecessor
        """
        return self.pred

    def get_edge_weight(self, dest):
        """
        Gets vertex edge weight.
        Process:
            returns item.weight or math.inf if the source and destination
            are/are not linked.
        Args:
            self(Vertex): self
        Returns:
            item.weight/math.inf(int/float): Returns vertex edge weight
        """
        for item in self.edges:
            if item.destination == dest:
                return int(item.weight)
        return math.inf

class Edge():          # Removed "object" at pylint's request. Using python 3+
    """ Edge class to create edge objects. """
    def __init__(self, src, dest, wgt, dir=None):
        """
        Initializer method to create edge objects.
        Process:
            Creates an Edge type object with a source, destination,
            weight, direction, and visit status.
        Args:
            self(Edge): self
            src(str): Source of the edge
            dest(str): Destination of the edge
            wgt(int/float): Weight of the edge
            dir(str): Direction of the edge (not used)
        Returns:
            None(None): None
        """
        self.source = src
        self.destination = dest
        self.weight = float(wgt)
        self.direction = dir
        self.visited = False

    def __str__(self):
        """
        Creates a string representation of the edge.
        Process:
            Creates a string using the destination and weight of
            the edge.
        Args:
            self(Edge): self
        Returns:
            edge(str): Returns string of edge values
        """
        return "('%s', %2.1f)"%(self.destination, self.weight)

    def set_source(self, source):
        """
        Sets edge source.
        Process:
            sets edge source using provided "source".
        Args:
            self(Edge): self
            source(str): Source of the edge
        Returns:
            None(None): None
        """
        self.source = source

    def set_destination(self, dest):
        """
        Sets edge destination.
        Process:
            sets edge destination using provided "dest".
        Args:
            self(Edge): self
            dest(str): Destination of the edge
        Returns:
            None(None): None
        """
        self.destination = dest

    def set_weight(self, wgt):
        """
        Sets edge weight.
        Process:
            sets edge weight using provided "wgt".
        Args:
            self(Edge): self
            wgt(int/float): Weight of the edge
        Returns:
            None(None): None
        """
        self.weight = wgt

    def get_weight(self):
        """
        Gets edge weight.
        Process:
            gets edge weight then returns it.
        Args:
            self(Edge): self
        Returns:
            self.weight(int/float): The weight of the edge
        """
        return self.weight
