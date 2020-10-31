class Graph:
    def __init__(self, graph={}):
         self.graph = graph

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        edges = []

        for values in self.graph.values():
            for link in values:
                edges.append(link)

        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, edge):
        (vertex1, vertex2) = tuple(edge)

        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]
