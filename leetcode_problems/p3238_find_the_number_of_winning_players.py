# You are given an integer n representing the number of players in a game and a 2D array pick
#  where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.
# Player i wins the game if they pick strictly more than i balls of the same color.
# In other words,
#  - Player 0 wins if they pick any ball.
#  - Player 1 wins if they pick at least two balls of the same color.
#    ...
#  - Player i wins if they pick at leasti + 1 balls of the same color.
# Return the number of players who win the game.
# Note that multiple players can win the game.
# --------------------------
# 2 <= n <= 10
# 1 <= pick.length <= 100
# pick[i].length == 2
# 0 <= xi <= n - 1
# 0 <= yi <= 10


def winning_player_count(n: int, pick: list[list[int]]) -> int:
    # working_sol (85.68%, 56.28%) -> (154ms, 16.59mb)  time: O(m) | space: O(m)
    # { player: { ball_color: ball_taken } }
    players: dict[int, dict[int, int]] = {}
    for player, colour in pick:
        if player not in players:
            players[player] = {}
        if colour in players[player]:
            players[player][colour] += 1
        else:
            players[player][colour] = 1
    out: int = 0
    for player in players.keys():
        for colour, occurs in players[player].items():
            if occurs > player:
                out += 1
                break
    return out


# Time complexity: O(m) <- n - length of the input array `pick`.
# In the worst case, there's unique players and colors in every pair in `pick`.
# So, we're going to traverse `pick`, twice => O(m * 2).
# --------------------------
# Auxiliary space: O(m)
# `players` <- will allocate space for each unique pair => O(m).


test_n: int = 4
test: list[list[int]] = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
test_out: int = 2
assert test_out == winning_player_count(test_n, test)

test_n = 5
test = [[1, 1], [1, 2], [1, 3], [1, 4]]
test_out = 0
assert test_out == winning_player_count(test_n, test)

test_n = 5
test = [[1, 1], [2, 4], [2, 4], [2, 4]]
test_out = 1
assert test_out == winning_player_count(test_n, test)
