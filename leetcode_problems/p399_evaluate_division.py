# You are given an array of variable pairs equations and an array of real numbers values,
#  where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
# Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query
#  where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid.
#  You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined,
#  so the answer cannot be determined for them.
# --------------------
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # working_sol (94.30%, 72.8%) -> (34ms 16.4mb)  time: O(n * k) | space: O(n + k)
    # ! The input is always valid ! => a/b = val, b/a = 1/val
    # ! a = val * b , b = a/val
    #   b/a = (a/val) / (val * b) == (a/val) / (val * (a/val) == 1/val
    #   b/c = val2, c/b = 1/val2  !
    # So -> a/c = a/b * b/c <- we just need DFS through correct path
    #   from a to c and multiply everything on this path.
    # And if path didn't found => impossible == -1.
    undirect_graph: dict[str: dict[str: int]] = {}
    for x in range(len(equations)):
        # Create undirected Graph with all variables.
        var1: str = equations[x][0]
        var2: str = equations[x][1]
        val: float = values[x]
        if var1 not in undirect_graph:
            undirect_graph[var1] = {var2: val}
        else:
            undirect_graph[var1][var2] = val
        if var2 not in undirect_graph:
            undirect_graph[var2] = {var1: 1 / val}
        else:
            undirect_graph[var2][var1] = 1 / val

    def dfs(node: str, target: str, path: float) -> float | None:
        # If correct Divisor present in current Dividend,
        #  correct path is found.
        if target in undirect_graph[node]:
            return undirect_graph[node][target] * path

        for edge in undirect_graph[node]:
            # Skipping visited.
            if edge not in visited:
                visited.add(edge)
                # a/c = a/b * b/c -> So we need to multiply everything on the path.
                if correct := dfs(edge, target, path * undirect_graph[node][edge]):
                    return correct
    # Standard BFS approach.
    new_values: list[float] = []
    visited: set[str] = set()
    for dividend, divisor in queries:
        visited.clear()
        visited.add(dividend)
        # If both ends are present, then there can be a correct path.
        if dividend in undirect_graph and divisor in undirect_graph:
            # a/a == 1, insta return. And we can't make this path anyway.
            if dividend == divisor:
                new_values.append(1)
                continue
            # Walrus is a good option, cuz return cant be 0.
            # We can't divide by 0 and Float result of division is never 0.
            if found := dfs(dividend, divisor, 1):
                new_values.append(found)
                continue
        # If there's no path ->
        # ! answer cannot be determined, return -1.0. !
        new_values.append(-1.0)

    return new_values


# Time complexity: O(n * k) -> guess, worst case is we're having something like [['a','b']['b','c'] ... ['y','z']] ->
# n - len of input_equations^^| -> so 'a' connected to 'z' in the end, and every query we have is ['a', 'z'] ->
# k - len of input_queries^^| -> we will DFS for every query in the same path, and traverse every node in equations =>
#                             => so it's should be correct to say O(n * k).
# Auxiliary space: O(n + k) -> stack can be with size of n, when we DFS this^^ worst case => O(n) -> and for every
#                          query we will at least store 1 value, so it's => O(k).
#                          Only problem is, should we ignore Stack? Like queries can have 1 question, while
#                          equations is having 20 then stack will dominate. Better to leave O(k + n).
#                          Actually I missed out dictionary part, we're storing x2 of original list into dictionary.
#                          So it's O(2n) anyway => O(n + k).
# --------------------
# Create undirected Graph with all given equations and search in them?
# Like -> ! The input is always valid ! -> a/b = val, b/a = 1/val <- a = val * b , b = a/val ,
# b/a = (a/val) / (val * b) == (a/val) / (val * (a/val) == 1/val
# b/c = val2, c/b = 1/val2
# So -> a/c = a/b * b/c <- we just need DFS through correct path from a to c and multiply everything.
# But, how to get this correct path? Actually it's DFS task Tag, so it's just Check everything. Let's try.


test_eq: list[list[str]] = [["a", "b"], ["b", "c"]]
test_va: list[float] = [2.0, 3.0]
test_qu: list[list[str]] = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
test_out: list[float] = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
assert test_out == calc_equation(test_eq, test_va, test_qu)

test_eq = [["a", "b"], ["b", "c"], ["bc", "cd"]]
test_va = [1.5, 2.5, 5.0]
test_qu = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
test_out = [3.75000, 0.40000, 5.00000, 0.20000]
assert test_out == calc_equation(test_eq, test_va, test_qu)

test_eq = [["a", "b"]]
test_va = [0.5]
test_qu = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
test_out = [0.50000, 2.00000, -1.00000, -1.00000]
assert test_out == calc_equation(test_eq, test_va, test_qu)
