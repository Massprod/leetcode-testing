# Given an integer array nums where every element appears three times except for one,
# which appears exactly once.
# Find the single element and return it.
# -----------------------
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# -----------------------
# 1 <= nums.length <= 3 * 104  ,  -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.


def single_number(nums: list[int]) -> int:
    # working_sol (70.60%, 42.82%) -> (66ms, 18mb)  time: O(n) | space: O(1)
    one: int = 0
    two: int = 0
    for num in nums:
        two = two | (one & num)
        one = one ^ num
        to_remove: int = ~(one & two)
        print(to_remove, "to")
        print(bin(to_remove))
        one &= to_remove
        print(one, "one")
        print(bin(one))
        two &= to_remove
        print(two, "two")
        print(bin(two))
        print("---------")
    return one


# Time complexity: O(n) -> every index will be used once => O(n)
# n - len of input_list^^
# Space complexity: O(1) -> only 2 extra constants => O(1)
# -----------------------
# Flow:
#  2, 2, 4, 2 ->
#  !-> first_encounter ->
#  two = first two will be just 0, because one it's just 0b00 <- with any num (one & num) gives 0b00
#  one = (one ^ 2) -> 0b00 ^ 0b10 => one = 2 == 0b10
#  to_remove = ~(one & two) -> one == 0b10, two == 0b00 -> one & two => 0b00 -> ~(0b00) => -0b1 (11111 all 1) == 1b111
#  one = (one & to_remove) -> 0b10 & 1b11 => 00..0010 => 0b10 == 2  <- first encounter remembered.
#              00..0010^^,11..1111^^
#  two = (two & to_remove) -> 0b00 & 1b11 => 00..0000 => 0b00 == 0  <- first encounter never remembered.
#  !-> second_encounter ->
#  two = (two | (one & num)) -> one & num => 0b10 & 0b10 => 0b10 == 2 -> two | 0b10 => 0b00 | 0b10 => 0b10
#  one = (one ^ 2) -> 0b10 ^ 0b10 => 0b00 == 0 -> removed bits, cuz we're met duplicate once.
#  to_remove = ~(one & two) -> one & two => 0b00 & 0b10 => 0b00 -> ~(0) => ~(0b00) => 1b11 == -1
#  one = (one & to_remove) -> 0b00 & 1b11 => 0b00 <- second encounter annul first.
#  two = (two & to_remove) -> 0b10 & 1b11 => 0b10 <- second encounter remembered.
#  !-> new_value_encounter ->
#  two = (two | (one & num)) -> 0b000 & 0b100 => 0b000 -> (two | 0) => 0b10 | 0b00 => 0b10 == 2
#  one = (one ^ num) -> 0b000 ^ 0b100 => 0b100 == 4 <- first encounter remembered.
#  to_remove = ~(one & two) -> one & two => 0b100 & 0b010 => 0b000 == 0 -> ~(0) => ~(0b00)  => 11.111111 => 1b11 == -1
#  one = (one & to_remove) -> 0b100 & 1b111 => 0b100 == 4 <- first encounter remembered,
#                                                            and will be here until second and deleted.
#  two = (two & to_remove) -> 0b10 & 1b11 => 0b10 == 2 <- second encounter still not zeroed,
#                                                         and will be here until third and deleted.
#  !-> third_encounter ->
#  two = (two | (one & num)) -> 0b100 & 0b010 => 0b000 -> (two | 0) => 0b10 | 0b00 => 0b10 == 2
#  one = (one ^ num) -> 0b100 ^ 0b010 => 0b110 == 6 <- again first encounter with new value added.
#  to_remove = ~(one & two) -> one & two => 0b110 & 0b010 => 0b010 == 2 -> ~(2) => ~(0b010) => 1b101 == -3
#  one = (one & to_remove) -> 0b110 & 1b101 => 0b100 == 4 <- removing last added value,
#                                                            after encountering this added value again.
#  two = (two & to_remove) -> 0b010 & 1b101 => 0b000 == 0 <- second encounter zeroed, only after third time.
# !
#  As I understand,
#  one -> hold first encounter in placed bits for every value on the path.
#  two -> hold second encounter in placed bits for every value on the path.
#  to_remove -> hold bites from one and two for every encounter,
#               and we're inverting(~) them to get places for 1's to remove.
#  Every time we're deleting these bits from one and two,
#               which actually deletes second encounters for the same values added early, from one and two.
#  Leaving us with bits in ONE, which have been added only ONCE into ONE.
# -----------------------
# Googled_description:
#   ones - At any point of time, this variable holds XOR of all the elements which have
#          appeared "only" once.
#   twos - At any point of time, this variable holds XOR of all the elements which have
#          appeared "only" twice.
#
#   So if at any point time,
#       1. A new number appears - It gets XOR'd to the variable "ones".
#       2. A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the
#          variable "twice".
#       3. A number appears for the third time - It gets removed from both "ones" and "twice".
#
# The final answer we want is the value present in "ones" - coz, it holds the unique element.
# -----------------------
# Ok. Bit operations is impossible to even grasp not just come up with something myself, for now.
# So I will just take this book_solution, and at least fully understand/learn how it's done.
# Because there's no casual_logic in tasks like this and with low_experience impossible to solve.
# https://www.careercup.com/question?id=7902674 <- solution/explanation


test1 = [2, 2, 3, 2]
test1_out = 3
print(single_number(test1))
assert test1_out == single_number(test1)

test2 = [0, 1, 0, 1, 0, 1, 99]
test2_out = 99
print(single_number(test2))
assert test2_out == single_number(test2)
