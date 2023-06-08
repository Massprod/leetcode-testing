# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string,
# and then at each step perform either of the following:
#   Append the character '0' zero times.
#   Append the character '1' one times.
#   This can be performed any number of times.
# A good string is a string constructed by the above process having a length between low and high (inclusive).
#
# Return the number of different good strings that can be constructed satisfying these properties.
# Since the answer can be large, return it modulo 10 ** 9 + 7.
# ------------------------
# 1 <= low <= high <= 10 ** 5  ,  1 <= zero, one <= low


def count_good_strings(low: int, high: int, zero: int, one: int) -> int:
    # working_sol (8.65%, 5.7%) -> (1014ms, 678.8mb)  time: O(n) | space: O(n)
    dynamic: list[int] = [1] + [0 for _ in range(high)]
    for length in range(1, high + 1):
        append_one: int = length - one
        if append_one >= 0 and length <= high:
            dynamic[length] += dynamic[append_one]
        append_zero: int = length - zero
        if append_zero >= 0 and length <= high:
            dynamic[length] += dynamic[append_zero]
    all_good: int = sum(dynamic[low: high + 1])
    return all_good % (10 ** 9 + 7)


# Time complexity: O(n) -> creating list of high + 1 size => O(n + 1) -> for indexes from 1 to n(inclusive),
# n - value of high_arg^^| deciding either we can add 0 zero_times or 1 one_times to get correct length => O(n) ->
#                          -> summarizing all possible good_strings in low to high range, in the worst case:
#                          low can be equal to 1, and then we're extra looping to summ whole n => O(n) ->
#                          -> O(n + n + n) => O(3n) => O(n).
# Auxiliary space: O(n) -> 3 constant INTs and extra list with size of n + 1 => O(3 + (n + 1)) ->
#                          -> only size of a list depends on input => O(n)
# ------------------------
# Same as p70, but with appending characters instead of steps.


test1_low = 3
test1_high = 3
test1_zero = 1
test1_one = 1
test1_out = 8
print(count_good_strings(test1_low, test1_high, test1_zero, test1_one))
assert test1_out == count_good_strings(test1_low, test1_high, test1_zero, test1_one)

test2_low = 2
test2_high = 3
test2_zero = 1
test2_one = 2
test2_out = 5
print(count_good_strings(test2_low, test2_high, test2_zero, test2_one))
assert test2_out == count_good_strings(test2_low, test2_high, test2_zero, test2_one)
