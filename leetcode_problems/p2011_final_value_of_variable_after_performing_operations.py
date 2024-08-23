# There is a programming language with only four operations and one variable X:
#  - ++X and X++ increments the value of the variable X by 1.
#  - --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations,
#  return the final value of X after performing all the operations.
# ---------------------
# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".


def final_value_after_operations(operations: list[str]) -> int:
    # working_sol (55.43%, 73.48%) -> (54ms, 16.48mb)  time: O(n) | space: O(1)
    out: int = 0
    ops: dict[str, int] = {
        '--X': -1,
        'X--': -1,
        'X++': 1,
        '++X': 1
    }
    for operation in operations:
        out += ops[operation]
    return out


# Time complexity: O(n) <- n - length of the input array `operations`.
# Always traversing whole `operations`, once => O(n).
# ---------------------
# Auxiliary space: O(1).


test: list[str] = ["--X", "X++", "X++"]
test_out: int = 1
assert test_out == final_value_after_operations(test)

test = ["++X", "++X", "X++"]
test_out = 3
assert test_out == final_value_after_operations(test)

test = ["X++", "++X", "--X", "X--"]
test_out = 0
assert test_out == final_value_after_operations(test)
