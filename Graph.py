'''
Vertex/Edge/Graph Data Structures
Supports weighted edges
Supports x and y coordinates for verticies
Default Graph is undirected, for undirected comment out line 43
'''

class Vertex():
    def __init__(self, label, x=None, y=None):
        self.label = label
        self.edges = []
        self.x = x
        self.y = y

    def add_edge(self,edge):
        self.edges.append(edge)

    def edges_out(self):
        return self.edges

    def location(self):
        return (self.x,self.y)

class Edge():
    def __init__(self,A,B,weight=None):
        self.src = A
        self.dest = B
        self.weight = weight

class Graph():
    def __init__(self):
        self.verticies = {}

    def add_vertex(self,A):
        self.verticies[A.label] = A

    def has_vertex(self,A):
        return A in self.verticies.keys()

    def add_edge(self,edge):
        if self.has_vertex(edge.src) and self.has_vertex(edge.dest):
            self.verticies[edge.src].add_edge(edge)
            self.verticies[edge.dest].add_edge(Edge(edge.dest, edge.src, edge.weight))

    def edges_out(self, A):
        if self.has_vertex(A):
            return self.verticies[A].edges_out()
        else:
            return None

    def toString(self):
        toString = {}
        for vertex in self.verticies:
            toString[vertex] = []
            for edge in self.verticies[vertex].edges_out():
                if edge.weight:
                    toString[vertex].append((edge.dest,edge.weight))
                else:
                    toString[vertex].append(edge.dest)
        return toString 

example = Graph()
example.add_vertex(Vertex('A', 0.0, 8.0))
example.add_vertex(Vertex('B', 6.0, 8.0))
example.add_vertex(Vertex('C', 0.0, 0.0))
example.add_vertex(Vertex('D', 6.0, 0.0))
example.add_vertex(Vertex('E', 1.5, 6.0))
example.add_vertex(Vertex('F', 3.0, 4.0))
example.add_vertex(Vertex('G', 4.5, 2.0))
example.add_vertex(Vertex('H', 3.0, 8.0))
example.add_vertex(Vertex('I', 0.0, 4.0))
example.add_vertex(Vertex('J', 6.0, 4.0))
example.add_vertex(Vertex('K', 3.0, 0.0))
example.add_vertex(Vertex('L', 4.5, 6.0))
example.add_vertex(Vertex('M', 1.5, 2.0))

example.add_edge(Edge('A','H',4))
example.add_edge(Edge('A','I',3))
example.add_edge(Edge('B','H',4))
example.add_edge(Edge('F','H',4))
example.add_edge(Edge('I','F',3))
example.add_edge(Edge('I','C',4))
example.add_edge(Edge('B','J',4))
example.add_edge(Edge('J','D',4))
example.add_edge(Edge('J','F',3))
example.add_edge(Edge('K','C',3))
example.add_edge(Edge('K','D',3))
example.add_edge(Edge('K','F',4))

example.add_edge(Edge('A','E',2.5))
example.add_edge(Edge('E','F',2.5))
example.add_edge(Edge('F','G',2.5))
example.add_edge(Edge('G','D',2.5))
