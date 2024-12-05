# You are given two strings start and target, both of length n.
# Each string consists only of the characters 'L', 'R', and '_' where:
# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is
#  a blank space directly to its left, and a piece 'R' can move to the right only if there is
#  a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces
#  of the string start any number of times.
# Otherwise, return false.
# ---------------------------
# n == start.length == target.length
# 1 <= n <= 10 ** 5
# start and target consist of the characters 'L', 'R', and '_'


def can_change(start: str, target: str) -> bool:
    # working_sol (86.29%, 55.09%) -> (105ms, 17.57mb)  time: O(n) | space: O(1)
    # n == start.length == target.length <- no reasons to check
    start_ind: int = 0
    target_ind: int = 0
    limit: int = len(start)
    while start_ind < limit or target_ind < limit:
        while start_ind < limit and '_' == start[start_ind]:
            start_ind += 1
        while target_ind < limit and '_' == target[target_ind]:
            target_ind += 1
        if start_ind >= limit or target_ind >= limit:
            return limit == start_ind and limit == target_ind
        if (start[start_ind] != target[target_ind]
                or ('L' == start[start_ind] and start_ind < target_ind)  # we can't shift `L` to the right
                or ('R' == start[start_ind] and start_ind > target_ind)):  # we can't shift `R` to the left
            return False
        start_ind += 1
        target_ind += 1
    return True


# Time complexity: O(n) <- n - length of the input strings `start` and `target`.
# In the worst case, we will use every index of both strings => O(2 * n).
# ---------------------------
# Auxiliary space: O(1)
# Only 3 constant INT's used, none of them depends on the input => O(1).


test_start: str = "_L__R__R_"
test_target: str = "L______RR"
test_out: bool = True
assert test_out == can_change(test_start, test_target)

test_start = "R_L_"
test_target = "__LR"
test_out = False
assert test_out == can_change(test_start, test_target)

test_start = "_R"
test_target = "R_"
test_out = False
assert test_out == can_change(test_start, test_target)
