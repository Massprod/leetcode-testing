# You are given an integer array target and an integer n.
# You have an empty stack with the two following operations:
#  "Push": pushes an integer to the top of the stack.
#  "Pop": removes the integer on the top of the stack.
# You also have a stream of the integers in the range [1, n].
# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target.
# You should follow the following rules:
#  If the stream of the integers is not empty, pick the next integer from the stream
#   and push it to the top of the stack.
#  If the stack is not empty, pop the integer at the top of the stack.
#  If, at any moment, the elements in the stack (from the bottom to the top) are equal to target,
#   do not read new integers from the stream and do not do more operations on the stack.
# Return the stack operations needed to build target following the mentioned rules.
# If there are multiple valid answers, return any of them.
# ----------------------
# 1 <= target.length <= 100
# 1 <= n <= 100
# 1 <= target[i] <= n
# target is strictly increasing.


def build_array(target: list[int], n: int) -> list[str]:
    # working_sol (91.15%, 76.26%) -> (33ms, 16.1mb)  time: O(n) | space: O(n)
    # ! target is strictly increasing. !
    # So, all we care is that push & pop wrong and push correct.
    index: int = 0
    # ! 1 <= target[i] <= n !
    # We don't even need 'n' to be used.
    stream: int = 1
    out: list[str] = []
    while index != len(target):
        if target[index] == stream:
            out.append('Push')
            stream += 1
            index += 1
        else:
            out += ['Push', 'Pop']
            stream += 1
    return out


# Time complexity: O(n) -> essentially traverse from 1 -> 'n' inclusive => O(n).
# n - input value 'n'^^|
# Auxiliary space: O(n) -> worst case == 'target' = [100], n = 100 -> we will use ['Push', 'Pop'] operations for every
#                          value in 'target', except last one => O(n * 2 - 1).


test: list[int] = [1, 3]
test_n: int = 3
test_out: list[str] = ["Push", "Push", "Pop", "Push"]
assert test_out == build_array(test, test_n)

test = [1, 2, 3]
test_n = 3
test_out = ["Push", "Push", "Push"]
assert test_out == build_array(test, test_n)

test = [1, 2]
test_n = 4
test_out = ["Push", "Push"]
assert test_out == build_array(test, test_n)

test = [100]
test_n = 100
assert 100 * 2 - 1 == len(build_array(test, test_n))
