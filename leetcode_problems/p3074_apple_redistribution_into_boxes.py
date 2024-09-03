# You are given an array apple of size n and an array capacity of size m.
# There are n packs where the ith pack contains apple[i] apples.
# There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
# Note that, apples from the same pack can be distributed into different boxes.
# ----------------------------
# 1 <= n == apple.length <= 50
# 1 <= m == capacity.length <= 50
# 1 <= apple[i], capacity[i] <= 50
# The input is generated such that it's possible to redistribute packs of apples into boxes.


def minimum_boxes(apple: list[int], capacity: list[int]) -> int:
    # working_sol (71.57%, 69.41%) -> (41ms, 16.47mb)  time: O(n * log n) | space: O(n)
    all_apples: int = sum(apple)
    out: int = 0
    # Use the highest capacity first == best tactic.
    capacity.sort(reverse=True)
    for box in capacity:
        all_apples -= box
        out += 1
        if 0 >= all_apples:
            break
    return out


# Time complexity: O(n * log n) <- n - length of the input array `capacity`, k - length of the input array `apple`
# Always traversing `apple` once, to get a sum of the elements => O(k).
# Always sorting `capacity` to get highest boxes first => O(n * log n + k).
# Extra traversing `capacity` to get # of boxes => O(n * log n + k + n).
# ----------------------------
# Auxiliary space: O(n).
# `sort` <- takes O(n) by itself => O(n).


test: list[int] = [1, 3, 2]
test_capacity: list[int] = [4, 3, 1, 5, 2]
test_out: int = 2
assert test_out == minimum_boxes(test, test_capacity)

test = [5, 5, 5]
test_capacity = [2, 4, 2, 7]
test_out = 4
assert test_out == minimum_boxes(test, test_capacity)
