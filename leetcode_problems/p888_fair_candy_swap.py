# Alice and Bob have a different total number of candies.
# You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i]
#  is the number of candies of the ith box of candy that Alice has and bobSizes[j]
#  is the number of candies of the jth box of candy that Bob has.
# Since they are friends, they would like to exchange one candy box each so that after the exchange,
#  they both have the same total amount of candy.
# The total amount of candy a person has is the sum of the number of candies in each box they have.
# Return an integer array answer where answer[0] is the number of candies
#  in the box that Alice must exchange, and answer[1] is the number of candies
#  in the box that Bob must exchange.
# If there are multiple answers, you may return any one of them.
# It is guaranteed that at least one answer exists.
# ----------------------
# 1 <= aliceSizes.length, bobSizes.length <= 10 ** 4
# 1 <= aliceSizes[i], bobSizes[j] <= 10 ** 5
# Alice and Bob have a different total number of candies.
# There will be at least one valid answer for the given input.
from collections import Counter


def fair_candy_swap(alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
    # working_sol (53.22%, 63.50%) -> (283ms, 19.09mb)  time: O(n + k) | space: O(n + k)
    out: list[int] = [0, 0]
    alice: int = sum(alice_sizes)
    bob: int = sum(bob_sizes)
    # { box_size: number of boxes }
    alice_boxes: dict[int, int] = Counter(alice_sizes)
    bob_boxes: dict[int, int] = Counter(bob_sizes)
    # SumA - x + y = SumB - y + x <- SumA == alice candies, SumB == bobs candies.
    #                                x - value we take, y - value we need to get in return
    # y + y = x + x + SumB - SumA
    # 2y = 2x + SumB - SumA
    # y = x + (SumB - SumA) / 2
    for box in alice_boxes:
        target: int = box + (bob - alice) // 2
        if target in bob_boxes:
            out[0], out[1] = box, target
            return out


# Time complexity: O(n + k) <- n - length of the input array `alice_sizes`, k - length of the input array `bob_sizes`.
# We're always traversing both input arrays, twice to get sum + all the boxes and their occurrences => O(2 * (n + k)).
# In the worst case, every value in `alice_sizes` is going to be unique.
# So, we're extra traversing `n` keys to get our `target` (answer is guaranteed) => O(2 * (n + k) + n).
# ----------------------
# Auxiliary space: O(n + k)
# In the worst case, every value in both input arrays is unique.
# Both dictionaries will be of the array sizes => O(n + k).


test_alice: list[int] = [1, 1]
test_bob: list[int] = [2, 2]
test_out: list[int] = [1, 2]
assert test_out == fair_candy_swap(test_alice, test_bob)

test_alice = [1, 2]
test_bob = [2, 3]
test_out = [1, 2]
assert test_out == fair_candy_swap(test_alice, test_bob)

test_alice = [2]
test_bob = [1, 3]
test_out = [2, 3]
assert test_out == fair_candy_swap(test_alice, test_bob)
