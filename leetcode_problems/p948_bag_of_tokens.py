# You start with an initial power of power, an initial score of 0,
#  and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.
# Your goal is to maximize the total score by strategically playing these tokens.
# In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
#   - Face-up: If your current power is at least tokens[i], you may play tokeni,
#     losing tokens[i] power and gaining 1 score.
#   - Face-down: If your current score is at least 1, you may play tokeni,
#     gaining tokens[i] power and losing 1 score.
# Return the maximum possible score you can achieve after playing any number of tokens.
# ----------------------
# 0 <= tokens.length <= 1000
# 0 <= tokens[i], power < 10 ** 4
from random import randint


def bag_of_tokens_score(tokens: list[int], power: int) -> int:
    # working_sol (76.02%, 94.31%) -> (50ms, 16.64mb)  time: O(n * log n) | space: O(n)
    # All we care about is using `power` to get score.
    # Best way to do this => take the smallest possible at a time.
    # And if we run out of `power`, try to restore it.
    tokens.sort()
    min_pos: int = 0
    max_pos: int = len(tokens) - 1
    out: int = 0
    current: int = 0
    while min_pos <= max_pos and min_pos != len(tokens) and max_pos >= 0:
        if tokens[min_pos] <= power:
            power -= tokens[min_pos]
            min_pos += 1
            current += 1
            out = max(out, current)
        elif 0 < current:
            power += tokens[max_pos]
            max_pos -= 1
            current -= 1
        else:
            break
    return out


# Time complexity: O(n * log n) <- n - length of input array `tokens`.
# Traversing `tokens` once, after sorting.
# ----------------------
# Auxiliary space: O(n).
# Standard python `sort()` have O(n) space, everything else is constant.


test: int = 50
test_tokens: list[int] = [100]
test_out: int = 0
assert test_out == bag_of_tokens_score(test_tokens, test)

test = 150
test_tokens = [200, 100]
test_out = 1
assert test_out == bag_of_tokens_score(test_tokens, test)

test = 200
test_tokens = [100, 200, 300, 400]
test_out = 2
assert test_out == bag_of_tokens_score(test_tokens, test)

test = randint(0, 10 ** 4)
test_tokens = [randint(0, 10 ** 4) for _ in range(1000)]
print(test, 'tete')
print(test_tokens)
