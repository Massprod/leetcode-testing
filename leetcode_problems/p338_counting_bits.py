# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
#   ans[i] is the number of 1's in the binary representation of i.
# ---------------------------
# 0 <= n <= 10 ** 5
# Follow up:
#   It is very easy to come up with a solution with a runtime of O(n log n).
#   Can you do it in linear time O(n) and possibly in a single pass?


def count_bits(n: int) -> list[int]:
    # working_sol (78.16%, 66.78%) -> (79ms, 23.1mb)  time: O(n) | space: O(n)
    # No reasons to store in dictionary,
    # cuz every number is in range(0, n + 1).
    counted: dict[int: int] = [0 for _ in range(n + 1)]

    def shifts_count(num: int) -> int:
        if counted[num]:
            return counted[num]
        # Last bit is either 0 or 1.
        if num == 0:
            return 0
        if num == 1:
            return 1
        # Every LSB(most_right) for EVEN number is always 0.
        if num % 2 == 0:
            counted[num] = shifts_count(num >> 1)
        # For ODD number is always 1.
        # So if we delete it, we need to extra +1 for replacement.
        elif num % 2 == 1:
            counted[num] = 1 + shifts_count(num >> 1)
        return counted[num]

    for _ in range(n + 1):
        counted[_] = shifts_count(_)
    return counted


# Time complexity: O(n) -> with storing and reuse of previous results, we will calc every num only once => O(n).
# n - input number^^|
# Auxiliary space: O(n) -> for every number in range(0, n + 1) we're using index to store in the list of size n => O(n).
# ---------------------------
# Well most basic way is O(n * log n), we can just shift right and count every 1 presented for everything
# in range(0, n + 1). Do this not iteratively, but with recursion?
# Then we could save every call and reuse later.
# Most important ->  Every LSB(most_right) for EVEN number is always 0 and ODD is always 1.
# Ok. Instead of using dictionary we can store everything in list with indexes in this range.


test: int = 2
test_out: list[int] = [0, 1, 1]
assert test_out == count_bits(test)

test = 5
test_out = [0, 1, 1, 2, 1, 2]
assert test_out == count_bits(test)
