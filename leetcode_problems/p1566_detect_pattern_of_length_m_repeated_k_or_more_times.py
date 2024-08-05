# Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.
# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values,
#  repeated multiple times consecutively without overlapping.
# A pattern is defined by its length and the number of repetitions.
# Return true if there exists a pattern of length m that is repeated k or more times,
#  otherwise return false.
# -------------------
# 2 <= arr.length <= 100
# 1 <= arr[i] <= 100
# 1 <= m <= 100
# 2 <= k <= 100
from random import randint
from collections import deque


def contains_pattern(arr: list[int], m: int, k: int) -> bool:
    # working_sol (90.97%, 6.86%) -> (31ms, 16.62mb)  time: O(n * (m + l)) | space: O(n * m + n * l + m)
    # { sequence: [array with all options to concat [next_index_for_concat, repeated_occurrences] ] }
    windows: dict[tuple, list[list[int]]] = {}
    left: int = 0
    right: int = m - 1
    # Standard sliding window.
    window: deque[int] = deque(arr[left: m])
    while right < len(arr):
        tup_window: tuple = tuple(window)
        if tup_window in windows:
            concat: bool = False
            for index, option in enumerate(windows[tup_window]):
                # If we can concat another sequence, we use concat our windows.
                if option[0] == left:
                    repeats: int = option[1] + 1
                    windows[tup_window][index] = [right + 1, repeats]
                    concat = True
                    if repeats >= k:
                        return True
                    break
            # Otherwise, we add this as a new option to concat with.
            if not concat:
                windows[tup_window].append([right + 1, 1])
        else:
            windows[tuple(window)] = [[right + 1, 1]]
        left += 1
        right += 1
        window.popleft()
        if right < len(arr):
            window.append(arr[right])
    return False


# Time complexity: O(n * (m + l)) <- n - length of the input array `arr`, l - number of options.
# Always traversing whole input array `arr` with our `window` => O(n).
# Extra on every index we convert `window` to tuple, and it's always of size `m` => O(n * (m + l)).
# -------------------
# Auxiliary space: O(n * m + n * l + m).
# In the worst case, every value is window sized.
# `windows` <- we will store every value as keys, and every option stored with set size => O(n * m + n * l).
# `window` and `tup_window` <- always of the size `m` => O(n * m + n * l + 2 * m)


test: list[int] = [1, 2, 4, 4, 4, 4]
test_m: int = 1
test_k: int = 3
test_out: bool = True
assert test_out == contains_pattern(test, test_m, test_k)

test = [1, 2, 1, 2, 1, 1, 1, 3]
test_m = 2
test_k = 2
test_out = True
assert test_out == contains_pattern(test, test_m, test_k)

test = [1, 2, 1, 2, 1, 3]
test_m = 2
test_k = 3
test_out = False
assert test_out == contains_pattern(test, test_m, test_k)

test = [1, 2, 3, 1, 2]
test_m = 2
test_k = 2
test_out = False
assert test_out == contains_pattern(test, test_m, test_k)

test = [3, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3, 2, 2]
test_m = 3
test_k = 2
test_out = True
assert test_out == contains_pattern(test, test_m, test_k)

test = [2, 1, 2, 2, 2, 2, 2, 2]
test_m = 2
test_k = 2
test_out = True
assert test_out == contains_pattern(test, test_m, test_k)

test = [3, 2, 1, 3, 3, 2, 1, 3, 3, 1, 2, 3, 3, 2, 1, 3, 2, 1, 1]
test_m = 1
test_k = 2
test_out = True
assert test_out == contains_pattern(test, test_m, test_k)

test = [randint(1, 100) for _ in range(100)]
print(test)
