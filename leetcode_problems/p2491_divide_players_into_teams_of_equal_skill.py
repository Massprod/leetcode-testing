# You are given a positive integer array skill of even
#  length n where skill[i] denotes the skill of the ith player.
# Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
# The chemistry of a team is equal to the product of the skills of the players on that team.
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players
#  into teams such that the total skill of each team is equal.
# ---------------------------
# 2 <= skill.length <= 10 ** 5
# skill.length is even.
# 1 <= skill[i] <= 1000
from random import randint


def divide_players(skill: list[int]) -> int:
    # working_sol (79.29%, 68.50%) -> (392ms, 29.45mb)  time: O(n * log n) | space: O(n)
    # We should make pairs like: (max_skill, lowest_skill)
    # Because if we use `max_skill` with someone else,
    #  we will never be able to find a pair for `lowest_skill` to match this pair.
    # Same for using `lowest_skill` with som1 else.
    # So, the best approach is to always take them in (max_skill, lowest_skill).
    out: int = 0
    skill.sort()
    lowest: int = 0
    highest: int = len(skill) - 1
    target_skill: int = skill[lowest] + skill[highest]
    while lowest < highest:
        team_skill: int = skill[lowest] + skill[highest]
        if target_skill != team_skill:
            return -1
        out += skill[lowest] * skill[highest]
        lowest += 1
        highest -= 1
    return out


# Time complexity: O(n * log n) <- n - length of the input array `skill`.
# Always sorting and traversing the input array `skill`, once => O((n * log n) + n)
# ---------------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) by itself => O(n).


test: list[int] = [3, 2, 5, 1, 3, 4]
test_out: int = 22
assert test_out == divide_players(test)

test = [3, 4]
test_out = 12
assert test_out == divide_players(test)

test = [1, 1, 2, 3]
test_out = -1
assert test_out == divide_players(test)

test = [randint(1, 1000) for _ in range(10 ** 4)]
print(test)
