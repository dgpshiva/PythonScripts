from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def detectCycleUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.detectCycleUtil(i, visited, recStack):
                    return True
            elif recStack[i]:
                return True

        recStack[v] = False
        return False


    def detectCycle(self):
        visited = [False] * self.V
        recStack = [False] * self.V

        for i in range(0, self.V):
            if not visited[i]:
                if self.detectCycleUtil(i, visited, recStack):
                    return True

        return False


g = Graph(4)

# Cycle - true
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
# print g.detectCycle()

# Cycle - false
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
print g.detectCycle()


