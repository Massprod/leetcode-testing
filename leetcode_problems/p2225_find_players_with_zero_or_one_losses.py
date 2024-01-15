# You are given an integer array matches where matches[i] = [winneri, loseri]
#  indicates that the player winneri defeated player loseri in a match.
# Return a list answer of size 2 where:
#   - answer[0] is a list of all players that have not lost any matches.
#   - answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# Note:
#   - You should only consider the players that have played at least one match.
#   - The testcases will be generated such that no two matches will have the same outcome.
# ------------------------
# 1 <= matches.length <= 10 ** 5
# matches[i].length == 2
# 1 <= winneri, loseri <= 10 ** 5
# winneri != loseri
# All matches[i] are unique.
from random import randint
from collections import defaultdict


def find_winners(matches: list[list[int]]) -> list[list[int]]:
    # working_sol (89.88%, 43.55%) -> (1400ms, 71.86mb)  time: O(n * log n) | space: O(n)
    # {player_id: status} , if (no loses) status == 0, if (1 lose) status == -1
    players_stats: dict[int, int] = defaultdict(int)
    for winner, loser in matches:
        if winner not in players_stats:
            players_stats[winner] = 0
        players_stats[loser] -= 1
    out: list[list[int]] = [[], []]
    for player, stats in players_stats.items():
        if 0 == stats:
            out[0].append(player)
        elif -1 == stats:
            out[1].append(player)
    # ! The values in the two lists should be returned in increasing order !
    out = [sorted(res) for res in out]
    return out


# Time complexity: O(n * log n) <- n - length of input array `matches`.
# Worst case: every match have unique players.
#  One of them winner == 0 loses, and other loser == 1 lose.
# Traversing whole input array `matches` to get all players and their stats => O(n).
# Traversing dict `players_stats` with size == 2 * `n`, because it holds all players => O(2n).
# We will get array with winners `out[0]` with size == `n` and sort() it => O(n * log n).
# Same goes for array with losers `out[1]` => O(n * log n).
# ------------------------
# Auxiliary space: O(n).
# Worst case: same.
# We will have (2 * `n`) players stored in `player_stats` => O(2n).
# Same players will be stored in `out`: winners in `out[0]`, and losers in `out[1]` => O(2n).
# Extra sort() will take O(n) for every call.


test: list[list[int]] = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
test_out: list[list[int]] = [[1, 2, 10], [4, 5, 7, 8]]
assert test_out == find_winners(test)

test = [[2, 3], [1, 3], [5, 4], [6, 4]]
test_out = [[1, 2, 5, 6], []]
assert test_out == find_winners(test)

test = [list(match) for match in {(randint(1, 10 ** 5), randint(1, 10 ** 5)) for match in range(10 ** 3)}]
print(test)
