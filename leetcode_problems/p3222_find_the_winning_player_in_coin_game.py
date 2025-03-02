# You are given two positive integers x and y,
#  denoting the number of coins with values 75 and 10 respectively.
# Alice and Bob are playing a game. Each turn, starting with Alice,
#  the player must pick up coins with a total value 115.
# If the player is unable to do so, they lose the game.
# Return the name of the player who wins the game if both players play optimally.
# ------------------------
# 1 <= x, y <= 100


def winning_player(x: int, y: int) -> str:
    # working_sol (100.00%, 40.71%) -> (0ms, 17.89mb)  time: O(1) | space: O(1)
    bob: str = 'Bob'
    alice: str = 'Alice'
    # No matter the case, player should always take 
    # `y` coin 4 times => just check it.
    # Whole turns players take.
    # We either can take all `x` options and cover them with 4 takes of `10`.
    # Or we can't take all `x` => we will only make `y // 4`
    full_turns: int = min(x, y // 4)
    # We start from `Alice` => even # of turns => `Bob` will take last one.
    return alice if full_turns % 2 else bob


# Time complexity: O(1)
# Auxiliary space: O(1)


test_x: int = 2 
test_y: int = 7
test_out: str = 'Alice'
assert test_out == winning_player(test_x, test_y)

test_x = 4
test_y = 11
test_out = 'Bob'
assert test_out == winning_player(test_x, test_y)
