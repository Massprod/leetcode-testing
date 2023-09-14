# You are given a list of airline tickets where tickets[i] = [fromi, toi]
#  represent the departure and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus,
#  the itinerary must begin with "JFK".
# If there are multiple valid itineraries, you should return the itinerary that
#  has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary.
# You must use all the tickets once and only once.
# -----------------------
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi


def find_itinerary(tickets: list[list[str]]) -> list[str]:
    # working_sol (96.38%, 87.47%) -> (76ms, 16.8mb)  time: O(n * log n) | space: O(n)
    # Create directed graph.
    dir_graph: dict[str, list[str]] = {}
    for ticket in tickets:
        if ticket[0] in dir_graph:
            dir_graph[ticket[0]].append(ticket[1])
            continue
        dir_graph[ticket[0]] = [ticket[1]]
    # Sort edges in lexicographically descending order.
    # Then we always will be able to use the smallest option.
    for value in dir_graph.values():
        value.sort(reverse=True)
    itinerary: list[str] = []

    def dfs(node: str) -> None:
        # Check all edges.
        while node in dir_graph and dir_graph[node]:
            dfs(dir_graph[node].pop())
        # Record backtrack path of DFS.
        itinerary.append(node)

    dfs('JFK')
    # Used backtracking, so we need to reverse it.
    return itinerary[::-1]


# Time complexity: O(n * log n) -> worst case == every pair is cycled, so we will always add FROM and TO as
# n - len of input_array^^|  2 different values in 2 different keys -> so dict(tickets) will have keys with
#                            list of the same size as n -> we're sorting them in_place => O(n * log n) ->
#                            -> dfs to check all vertexes and edges, in worst case it's just a cycle with
#                            2 endpoints, like: ['JFK', 'MUC'] * 100, ['MUC', 'JFK'] * 100 ->
#                            -> actually, no matter the vertexes and edges we're always checking all pairs of tickets,
#                            doesn't matter if they lead somewhere => O(n) ->
#                            -> extra reversing backtrack path of DFS => O(n).
# Auxiliary space: O(n) -> worst case == ['JFK', 'MUC'] * 100, ['MUC', 'JFK'] * 100 -> we will store every destination,
#                          we have cycle, so it's both 'JFK' and 'MUC', as edges => O(n) ->
#                          -> every pair from input_array == at least 1 edge, so STACK + itinerary, should be linear.
# -----------------------
# Ok. We actually need to use backtrack and add nodes in reverse. With reversing them in the end.
# Add node in itinerary if it doesn't have edges, and check all edges if it has them.
# Literally DFS definition, but I was trying to record path from 1 -> last from beginning. Good exp anyway.
# At least sorting and using minimum edge was correct. But adding of nodes with no edges was incorrect.
# -----------------------
# Ok. We can't just use minimal lexi option for every edge. Fixed this part with first using edges which can lead
# to other vertexes, and single ones later. But it's still incorrect.
# We need to check all edges which leading to a cycle and only then add edges which leads to some endpoint break.
# Nah. Can't make it correctly. Always adding first endpoint route  which doesn't lead to cycle, and it actually
# should be second. Can't maintain it correctly...
# -----------------------
# 100% DFS problem, and only question is how to make this in ! smallest lexical order when read as a single string !.
# Cuz we can make string and remember it. But then we will need to rebuild itinerary again with other sequence.
# What we need essentially? Build sequence using SMALLEST lexico options right?
# Cuz lexico_smaller is smaller on first symbol_diff, so we can just take the smallest edge from presented?
# Like -> create directed_graph, cuz we're given directions and with DFS use the SMALLEST edge to go to?
# We will use every edge, cuz DFS. And it should be correct smallest_lexico itinerary.
# ! You must use all the tickets once and only once. ! <- but we have same edges in different tickets,
# so we can have cycles. Delete used? We need only 1 path, and it's harder to store visited with cycles.
# Just delete edges we already used, should be fine.
# Otherwise, it's extra dictionary -> (every vertex: set with visited edges), and we don't actually need it.


test: list[list[str]] = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
test_out: list[str] = ["JFK", "MUC", "LHR", "SFO", "SJC"]
assert test_out == find_itinerary(test)

test = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
test_out = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
assert test_out == find_itinerary(test)

test = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
test_out = ["JFK", "NRT", "JFK", "KUL"]
assert test_out == find_itinerary(test)

test = [
    ["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"], ["TIA", "AUA"],
    ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"],
    ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]
]
test_out = [
    "JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU",
    "JFK", "AXA", "EZE", "TIA", "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"
]
assert test_out == find_itinerary(test)
