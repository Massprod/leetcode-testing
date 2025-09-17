# You are given an integer array order of length n and an integer array friends.
# order contains every integer from 1 to n exactly once, representing the IDs
#  of the participants of a race in their finishing order.
# friends contains the IDs of your friends in the race sorted
#  in strictly increasing order.
# Each ID in friends is guaranteed to appear in the order array.
# Return an array containing your friends' IDs in their finishing order.
# --- --- --- ---
# 1 <= n == order.length <= 100
# order contains every integer from 1 to n exactly once
# 1 <= friends.length <= min(8, n)
# 1 <= friends[i] <= n
# friends is strictly increasing


def recover_order(order: list[int], friends: list[int]) -> list[int]:
    # working_solution: (100%, 42.89%) -> (0ms, 17.84mb)  Time: O(n + m) Space: O(m)
    out: list[int] = []
    fast_friends: set[int] = set(friends)
    for finisher in order:
        if finisher not in fast_friends:
            continue
        out.append(finisher)
    
    return out


# Time complexity: O(n + m) <- n - length of the input array `order`,
#                              m - length of the input array `friends`.
# We're always traversing both input arrays, once => O(n + m).
# --- --- --- ---
# Space complexity: O(m)
# `fast_friends` <- allocates space for each record in `friends` => O(m).
# `out` <- allocates space for each record in `friends` => O(2 * m).


test: list[int] = [3, 1, 2, 5, 4]
test_friends: list[int] = [1, 3, 4]
test_out: list[int] = [3, 1, 4]
assert test_out == recover_order(test, test_friends)

test = [1, 4, 5, 3, 2]
test_friends = [2, 5]
test_out = [5, 2]
assert test_out == recover_order(test, test_friends)
