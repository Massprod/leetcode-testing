# You are given an integer n, the number of teams in a tournament that has strange rules:
#   - If the current number of teams is even, each team gets paired with another team.
#     A total of n / 2 matches are played, and n / 2 teams advance to the next round.
#   - If the current number of teams is odd, one team randomly advances in the tournament,
#     and the rest gets paired. A total of (n - 1) / 2 matches are played,
#     and (n - 1) / 2 + 1 teams advance to the next round.
# Return the number of matches played in the tournament until a winner is decided.
# -------------------------------
# 1 <= n <= 200


def number_of_matches(n: int) -> int:
    # working_sol (98.17%, 90.87%) -> (26ms, 16.10mb)  time: O(log n) | space: O(1)
    out: int = 0
    calls: int = 0
    while n > 1:
        calls += 1
        # Odd.
        if n % 2:
            n = n // 2
            # ! (n - 1) / 2 matches are played !
            out += n
            # ! (n - 1) / 2 + 1 teams advance !
            n += 1
        else:
            # ! n / 2 matches are played !
            n = n // 2
            # ! n / 2 teams advance !
            out += n
    return out


# Time complexity: O(log n).
# log2(n) steps to get to 1. Because we always split n in two.
# Auxiliary space: O(1).
# -------------------------------
# Without simulation we can just return: (n - 1).
# Because w.e the matches we will have we always eliminate only 1 team per match.
# In the end there's (n - 1) losers == matches, and only 1 winner.
# So, n == 200 => 100 matches => -100 teams
#     n == 100 => 50 matches => -50 teams
#     n == 50 => 25 matches => -25 teams
#     n == 25 => 12 matches => -12 teams
#     n == 13 => 6 matches => -6 teams
#     n == 7 => 3 matches => -3 teams
#     n == 4 => 2 matches => -2 teams
#     n == 2 => 1 matches => -1 teams
#     matches == 100 + 50 + 25 + 12 + 6 + 3 + 2 + 1 == 199


test: int = 7
test_out = 6
assert test_out == number_of_matches(test)

test = 14
test_out = 13
assert test_out == number_of_matches(test)

test = 200
test_out = 199
assert test_out == number_of_matches(test)
