# You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively.
# Each turn you choose two different non-empty piles,
#   take one stone from each, and add 1 point to your score.
# The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).
# Given three integers a, b, and c, return the maximum score you can get.
# -----------------
# 1 <= a, b, c <= 10 ** 5
from random import randint


def maximum_score(a: int, b: int, c: int) -> int:
    # working_sol (49.47%, 41.28%) -> (351ms, 16.4mb)  time: O(max - (med + min)) | O((max + med + min) // 2)
    #                                                  space: O(1)
    score: int = 0
    # Simplier to take min, max  from a list.
    values: list[int] = [a, b, c]
    # We're always exhausting current_maximum and
    # minimum value ->
    minimum: int = values.index(min(values))
    while values[minimum]:
        maximum: int = values.index(max(values))
        # Unique case when all 3 values are equal,
        # we can take w.e want. So just changing index to any other.
        if maximum == minimum:
            maximum -= 1
        values[maximum] -= 1
        values[minimum] -= 1
        score += 1
    # -> delete exhausted minimum, cuz it's 0 and can't be used ->
    del values[minimum]
    # -> set new minimum and repeat.
    minimum = values.index(min(values))
    while values[minimum]:
        maximum = values.index(max(values))
        # Same, values can be equal, and we need just 0 or 1 index.
        # -1  == 1 index. So it's either 0 - 1 == -1, or 1 - 1 == 0.
        if maximum == minimum:
            maximum -= 1
        values[maximum] -= 1
        values[minimum] -= 1
        score += 1
    return score


# Time complexity:
#   if max >= (med + min) => O(max - (med + min) -> we're always taking all from min_value and med_value,
#                            because summ of them == to max, so it's just taking all from min and then changing
#                            med_value into a min_value and exhausting it as well.
#   But I can't understand case when ! max < (med + min) -> we're always changing max_value and med_value.
#   Same for max == med == min, we're always changing min, tested some cases like a=100, b=100, c=100 ->
#   -> correct answer is 150 == (a + b + c) // 2, same for a=17944, b=25172, c=25172 -> 34144 == (a + b + c) // 2.
#   Should be correct, but how to merge them?
#   if max < (med + min) => O((max + med + min) // 2).
#   No idea how to merge this two cases correctly.
# -----------------
# Auxiliary space: O(1) -> creating extra list with size of 3 to store all input_values, always given same input,
#                          so it's constant => O(1)
# -----------------
# Working correctly for my test_cases, but I don't know tricky parts.
# Time to fail and see. Ok. All 3 values can be equal => Just change any of indexes to another index.
# -----------------
# Exhaust minimum while taking from changing maximum?
# At least working for given 3 cases, let's test.


test_a: int = 2
test_b: int = 4
test_c: int = 6
test_out: int = 6
assert test_out == maximum_score(test_a, test_b, test_c)

test_a = 4
test_b = 4
test_c = 6
test_out = 7
assert test_out == maximum_score(test_a, test_b, test_c)

test_a = 1
test_b = 8
test_c = 8
test_out = 8
assert test_out == maximum_score(test_a, test_b, test_c)

# test -> Failed -> I encounter same mistake with min_index == max_index in second while loop.
#                   But failed to see this could happen with first, when all 3 values are equal.
#                   We can just take any other index, cuz they're all same values.
test_a = 1
test_b = 1
test_c = 1
test_out = 1
assert test_out == maximum_score(test_a, test_b, test_c)

test_a = randint(1, 10 ** 5)
test_b = randint(1, 10 ** 5)
test_c = randint(1, 10 ** 5)
# print(f'{test_a}\n{test_b}\n{test_c}\n')
