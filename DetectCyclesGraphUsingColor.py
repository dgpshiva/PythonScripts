from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def detectCyclesUtil(self, v, color):
        color[v] = "GRAY"

        for i in self.graph[v]:
            if color[i] == "WHITE" and self.detectCyclesUtil(i, color) == True:
                return True
            elif color[i] == "GRAY":
                return True

        color[v] = "BLACK"
        return False

    def detectCycles(self):
        color = ["WHITE"] * self.V

        for i in range(0, self.V):
            if color[i] == "WHITE":
                if self.detectCyclesUtil(i, color) == True:
                    return True

        return False

g = Graph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)

print g.detectCycles()