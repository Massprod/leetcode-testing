# You are given an integer array deck. There is a deck of cards where every card has a unique integer.
# The integer on the ith card is deck[i].
# You can order the deck in any order you want.
# Initially, all the cards start face down (unrevealed) in one deck.
# You will do the following steps repeatedly until all cards are revealed:
#  - Take the top card of the deck, reveal it, and take it out of the deck.
#  - If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
#  - If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.
# Note that the first entry in the answer is considered to be the top of the deck.
# ---------------------------
# 1 <= deck.length <= 1000
# 1 <= deck[i] <= 10 ** 6
# All the values of deck are unique.
from random import randint
from collections import deque


def deck_reveal(deck: list[int]) -> list[int] | deque[int]:
    # working_sol (95.04%, 80.95%) -> (37ms, 16.78mb)  time: O(n * log n) | space: O(n)
    # In reverse, we can see it like this:
    # [HIGHEST]
    # [NEW_HIGHEST, HIGHEST] <- we take NEW, and we can have HIGHEST as we want.
    # [NEW_HIGHEST, HIGHEST, PRE_HIGHEST]
    # If we want to take HIGHEST, we need to take NEW_HIGHEST and skip HIGHEST,
    #  then we can have PRE_HIGHEST and finally HIGHEST.
    # Repeat for every value we add.
    deck.sort()
    new_deck: deque[int] = deque([])
    while deck:
        if new_deck:
            new_deck.appendleft(new_deck.pop())
        cur_highest: int = deck.pop()
        new_deck.appendleft(cur_highest)
    return new_deck


# Time complexity: O(n * log n) <- n - length of an input array `deck`.
# Standard `sort` takes O(n * log n) and we only traverse `deck` once.
# ---------------------------
# Auxiliary space: O(n)
# Standard `sort` taken O(n) extra space, and we create extra `deque` with size == `n` => O(2n).


test: list[int] = [17, 13, 11, 2, 3, 5, 7]
test_out: list[int] = [2, 13, 3, 11, 5, 17, 7]
assert test_out == list(deck_reveal(test))

test = [1, 1000]
test_out = [1, 1000]
assert test_out == list(deck_reveal(test))

test = [randint(1, 10 ** 6) for _ in range(1000)]
print(test)
