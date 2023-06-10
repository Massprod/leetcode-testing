# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
#   - Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   - Repeat the process until the number equals 1 (where it will stay),
#        or it loops endlessly in a cycle which does not include 1.
#   - Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# -----------------------
# 1 <= n <= 2 ** 31 - 1


def is_happy(n: int) -> bool:
    to_power: list[int] = []
    while True:
        while True:
            part: int = n % 10
            n = n // 10
            to_power.append(part)
            if n < 10:
                to_power.append(n)
                break
            if n == 10:
                to_power.append(1)
                break
        n = 0
        while to_power:
            n += to_power.pop() ** 2
        if 1 < n < 10 and n != 7:
            return False
        if n == 1 or n == 7:
            return True


# It was expected to other than 1 and 10 fail with loop, but this extra 7 is not obvious at all.
# Unique case which can't be seen without failing or extra math_info on that, I made it with brute_forcing,
# without research, so I guess there's some other methods explaining it.
# -----------------------
# Hmm. all except 7 is correct for my solution, but only 7 is unique in case of less than 10.
# I was thinking every value except 1 will be endless loop but here's extra 7, maybe something more but other's is
# ending in a loop. Guess I will just check for 1 and 7, and find extra info on that after.
# -----------------------
# Guess there's TLE for standard manipulations with power(), so either I insta look
# for extra info or fail TimeLimit first. Prefer to fail first, maybe im wrong. But don't see any bit_methods I know.


test1 = 19
test1_out = True
print(is_happy(test1))

test2 = 2
test2_out = False
print(is_happy(test2))

test3 = 2 ** 31 - 1
test3_out = False
print(is_happy(test3))

test4 = 1111111
test4_out = True
print(is_happy(test4))
