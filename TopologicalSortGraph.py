from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.stack = []
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topologicalSortUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited)

        self.stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        for i in range(0, self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited)

if __name__ == '__main__':
    g= Graph(6)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(5, 2)
    g.addEdge(5, 0)

    g.topologicalSort()

    print g.stack
