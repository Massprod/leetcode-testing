# The Leetcode file system keeps a log each time
#  some user performs a change folder operation.
# The operations are described below:
#  - "../" : Move to the parent folder of the current folder.
#    (If you are already in the main folder, remain in the same folder).
#  - "./" : Remain in the same folder.
#  - "x/" : Move to the child folder named x (This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
# The file system starts in the main folder,
#  then the operations in logs are performed.
# Return the minimum number of operations needed
#  to go back to the main folder after the change folder operations.
# -------------------------
# 1 <= logs.length <= 10 ** 3
# 2 <= logs[i].length <= 10
# logs[i] contains lowercase English letters, digits, '.', and '/'.
# logs[i] follows the format described in the statement.
# Folder names consist of lowercase English letters and digits.
from random import choice


def min_operations(logs: list[str]) -> int:
    # working_sol (92.26%, 82.14%) -> (42ms, 16.62mb)  time: O(n * k) | space: O(1)
    out: int = 0
    for move in logs:
        if '../' == move:
            if out > 0:
                out -= 1
        elif './' != move:
            out += 1
    return out


# Time complexity: O(n * k) <- n - length of the input array `logs`, k - average length of words in `logs`.
# Always traversing every index of the input array `logs` and every word inside it while comparing => O(n * k).
# -------------------------
# Auxiliary space: O(1)
# Only 1 constant INT used, doesn't depend on input => O(1).


test: list[str] = ["d1/", "d2/", "../", "d21/", "./"]
test_out: int = 2
assert test_out == min_operations(test)

test = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
test_out = 3
assert test_out == min_operations(test)

test = ["d1/", "../", "../", "../"]
test_out = 0
assert test_out == min_operations(test)

test = [choice([f'd{index}/', './', '../']) for index in range(10 ** 3)]
print(test)
