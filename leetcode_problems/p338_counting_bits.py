# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
#   ans[i] is the number of 1's in the binary representation of i.
# ---------------------------
# 0 <= n <= 10 ** 5
# Follow up:
#   It is very easy to come up with a solution with a runtime of O(n log n).
#   Can you do it in linear time O(n) and possibly in a single pass?


def count_bits(n: int) -> list[int]:
    # working_sol (87.05%, 94.90%) -> (69ms, 22.99mb)  time: O(n) | space: O(n)
    # Reuse of previously calculated options.
    counted: list[int] = [0]
    for num in range(1, n + 1):
        # num >> 1 == num // 2, so we can reuse previous number,
        #  and simply add new LSB of the current number.
        counted.append(counted[num >> 1] + (num & 1))
    return counted


# Time complexity: O(n) -> for loop from 1, to n + 1 (n inclusive) with reusing of previously counted(stored) => O(n).
# n - input number^^|
# Auxiliary space: O(n) -> for every number in range(0, n + 1) we're using index to store in the list of size n => O(n).
# ---------------------------
# Well most basic way is O(n * log n), we can just shift right and count every 1 presented for everything
# in range(0, n + 1). Do this not iteratively, but with recursion?
# Then we could save every call and reuse later.
# Most important ->  Every LSB(most_right) for EVEN number is always 0 and ODD is always 1.
# Or just reuse everything from a single list.


test: int = 2
test_out: list[int] = [0, 1, 1]
assert test_out == count_bits(test)

test = 5
test_out = [0, 1, 1, 2, 1, 2]
assert test_out == count_bits(test)
