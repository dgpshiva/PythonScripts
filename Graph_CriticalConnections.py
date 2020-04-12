import collections
class Solution(object):
    def criticalConnections(self, n, connections):
        def makeGraph(connections):
            graph = collections.defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)

        print map(sorted, connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        def dfs(node, depth):
            # if rank[node] >= 1:   # If node numbering starts with 1
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth
            
        # dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
        dfs(1, 1)  # If node numbering starts with 1
        return list(connections)


if __name__ == '__main__':
    s = Solution()
    # print s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
    # print s.criticalConnections(7, [[0,1],[1,3],[3,2],[3,4],[2,5],[5,6],[2,0]])
    print s.criticalConnections(8, [[1,2],[2,4],[4,3],[3,1],[4,5],[3,6],[6,7]])     # If node numbering starts with 1