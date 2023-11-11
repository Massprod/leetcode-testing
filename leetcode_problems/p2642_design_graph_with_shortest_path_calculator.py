# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1.
# The edges of the graph are initially represented by the given array edges where
#  edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge
#  from fromi to toi with the cost edgeCosti.
# Implement the Graph class:
#  - Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
#  - addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost].
#    It is guaranteed that there is no edge between the two nodes before adding this one.
#  - int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2.
#    If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
# --------------------
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1)
# edges[i].length == edge.length == 3
# 0 <= fromi, toi, from, to, node1, node2 <= n - 1
# 1 <= edgeCosti, edgeCost <= 10 ** 6
# There are no repeated edges and no self-loops in the graph at any point.
# At most 100 calls will be made for addEdge.
# At most 100 calls will be made for shortestPath.
import heapq


class Graph:
    # working_sol (64.12%, 76.47%) -> (694ms, 19.5mb)

    def __init__(self, n: int, edges: list[list[int]]):
        # (node: [(edge, distance to travel)])
        # ! n nodes numbered from 0 to n - 1 !
        self.graph: dict[int, list[tuple[int, int]]] = {key: [] for key in range(n)}
        for start, end, cost in edges:
            self.graph[start].append((end, cost))

    def addEdge(self, edge: list[int]) -> None:
        # ! There are no repeated edges and no self-loops in the graph at any point !
        # So, we don't care about anything except adding the new edge.
        # edge == (start, end, distance)
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        # Shortest path in directed graph with weight == Dijkstra's algorithm.
        # (`node`: distance from node1 to this `node`)
        # '-1' for never visited.
        paths: dict[int, int] = {key: -1 for key in self.graph}
        # (distance from node1 to this `node`, `node`)
        que: list[tuple[int, int]] = [(0, node1)]
        # Standard Dijkstra with heap.
        heapq.heapify(que)
        while que:
            node_data: tuple[int, int] = heapq.heappop(que)
            if node_data[1] == node2:
                break
            for edge, distance in self.graph[node_data[1]]:
                path: int = node_data[0] + distance
                # First visit.
                if paths[edge] == -1:
                    paths[edge] = path
                    heapq.heappush(que, (path, edge))
                # New path with lower distance to travel.
                elif paths[edge] > path:
                    paths[edge] = path
                    heapq.heappush(que, (path, edge))
        return paths[node2]


# Time complexity:
#       initiation: O(n + k) -> creating dictionary with 'n' Nodes + populating their edges => O(n + k).
#        n - input value 'n' == number of Nodes(vertices) in graph^^|
#        k - len of input array 'edges' == number of Edges in graph^^|
#       addEdge: O(1) -> always just appending list with a new value => O(1).
#       shortestPath: O(e * log n) -> copying all keys from 'self.graph' => O(n) ->
#        e - current number of edges in graph^^| -> standard Dijkstra with heap => O(e * log n).
#        ! We're not adding new Nodes, but we will add new edges. !
# Auxiliary space:
#       classObject: O(n + e) -> every Node is key + every edge is extra tuple(edge, cost) => O(n + e).
#       addEdge: O(1) -> only expands edges of classObject.
#       shortestPath: O(n + e) -> 'paths' with all Nodes stored + 'que' - with all edges allocated, in the worst case.
