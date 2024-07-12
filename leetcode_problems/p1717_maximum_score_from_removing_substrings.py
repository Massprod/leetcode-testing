# You are given a string s and two integers x and y.
# You can perform two types of operations any number of times.
#  - Remove substring "ab" and gain x points.
#    - For example, when removing "ab" from "cabxbae" it becomes "cxbae".
#  - Remove substring "ba" and gain y points.
#    - For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.
# -----------------------
# 1 <= s.length <= 10 ** 5
# 1 <= x, y <= 10 ** 4
# s consists of lowercase English letters.
from random import choice
from string import ascii_lowercase


def maximum_gain(s: str, x: int, y: int) -> int:
    # working_sol (73.38%, 38.96%) -> (232ms, 18.32mb)  time: O(s) | space: O(s)
    # 'abba' <- if we delete 'ab' => 'ba'
    # if we delete 'ba' => 'ab'
    # W.e the case they're going to be equal, but if we have:
    # 'bababa' <- we should prefer the one with higher cost.
    # x == 5 y == 1
    # if we delete only 'ba' => 3
    # if we delete 'ab' and then still have 'ba' left => 11
    # Actually w.e the options we take we're still utilizing everything,
    #  so I guess we can just take the most profitable option.
    # Traverse, with deleting the highest option,
    #  and traverse again to delete everything left?
    out: int = 0
    highest_cost: str = 'a'
    counterpart: str = 'b'
    highest: int = y
    lowest: int = x
    if x >= y:
        highest_cost: str = 'b'
        counterpart = 'a'
        highest = x
        lowest = y
    stack: list[str] = []
    allowed: set[str] = {'a', 'b'}
    for char in s:
        if char in allowed:
            if char == highest_cost and stack and stack[-1] == counterpart:
                stack.pop()
                out += highest
                continue
        stack.append(char)
    new_string: str = ''.join(stack)
    stack = []
    for char in new_string:
        if char in allowed:
            if char == counterpart and stack and stack[-1] == highest_cost:
                stack.pop()
                out += lowest
                continue
        stack.append(char)
    return out


# Time complexity: O(s)
# In the worst case, there's no correct pairs present.
# So, we will just traverse `s` once to get full string in the `stack` => O(s).
# Traverse it again in full size to try and delete other option => O(2s).
# If we have correct pairs, we're going to traverse stack to delete them, even if we're going to have
#  all the highest-cost pairs in string.
# We're still only traversing the string twice, so it's 100% Linear.
# -----------------------
# Auxiliary space: O(s)
# `stack` at max will allocate space for every char in `s` => O(s).
# And if we didn't have any correct pairs `new_string` is also going to be of size `s` => O(2s).


test: str = "cdbcbbaaabab"
test_x: int = 4
test_y: int = 5
test_out: int = 19
assert test_out == maximum_gain(test, test_x, test_y)

test = "aabbaaxybbaabb"
test_x = 5
test_y = 4
test_out = 20
assert test_out == maximum_gain(test, test_x, test_y)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test)
