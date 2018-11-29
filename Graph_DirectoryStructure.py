from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, u, v):
        self.graph[u].append(v)


if __name__ == '__main__':
    input = ["var/tmp/foo", "var/tmp/boo", "var/tmp/x", "var/tmp/x/y", "var/tmp/x/z", "var/lib/m", "var/lib/n", "var/std/", "var/bar/test"]

    graph = Graph()

    for path in input:
        dirs = path.split('/')
        for i in range(0, len(dirs)-1):
            if dirs[i+1] not in graph.graph[dirs[i]]:
                graph.add(dirs[i], dirs[i+1])

    print graph.graph
