# Given two strings s and goal, return true if you can swap two letters in s
#   so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed)
#   such that i != j and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
# ---------------
# 1 <= s.length, goal.length <= 2 * 10 ** 4
# s and goal consist of lowercase letters.
from string import ascii_lowercase
from random import choice, randint


def buddy_strings(s: str, goal: str) -> bool:
    # working_sol (94.25%, 89.62%) -> (40ms, 16.4mb)  time: O(n) | space: O(n)
    # Not equal length -> not buddies :(
    if len(s) != len(goal):
        return False
    # Assuming we have equal strings,
    # cuz if they're equal we need to count S symbols occurrences.
    equal: bool = True
    # Storing this occurrences in dict.
    s_symbols: dict[str, int] = {}
    # We only need 2 indexes if there's more we can't switch only 2 as we said,
    # if there's less than 2 we can't switch 2 either.
    switch_indexes: list[int] = []
    # Breaker to escape from symbol recording.
    # Cuz we don't need more symbols if we're already having 1 symbol with
    # 2 occurrences and strings are equal.
    double: bool = False
    for x in range(len(s)):
        # We can't have more than 2 ^^|
        if len(switch_indexes) >= 3:
            return False
        # If there's different symbol on same index,
        # strings are not equal. And we need to count this diff indexes.
        if s[x] != goal[x]:
            equal = False
            switch_indexes.append(x)
        if equal:
            if not double:
                if s[x] not in s_symbols:
                    s_symbols[s[x]] = 1
                    continue
                # We can ignore any other symbols after.
                s_symbols[s[x]] += 1
                double = True
    # If strings are equal, and we have duplicate, we can switch it.
    if double and equal:
        return True
    # If strings are equal, but we don't have duplicate.
    # We can't switch anything and keep them equal.
    if not double and equal:
        return False
    # If there's only 1 index_difference, we can't do 2 switches as required.
    if len(switch_indexes) != 2:
        return False
    # We need to switch s[0] to s[1] such s[1] == goal[0] and s[0] == goal[1].
    if s[switch_indexes[0]] == goal[switch_indexes[1]] and s[switch_indexes[1]] == goal[switch_indexes[0]]:
        return True
    # I was lucky there's no such test cases, but we can get 2 switch_indexes,
    # and they will have different symbols than goal[0] and goal[1].
    # So we need extra return False, after.
    return False


# Time complexity: O(n) -> traversing both input_arrays at the same time, only if they're length are equal => O(n) ->
# n - len of any input_array^^| -> extra check for 2 indexes, so it's constant and ignored.
#                       If there's more than 2 diff indexes we're breaking on some part Ω(log n).
# Auxiliary space: O(n) -> in the worst case there's only unique values without duplicates and strings are equal ->
#                       -> so we're going to store every symbol of S in dictionary with constant 1 as value => O(n).
#                       If they're not equal, we're only storing some part Ω(log n), same for traverse
# ---------------
# First rule -> we can swap ONLY 2 indexes to make them equal.
# Second rule -> we can use same symbols, but no the same indexes.
# Third rule -> they should be of equal size, cuz we can't make them equal with diff sizes.
# Ok. So if there's 3 different symbols we can't make them equal, also if diff sizes.
# And we can reuse symbols if strings already equal, if they're on different indexes.
# Traverse both of them together record what symbols and how many of them we have,
# and if strings equal, find count >= 2 for some symbol to shuffle. Should be correct.


test1_s = "ab"
test1_goal = "ba"
test1_out = True
assert test1_out == buddy_strings(test1_s, test1_goal)

test2_s = "ab"
test2_goal = "ab"
test2_out = False
assert test2_out == buddy_strings(test2_s, test2_goal)

test3_s = "aa"
test3_goal = "aa"
test3_out = True
assert test3_out == buddy_strings(test3_s, test3_goal)

test_s: list[str] = []
test_goal: list[str] = []
for _ in range(2 * 10 ** 4):
    hold: str = choice(ascii_lowercase)
    test_s.append(hold)
    test_goal.append(hold)
switch_1: int = randint(0, 2 * 10 ** 4 - 1)
switch_2: int = randint(0, 2 * 10 ** 4 - 1)
test_s[switch_1], test_s[switch_2] = test_s[switch_2], test_s[switch_1]
# print("".join(test_s))
# print("----------------")
# print("".join(test_goal))
