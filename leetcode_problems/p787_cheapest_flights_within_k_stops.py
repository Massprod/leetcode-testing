# There are n cities connected by some number of flights.
# You are given an array flights where flights[i] = [fromi, toi, pricei]
#  indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k,
#  return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.
# ---------------------
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 10 ** 4
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
from collections import defaultdict, deque


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    # {node: [(edge, price to reach)]}
    graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for _from, _to, _price in flights:
        graph[_from].append((_to, _price))
    que: deque[tuple[int, int] | None] = deque([(src, 0), None])
    costs: list[int | float] = [float('inf') for _ in range(n)]
    while k != -1:
        while que[0]:
            node, price = que.popleft()
            for edge, travel_price in graph[node]:
                new_price: int = price + travel_price
                if new_price <= costs[edge]:
                    que.append((edge, new_price))
                    costs[edge] = new_price
        que.append(que.popleft())
        k -= 1
    if float('inf') == costs[dst]:
        return -1
    return costs[dst]


test: int = 4
test_flights: list[list[int]] = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
test_src: int = 0
test_dst: int = 3
test_k: int = 1
test_out: int = 700
assert test_out == find_cheapest_price(test, test_flights, test_src, test_dst, test_k)

test = 3
test_flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
test_src = 0
test_dst = 2
test_k = 1
test_out = 200
assert test_out == find_cheapest_price(test, test_flights, test_src, test_dst, test_k)

test = 3
test_flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
test_src = 0
test_dst = 2
test_k = 0
test_out = 500
assert test_out == find_cheapest_price(test, test_flights, test_src, test_dst, test_k)
