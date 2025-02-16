# Given an integer n, find a sequence that satisfies all of the following:
#  - The integer 1 occurs once in the sequence.
#  - Each integer between 2 and n occurs twice in the sequence.
#  - For every integer i between 2 and n, the distance between\
#    the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j],
#  is the absolute difference of their indices, |j - i|.
# Return the lexicographically largest sequence.
# It is guaranteed that under the given constraints, there is always a solution.
# A sequence a is lexicographically larger than a sequence b (of the same length)
#  if in the first position where a and b differ, sequence a has a number greater than
#  the corresponding number in b. For example, [0,1,9,0] is lexicographically larger
#  than [0,1,5,6] because the first position they differ is at the third number,
#  and 9 is greater than 5.
# ---------------------------
# 1 <= n <= 20
from collections import deque


def construct_distanced_sequence(n: int) -> list[int]:
    # working_sol (48.44%, 64.06%) -> (7ms, 17.71mb)  time: O(n!) | space: O(n)
    # All values used twice, except the `1`.
    out: list[int] = [0 for _ in range(n * 2 - 1)]
    used_vals: set[int] = set()

    def check(
        index: int, cur_sequence: list[int],
        used: set[int], limit: int
    ) -> bool:
        # Correctly built sequence
        if index == len(cur_sequence):
            return True
        # We can't place anything on busy spot.
        if 0 != cur_sequence[index]:
            return check(index + 1, cur_sequence, used, limit)
        for value in range(limit, 0, - 1):
            if value in used_vals:
                continue
            used_vals.add(value)
            # Try to place the value.
            cur_sequence[index] = value
            # If it's 1, we don't need a second index placed.
            if 1 == value:
                # If it's correct sequence, return it. Or change it back.
                if check(index + 1, cur_sequence, used, limit):
                    return True
            # Any other value, should have it's second index in correct range.
            # And index should be empty.
            elif (
                index + value < len(cur_sequence)
                and
                0 == cur_sequence[index + value]
            ):
                # Take second index to check.
                shifted_index: int = index + value
                cur_sequence[shifted_index] = value
                if check(index + 1, cur_sequence, used, limit):
                    return True
                # Restore if incorrect.
                cur_sequence[shifted_index] = 0
            
            cur_sequence[index] = 0
            used_vals.remove(value)
        
        return False

    check(0, out, used_vals, n)
    return out


# Time complexity: O(n!)
# Always check every possible combination of values from 1 -> n.
# It always takes n! => O(n!).
# ---------------------------
# Auxiliary space: O(n)
# `used_vals` <- allocates space for each value in 1 -> n => O(n).
# `out` <- allocates space for each value in (2 -> n * 2) and `1` => O(2 * n - 1 + n).


test: int = 3
test_out: list[int] = [3, 1 ,2, 3, 2]
assert test_out == construct_distanced_sequence(test)

test = 5
test_out = [5, 3, 1, 4, 3, 5, 2, 4, 2]
assert test_out == construct_distanced_sequence(test)
