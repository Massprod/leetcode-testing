# There are n bulbs that are initially off. You first turn on all the bulbs,
# then you turn off every second bulb.
#
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
# For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
#
# Return the number of bulbs that are on after n rounds.
# -----------------------
# 0 <= n <= 109
import math


def bulb_switch(n: int) -> int:
    # working_sol (72.97%, 46.95%) -> (43ms, 16.3mb)  time: O(1) or O(n) | space: O(1)
    # if n == 0:                                                  #  ^^for a loop
    #     return 0
    # bulb_count: int = 0
    # for x in range(1, n + 1):
    #     if int(math.sqrt(x)) * int(math.sqrt(x)) == x:
    #         bulb_count += 1
    # return bulb_count
    return int(math.sqrt(n))


# Time complexity: O(1) <- for insta return
# Time complexity: O(n) <- for solution with a loop if we search for a perfect squares one by one.
# Space complexity: O(1)
# -----------------------
# !
# As all the bulbs are initially off, at the end only bulbs that are toggled
#   an odd number of times will remain on.
# Now, whenever we are at a round i we know we toggle all bulbs having a factor i.
# Thus, we need to find the bulbs which have an odd number of factors,
#   as those bulbs will be toggled an odd number of times (once by each factor).
# Now let's discuss, why do perfect squares have odd and non-perfect squares have an even number of factors?
# When we factorize a number y, say we have one factor x, then the other factor whose multiplication
#   will result in the original number will be y / x.
# Now comparing x and y / x, if y is a perfect square it means y = a * a
#   thus, here it is a possibility that x and y / x are same numbers, i.e. a.
# But if y is not a perfect square then for each x we will have a unique y / x,
#   thus, it's factor pairs will always exist as two different numbers
#   (e.g: for 12 -> 1 x 12, 2 x 6, 3 x 4, (it has three factor pairs, so total 6 factors)),
#   thus the total count of number of factors for non-perfect squares will be even,
#   and for perfect square, all other x and y / x factor pairs will be two different numbers
#   except for one case, i.e. a and a (e.g: for 16 -> 1 x 16, 2 x 8, 4 x 4
#   (4 is paired with itself, it has three factor pairs, but one pair has both numbers same, so total 5 factors)).
#   Thus, it will have odd number of total factors.
# Thus, we just need to find how many numbers from 1 to n are perfect squares.
# We can iterate on each number and check if it's a perfect square or not,
#   (i.e. floor(sqrt(i)) * floor(sqrt(i)) == i)
# Or, we can directly find the square root of n and its floor value will be equal
#   to the count of numbers whose squares exist in this range 1 to n.
# The floor of the square root of n gives us the largest number whose square is less than or equal to n.
#   For example, if n = 26, then the floor of square root of n is 5,
#   which means the largest number whose square is less than or equal to 26 is 5
#   thus for each number from 1 to 5, its respective square will be present in the original range.
#       So, there are 5 perfect squares in the range 1 to 25 (1, 4, 9, 16, and 25).
# -----------------------
# Hard to come up with workings solution for a time_limit, but now I understand how it's needs to be done.
# For a future use -> perfect_square is any number which -> int(sqrt(num)) * int(sqrt(num)) == num,
#                     and perfect_square number always have ODD factors, which means
#                     it will be triggered ODD times. Non-perfect always have EVEN factors(triggers).


test1 = 3
test1_out = 1
print(bulb_switch(test1))
assert test1_out == bulb_switch(test1)

test2 = 0
test2_out = 0
print(bulb_switch(test2))
assert test2_out == bulb_switch(test2)

test3 = 1
test3_out = 1
print(bulb_switch(test3))
assert test3_out == bulb_switch(test3)

test4 = 9999999
test4_out = 3162
print(bulb_switch(test4))
assert test4_out == bulb_switch(test4)
