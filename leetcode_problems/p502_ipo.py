# Suppose LeetCode will start its IPO soon.
# In order to sell a good price of its shares to Venture Capital,
#  LeetCode would like to work on some projects to increase its capital before the IPO.
# Since it has limited resources, it can only finish at most k distinct projects before the IPO.
# Help LeetCode design the best way to maximize its total capital after finishing
#  at most k distinct projects.
# You are given n projects where the ith project has a pure profit profits[i]
#  and a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project,
#  you will obtain its pure profit and the profit will be added to your total capital.
# Pick a list of at most k distinct projects from given projects to maximize your final capital,
#  and return the final maximized capital.
# The answer is guaranteed to fit in a 32-bit signed integer.
# ----------------------
# 1 <= k <= 10 ** 5
# 0 <= w <= 10 ** 9
# n == profits.length
# n == capital.length
# 1 <= n <= 10 ** 5
# 0 <= profits[i] <= 10 ** 4
# 0 <= capital[i] <= 10 ** 9
import heapq
from random import randint


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    # working_sol (95.3%, 84.23%) -> (735ms, 41mb)  time: O(n * log n) | space: O(n)
    # Maximized heap with profits of projects we can buy.
    affordable: list[int] = []
    heapq.heapify(affordable)
    # (capital, profit) pairs for every project.
    max_price: int = 0
    projects: list[tuple[int, int]] = []
    for x in range(len(profits)):
        projects.append((capital[x], profits[x]))
        max_price = max(max_price, capital[x])
    projects.sort()
    # We can buy anything, just take most profitable projects.
    if w >= max_price:
        for y in range(len(profits) - 1, len(profits) - k - 1, - 1):
            w += projects[y][1]
        return w
    index: int = 0
    while k:
        # Add every project we can afford into maximized heap.
        while index < len(projects) and projects[index][0] <= w:
            heapq.heappush(affordable, projects[index][1] * -1)
            index += 1
        # Always buying maximum profit from all projects we can afford.
        if affordable:
            w += heapq.heappop(affordable) * -1
            k -= 1
            continue
        # If we can't afford any project, we can't continue.
        # Even if 'k' is not exhausted.
        break
    return w


# Time complexity: O(n * log n) -> sorting dominates everything => O(n * log n).
# n - len of input arrays, they're equal^^|
# Auxiliary space: O(n) -> extra list with all project pairs => O(n).
# ----------------------
# Ok. Profits was questionable, do we get full money back and + profits or just profit.
# Tested -> we always get ALL money we pay to purchase something and + profit. No commission or w.e.
# So it's just BUY the lowest price, but with BIGGEST profit. And im already did similar with heap.
# They bound by indexes, so we need to combine them, sort ascending and add everything we can afford into a heap.
# Then we just take BIGGEST profit from maximized_heap and use it. Get profit and try to buy something else.
# With same logic, but there's I guess why it's HARD. We're allowed to buy and sell instantly.
# So we can just buy something more expensive but more profitable after we sell, cuz capital growth instantly.
# Sell => check what else we can add into a heap with new capital and repeat until K operations done.
# Should be correct.


test_k: int = 2
test_w: int = 0
test_profits: list[int] = [1, 2, 3]
test_capitals: list[int] = [0, 1, 1]
test_out: int = 4
assert test_out == find_maximized_capital(test_k, test_w, test_profits, test_capitals)

test_k = 3
test_w = 0
test_profits = [1, 2, 3]
test_capitals = [0, 1, 2]
test_out = 6
assert test_out == find_maximized_capital(test_k, test_w, test_profits, test_capitals)

test_profits = [randint(0, 10 ** 4) for _ in range(10 ** 3)]
test_capitals = [randint(0, 10 ** 9) for _ in range(10 ** 3)]
print(test_profits)
print('-----------!')
print(test_capitals)
