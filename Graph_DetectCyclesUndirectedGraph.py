from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
    

    def detectCycleUtil(self, v, parent, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.detectCycleUtil(i, v, visited):
                    return True
            elif parent != i:
                return True
        
        return False

    
    def detectCycle(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.detectCycleUtil(i, -1, visited):
                    return True
        
        return False



if __name__ == '__main__':
    g = Graph(5)

    # # Cycle - true
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(0, 3)
    # g.addEdge(1, 0)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 1)
    # g.addEdge(3, 0)
    # g.addEdge(3, 4)
    # g.addEdge(4, 3)
    # print g.detectCycle()

    # Cycle - false
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    g.addEdge(3, 0)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    print g.detectCycle()



