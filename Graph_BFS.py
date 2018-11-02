from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFSGraph(self, v):
        visited = [False] * len(self.graph)
        queue = []

        visited[v] = True
        queue.append(v)

        while queue:
            v = queue.pop()
            print v,
            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFSGraph(2)



