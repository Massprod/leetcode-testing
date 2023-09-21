# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'.
# You are given a string colors of length n where colors[i] is the color of the ith piece.
# Alice and Bob are playing a game where they take alternating turns removing pieces from the line.
# In this game, Alice moves first.
#   - Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'.
#     She is not allowed to remove pieces that are colored 'B'.
#   - Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'.
#     He is not allowed to remove pieces that are colored 'A'.
#   - Alice and Bob cannot remove pieces from the edge of the line.
#   - If a player cannot make a move on their turn, that player loses and the other player wins.
# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
# -----------------------
# 1 <= colors.length <= 10 ** 5
# colors consists of only the letters 'A' and 'B'
from random import choice


def winner_of_game(colors: str) -> bool:
    # working_sol (91.9%, 72.89%) -> (151ms, 17.3mb)  time: O(n) | space: O(n)
    alice_turns: int = 0
    bob_turns: int = 0
    cur_sub: str = ''
    for color in colors:
        # Expand subarray.
        if not cur_sub or color == cur_sub[-1]:
            cur_sub += color
        # Count turns.
        elif len(cur_sub) >= 3:
            if cur_sub[-1] == 'A':
                alice_turns += len(cur_sub) - 2
            elif cur_sub[-1] == 'B':
                bob_turns += len(cur_sub) - 2
            cur_sub = color
        # Reset.
        else:
            cur_sub = color
    # Extra check for last subarray.
    if len(cur_sub) >= 3:
        if cur_sub[-1] == 'A':
            alice_turns += len(cur_sub) - 2
        elif cur_sub[-1] == 'B':
            bob_turns += len(cur_sub) - 2
    # Alice can't start.
    if not alice_turns:
        return False
    # Alice have more turns.
    elif alice_turns > bob_turns:
        return True
    # Alice have same turns, but bob will make last == win.
    elif alice_turns <= bob_turns:
        return False


# Time complexity: O(n) -> traversing whole input_string once => O(n).
# n - len of input_string^^|
# Auxiliary space: O(n) -> worst case == every symbol is 'A' or 'B', we will get subarray with size of n => O(n).
# -----------------------
# We don't care about x2 subs, and we always make turns 1 by 1 without skips.
# So, all we care is that is there's still SUB with x3 same elements in it.
# And we can't take more than (lenSUB - 2) elements from any SUB.
# Just count every SUB with x3 of same, and calc their maximum ways to take.
# If 'A' more than Alice, if 'B' more than Bob.
# Extra, Bob wins if Alice doesn't have any SUB at all.


test: str = "AAABABB"
test_out: bool = True
assert test_out == winner_of_game(test)

test = "AA"
test_out = False
assert test_out == winner_of_game(test)

test = "ABBBBBBBAAA"
test_out = False
assert test_out == winner_of_game(test)

test = ''
for _ in range(10 ** 5):
    test += choice(['A', 'B'])
print(test)
