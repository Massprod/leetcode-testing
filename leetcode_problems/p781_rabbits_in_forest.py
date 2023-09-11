# There is a forest with an unknown number of rabbits.
# We asked n rabbits "How many rabbits have the same color as you?" and collected the answers
#  in an integer array answers where answers[i] is the answer of the ith rabbit.
# Given the array answers, return the minimum number of rabbits that could be in the forest.
# -------------------
# 1 <= answers.length <= 1000
# 0 <= answers[i] < 1000
from random import randint


def num_rabbits(answers: list[int]) -> int:
    # working_sol (76.65%, 97.80%) -> (46ms, 16.2mb)  time: O(n) | space: O(n)
    # (answer + 1) => rabbits with same color.
    # And only (answer + 1) rabbits can say this colour again.
    all_answers: int = 0
    # So we maintain limits for this. If someone say it's colour over limit,
    #  we need to reset limit and count these rabbits as different colour.
    limits: dict[int, int] = {}
    for answer in answers:
        # Unique rabbit.
        if answer == 0:
            all_answers += 1
        elif answer in limits:
            limits[answer] += 1
            # If more than (answer + 1) of same colour says it again.
            if limits[answer] > (answer + 1):
                all_answers += answer + 1
                limits[answer] = 1
        elif answer not in limits:
            all_answers += answer + 1
            limits[answer] = 1

    return all_answers


# Time complexity: O(n) -> traversing whole input_array once to get all rabbits by colours => O(n).
# n - len of input_array^^|
# Auxiliary space: O(n) -> worst case every rabbit says unique value, and not equal to 0 ->
#                       -> we will store every value in limits => O(n).
# -------------------
# So we can use every equal answers as ANSWER + 1, cuz it's ANSWER rabbits + 1 that says it.
# And for unique answers it's ANSWER + 1, cuz it's ANSWER rabbits which exist but wasn't asked, + 1 who answered.
# Store everything in dict, and just use VALUE == KEY + 1 with ignoring of duplicates.
# Extra unique case with 0. It's always +1 rabbit. Working with randoms, let's fail.
# Extra we need to consider same colour rabbits limitation. Cuz there can't be more than (answer + 1) with same colour.


test: list[int] = [1, 1, 2]
test_out: int = 5
assert test_out == num_rabbits(test)

test = [10, 10, 10]
test_out = 11
assert test_out == num_rabbits(test)

# test -> Failed -> We need to consider that rabbits which says 1, or w.e value it's limited for repeats.
#                   Only 1 other rabbit can say 1 again, and if more we need to reset limit. Fixed.
test = [0, 0, 1, 1, 1]
test_out = 6
assert test_out == num_rabbits(test)

test = [randint(0, 999) for _ in range(1000)]
print(test)
