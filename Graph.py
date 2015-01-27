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

G = Graph()
for node in range(ord('A'), ord('G')):
    G.add_vertex(Vertex(chr(node)))

G.add_edge(Edge('A','B',4))
G.add_edge(Edge('A','C',2))
G.add_edge(Edge('B','C',5))
G.add_edge(Edge('B','D',10))
G.add_edge(Edge('C','E',3))
G.add_edge(Edge('E','D',4))
G.add_edge(Edge('D','F',11))

F = Graph()
F.add_vertex(Vertex('A', 0.0, 8.0))
F.add_vertex(Vertex('B', 6.0, 8.0))
F.add_vertex(Vertex('C', 0.0, 0.0))
F.add_vertex(Vertex('D', 6.0, 0.0))
F.add_vertex(Vertex('E', 1.5, 8.0))
F.add_vertex(Vertex('F', 3.0, 4.0))
F.add_vertex(Vertex('G', 4.5, 2.0))

F.add_edge(Edge('A','B',6))
F.add_edge(Edge('B','D',8))
F.add_edge(Edge('A','C',8))
F.add_edge(Edge('C','D',6))
F.add_edge(Edge('A','E',2.5))
F.add_edge(Edge('E','F',2.5))
F.add_edge(Edge('F','G',2.5))
F.add_edge(Edge('G','D',2.5))

