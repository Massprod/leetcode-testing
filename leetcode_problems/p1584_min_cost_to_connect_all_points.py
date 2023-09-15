# You are given an array points representing integer coordinates of some points on a 2D-plane,
#  where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
#  |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected.
# All points are connected if there is exactly one simple path between any two points.
# ----------------------------
# 1 <= points.length <= 1000
# -10 ** 6 <= xi, yi <= 10 ** 6
# All pairs (xi, yi) are distinct.
from random import randint


def min_cost_connect(points: list[list[int]]) -> int:
    # working_sol (86.83%, 68.55%) -> (893ms, 90.45mb)  time: O(nC2 * log (nC2)) | space: O(nC2)
    # Searching for a MST with FindUnion.
    # (manh_distance, point1, point2)
    all_edges: list[tuple[int, int, int]] = []
    # f -> first point, s -> second point.
    for f in range(len(points)):
        for s in range(f + 1, len(points)):
            all_edges.append(
                (abs(points[f][0] - points[s][0]) + abs(points[f][1] - points[s][1]), f, s)
            )
    # Sort by distance, ascending.
    all_edges.sort(key=lambda x: x[0])
    parent: list[int] = [_ for _ in range(len(points))]
    ranks: list[int] = [1 for _ in range(len(points))]

    def find(node: int) -> int:
        # Find representative of the set that
        #  node is an element of.
        if parent[node] == node:
            return node
        parent[node] = find(parent[node])
        return parent[node]

    def union(node1: int, node2: int) -> None:
        # Find representatives for both nodes.
        node1_set = find(node1)
        node2_set = find(node2)
        # If they're already in the same set, ignore.
        if node1_set == node2_set:
            return
        # If they're in different sets.
        # Put smaller ranked set under bigger ranked set.
        if ranks[node1_set] < ranks[node2_set]:
            parent[node1_set] = node2_set
        elif ranks[node1_set] > ranks[node2_set]:
            parent[node2_set] = node1_set
        # If they're ranks are the same, we can put them in any way.
        # node1_set|node2_set <- doesn't matter.
        elif ranks[node1_set] == ranks[node2_set]:
            parent[node2_set] = node1_set
            # But increase rank of one we placed set under.
            ranks[node1_set] = ranks[node1_set] + 1

    mst: int = 0
    used_edges: int = 0
    for distance, p_1, p_2 in all_edges:
        # Same set -> discard.
        if find(p_1) == find(p_2):
            continue
        # Count edge for MST.
        mst += distance
        # Assign them in the same set.
        union(p_1, p_2)
        used_edges += 1
        # ! If there are n vertices in the graph,
        #   then each spanning tree has n − 1 edges. !
        # MST -> MinimumSpanningTree, applies to it as well.
        if used_edges == (len(points) - 1):
            break
    return mst


# Time complexity: O(nC2 * log (nC2)) -> creating all edges for every point, nested loops with (n) + (n - 1) max iters.
# n - len of input_array^^|  => O(n * log n) -> ! The maximum number of edges possible in a single graph with ‘n’
#                            vertices is nC2 where nC2 = n(n – 1)/2. ! -> we're creating all edges and sorting them =>
#                            => O(nC2 * log (nC2)) ->
#                            -> ! The two techniques - path compression with the union by rank/size,
#                               the time complexity will reach nearly constant time.
#                               It turns out, that the final amortized time complexity is O(α(n)),
#                                where α(n) is the inverse Ackermann function,
#                                which grows very steadily (it does not even exceed for n<10 ** 600  approximately).
#                               ! First time met FindUnion problem, so it's made from gfg guidance.
#                            Sorting edges is dominating, so it's => O(nC2 * log (nC2)), where - nC2 = n(n – 1)/2.
# Auxiliary space: O(nC2) -> we're creating and storing all edges => O(nC2).
# ----------------------------
# FindUnion problem.
# https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
# 1) Create all edges, and sort them in ascending.
# 2) Create Find and Union function to check cycles.
# 3) Try to add edge, if it's connecting to a cycle, discard.
# 3+) Repeat until there's (n - 1) edges used.


test: list[list[int]] = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
test_out: int = 20
assert test_out == min_cost_connect(test)

test = [[3, 12], [-2, 5], [-4, 1]]
test_out = 18
assert test_out == min_cost_connect(test)

test = []
test_point: list[int, int] = []
points_used: set[tuple[int, int]] = set()
for _ in range(1000):
    test_point = [randint(-10 ** 6, 10 ** 6), randint(-10 ** 6, 10 ** 6)]
    while tuple(test_point) in points_used:
        test_point = [randint(-10 ** 6, 10 ** 6), randint(-10 ** 6, 10 ** 6)]
    test.append(test_point)
print(test)
