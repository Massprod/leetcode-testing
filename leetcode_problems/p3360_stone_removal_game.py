# Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
#  - Alice starts by removing exactly 10 stones on her first turn.
#  - For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
# The player who cannot make a move loses the game.
# Given a positive integer n, return true if Alice wins the game and false otherwise.
# -------------------------------
# 1 <= n <= 50


def can_alice_win(n: int) -> bool:
    # working_sol: (100.00%, 13.30%) -> (0ms, 17.20mb)  time: O(n) | space: O(1)
    turn: int = 10
    # If `alice` can't make first turn == Lose
    alice: bool = False
    while turn <= n:
        n -= turn
        turn -= 1
        alice = not alice
    return alice


# Time complexity: O(n)
# Always depleting `n` to value lower than `turn` => O(n).
# -------------------------------
# Auxiliary space: O(1)


test: int = 12
test_out: bool = True
assert test_out == can_alice_win(test)

test = 1
test_out = False
assert test_out == can_alice_win(test)
