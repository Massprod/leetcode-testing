# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
#   -1: Your guess is higher than the number I picked (i.e. num > pick).
#    1: Your guess is lower than the number I picked (i.e. num < pick).
#    0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
# -----------------
# 1 <= n <= 2 ** 31 - 1
# 1 <= pick <= n
from random import randint


class Number:

    def __init__(self, value: int):
        if value:
            self.number = value
        else:
            self.number: int = randint(1, 2 ** 31 - 1)

    def guess(self, check: int):
        if self.number == check:
            return 0
        elif self.number > check:
            return 1
        elif self.number < check:
            return -1

    def which(self):
        return self.number


def guess_number(n: int) -> int:
    # working_sol (87.34%, 99.71%) -> (35ms, 16.1mb)  time: O(log n) | space: O(1)
    left_l: int = 1
    right_l: int = n
    while left_l < right_l:
        middle: int = (left_l + right_l) // 2 + 1
        take_a_guess: int = test_number.guess(middle)
        # Correct.
        if take_a_guess == 0:
            return middle
        # Higher -> try Lower.
        elif take_a_guess == -1:
            right_l = middle - 1
        # Lower -> try Higher.
        elif take_a_guess == 1:
            left_l = middle
    return left_l


# Time complexity: O(log n) -> we're always given High limit of 'n', so it's standard BS with O(log n).
# Auxiliary space: O(1) -> only 3 constant INTs used, none of them depends on input => O(1).
# -----------------
# Ok. Did some overhead stuff for this task, but good_simple_practice anyway.


test_n: int = 10
test_pick: int = 6
test_number: Number = Number(test_pick)
test_out: int = 6
assert test_out == guess_number(test_n)
del test_number

test_n = 1
test_pick = 1
test_number = Number(test_pick)
test_out = 1
assert test_out == guess_number(test_n)
del test_number

test_n = 2
test_pick = 1
test_number = Number(test_pick)
test_out = 1
assert test_out == guess_number(test_n)
del test_number

test: int = 100
while test:
    test -= 1
    test_n = 2 ** 31 - 1
    test_number = Number(test_pick)
    test_out = test_number.which()
    assert test_out == guess_number(test_n)
    del test_number
