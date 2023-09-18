# You are given a string of digits num, such as "123456579".
# We can split it into a Fibonacci-like sequence [123, 456, 579].
# Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:
#   0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
#   f.length >= 3, and
#   f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
# Note that when splitting the string into pieces, each piece must not have extra leading zeroes,
#  except if the piece is the number 0 itself.
# Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.
# -------------------
# 1 <= num.length <= 200
# num contains only digits.


def split_into_fibo(num: str) -> list[int]:
    # working_sol (94.91%, 87.4%) -> (38ms, 16.3mb)  time: O(n * n) | space: O(n)
    # We can't build anything from only zeroes, except [0, 0, ... 0]
    # So, it's unique case.
    if num.count('0') == len(num):
        return [0 for _ in num]
    # Cull calc.
    limit: list[int] = [2 ** 31]

    def check(start: int, sequence: list[int]) -> list[int]:
        # Nothing left to build from.
        if start >= len(num):
            # We're building from (0 -> len(nums) - 1) for every option.
            # Even first number, need extra check for correct sequence >= 3.
            # And because all digits are positive we can't have 0 at the end.
            # Only unique case with 0 at the end checked before.
            if len(sequence) >= 3 and sequence[-1] != 0:
                return sequence
            return []
        # We can use 0, but not build with leading 0.
        if num[start] == '0':
            if correct := check(start + 1, sequence + [0]):
                return correct
            return []
        end: int = start
        # First two doesn't require correct sum of previous 2.
        if len(sequence) < 2:
            while end < len(num):
                cur_num: int = int(num[start:end + 1])
                if not 0 <= cur_num < limit[0]:
                    return []
                # return -> list|none, so it's needs to be saved.
                # Either walrus or just variable.
                # We can insta return correct sequence if it's found:
                # ! Return any Fibonacci-like sequence split from num !
                if correct := check(end + 1, sequence + [cur_num]):
                    return correct
                end += 1
            return []
        # Cull calc.
        expected: int = sequence[-2] + sequence[-1]
        while end < len(num):
            cur_num = int(num[start:end + 1])
            if not 0 <= cur_num < limit[0]:
                return []
            if expected == cur_num:
                if correct := check(end + 1, sequence + [cur_num]):
                    return correct
            end += 1
            # Only positive values -> always increasing.
            # No reasons to check higher ones.
            if expected < cur_num:
                break
        return []

    return check(0, [])


# Time complexity: O(n * n) -> counting '0' => O(n) -> we're always trying to build from any index, assume we have
# n - len of input_string^^| string which gives us option to build from any index correct sequence except last one ->
#                            -> then we will start from [0] and build with every other index same way [1][2][3][4] ...
#                            [last] <- fail, start again [0, 1], again [0, 1, 2] [0, 1, 2, 3] ... etc.
#                            So, every index will be used 'n' times => O(n * n). Should be correct.
# Auxiliary space: O(n) -> worst case == every value is '0' or string is correct fibo sequence with 1 digits numbers ->
#                          -> then for every number we will add INT(value) into an output list => O(n).


test: str = "1101111"
test_out: list[int] = [11, 0, 11, 11]
assert test_out == split_into_fibo(test)

test = "112358130"
test_out = []
assert test_out == split_into_fibo(test)

test = "0123"
test_out = []
assert test_out == split_into_fibo(test)

test = "047960461863532249231225"
test_out = []
assert test_out == split_into_fibo(test)

test = "1123581321345589144233377610987"
test_out = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
assert test_out == split_into_fibo(test)

test = "01123581321345589144233377610987159725844181"
test_out = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
assert test_out == split_into_fibo(test)

test = "0000"
test_out = [0, 0, 0, 0]
assert test_out == split_into_fibo(test)

test = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
test_out = []
assert test_out == split_into_fibo(test)
