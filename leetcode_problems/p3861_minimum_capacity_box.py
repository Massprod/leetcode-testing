# You are given an integer array capacity, where capacity[i] represents the capacity
#  of the ith box, and an integer itemSize representing the size of an item.
# The ith box can store the item if capacity[i] >= itemSize.
# Return an integer denoting the index of the box with the minimum capacity
#  that can store the item.
# If multiple such boxes exist, return the smallest index.
# If no box can store the item, return -1.
# --- --- --- ---
# 1 <= capacity.length <= 100
# 1 <= capacity[i] <= 100
# 1 <= itemSize <= 100


def minimum_index(capacity: list[int], item_size: int) -> int:
    # working_solution: (100%, 66.02%) -> (0ms, 19.24mb)  Time: O(n) Space: O(1)
    out: int = -1
    used_capacity: int = 101
    for index, box_capacity in enumerate(capacity):
        if item_size > box_capacity:
            continue
        if used_capacity > box_capacity:
            out, used_capacity = index, box_capacity

    return out


# Time complexity: O(n)
# n - length of the input array `capacity`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 5, 3, 7]
test_size: int = 3
test_out: int = 2
assert test_out == minimum_index(test, test_size)

test = [3, 5, 4, 3]
test_size = 2
test_out = 0
assert test_out == minimum_index(test, test_size)

test = [4]
test_size = 5
test_out = -1
assert test_out == minimum_index(test, test_size)
