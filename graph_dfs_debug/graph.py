"""
Simple graph implementation compatible with BokehGraph class.
"""

#https://www.programiz.com/python-programming/set

class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(start)
        if bidirectional:
            self.vertices[end].add(end)

    # address issues in dfs
    def dfs(self, start, target):
        stack = []
        stack.append(start)

        visited = set(stack)

        while len(stack) > 0:
            removed = stack.pop()
            print("removed vertex: ", removed)
            if removed == target:
                return True
            visited.add(removed)
            for vertex in self.vertices[removed].edges:
                if vertex not in visited:
                    stack.append(vertex)
        return False

    def graph_rec(self, start, target=None):
        x = set()
        x.append(start)
        for v in self.vertices[start]:
            graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
