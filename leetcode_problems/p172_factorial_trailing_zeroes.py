# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
# ---------------
# 0 <= n <= 10 ** 4
# ---------------
# Follow up: Could you write a solution that works in logarithmic time complexity?


def trailing_zeros(n: int) -> int:
    # working_sol (90.1%, 92.65%) -> (41ms, 16.2mb)  time: O(log_5_(n)) | space: O(1)
    # Trailing 0s of n! == n // 5 + n // (5 * 5) + n // (5 * 5 * 5) + ...
    # while n >= 5.
    prime: int = 5
    count: int = 0
    while n >= 5:
        n //= 5
        count += n
        prime *= 5
    return count


# Time complexity: O(log_5_(n)) -> while loop will be continued until we hit value of n < 5 ->
# n - input INT^^| -> every operation is doing floor division of n with 5, so in other words
#                   n // 5 // 5 // 5 // 5 which is equal to n // 5 ** k -> k is number of repeats =>
#                   => log_5_(5 ** k) = k -> should be correct ->
#                   -> like (10 ** 4 // 5 ** 5) = 3 ! 3 < 5 break ! so last value we used 5 ** 5
#                   number of times we divide n // 5 and multiply 5 * 5 is equal, in this case k == 5 =>
#                   so it's should be as well ->  log_5_(5 ** 5 == 3125) = 5 and log_5_(10 ** 4) = 5.7 <- we take floor
#                   because we only interested in LOOPS, and we can't do 0.7 of iteration => O(log_5_(n)).
# Auxiliary space: O(1) -> only 2 extra INTs used, doesn't depend on input => O(1).
# ---------------
# Nah. Not even a bit_operations just some MATH_check on factorials ->
# -> https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
# A trailing zero is always produced by prime factors 2 and 5.
# We can change any factorial like -> 11! = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 =>
# => (2 ** 8) * (3 ** 4) * (5 ** 2) * 7 -> because there's eight 2 and two 5 presented,
# then it's going to have 2 trailing zeroes because every pait of 2 and 5 gives trailing zero 2 * 5 = 10.
# And there's always more 2 than 5 in prime factors of any number.
# So number of TrailingZeroes is equal to count of 5s in PrimeFactors of n!.
# Trailing 0s of n! == n // 5 + n // (5 * 5) + n // (5 * 5 * 5) + ... while n >= 5.
# ---------------
# Ok. It's working, but with 8000ms. Then there's some BIT_operations task.
# ---------------
# Well I know how we can delete decimals, so why don't just delete them until they're 0
# and count every deletion. Break when something else encountered. Don't see how it's incorrect.
# But task is medium, so I'm sure there's something else.


test1 = 3
test1_out = 0
print(trailing_zeros(test1))
assert test1_out == trailing_zeros(test1)

test2 = 5
test2_out = 1
print(trailing_zeros(test2))
assert test2_out == trailing_zeros(test2)

test3 = 0
test3_out = 0
print(trailing_zeros(test3))
assert test3_out == trailing_zeros(test3)

test4 = 1111
test4_out = 275
print(trailing_zeros(test4))
assert test4_out == trailing_zeros(test4)

test5 = 10 ** 4
test5_out = 2499
print(trailing_zeros(test5))
assert test5_out == trailing_zeros(test5)
