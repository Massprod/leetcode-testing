# You are keeping the scores for a baseball game with strange rules.
# At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i]
#  is the ith operation you must apply to the record and is one of the following:
#   An integer x.
#       Record a new score of x.
#   '+'.
#     Record a new score that is the sum of the previous two scores.
#   'D'.
#     Record a new score that is the double of the previous score.
#   'C'.
#     Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations
#  fit in a 32-bit integer and that all operations are valid.
# ------------------------
# 1 <= operations.length <= 1000
# operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10 ** 4, 3 * 10 ** 4].
# For operation "+", there will always be at least two previous scores on the record.
# For operations "C" and "D", there will always be at least one previous score on the record.


def cal_point(operations: list[int]) -> int:
    # working_sol (95.08%, 82.48%) -> (35ms, 16.66mb)  time: O(n) | space: O(n)
    stack: list[int] = []
    for op in operations:
        if '+' == op:
            stack.append(stack[-1] + stack[-2])
        elif 'D' == op:
            stack.append(stack[-1] * 2)
        elif 'C' == op:
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)


# Time complexity: O(n) <- n - length of the input array `operations`.
# Always traversing `operations`, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# Worst case: every operation is just a INTEGER, stack will be of size `n` => O(n).
