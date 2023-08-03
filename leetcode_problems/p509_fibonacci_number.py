# The Fibonacci numbers, commonly denoted F(n) form a sequence,
#   called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
# That is,
#   F(0) = 0, F(1) = 1
#   F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
# -------------
# 0 <= n <= 30


def fib(n: int) -> int:
    # working_sol (96.57%, 91.50%) -> (35ms, 16.18mb)  time: O(n) | space: O(n)
    recur_cache: dict[int, int] = {
        0: 0,
        1: 1,
    }

    def fibo(k: int) -> int:
        if k in recur_cache:
            return recur_cache[k]

        recur_cache[k] = fibo(k - 1) + fibo(k - 2)
        return recur_cache[k]

    return fibo(n)


# Time complexity: O(n) -> recursion tree with 2 options and depths of n => O(2 ** n) ->
# n - input value^^|       -> but we're using cache to store all calls from 1 -> 30, and every other call
#                          with fibo(k - 2) is going to reuse this calls, cuz first fibo(k - 1) is called => O(n).
# Auxiliary space: O(n) -> there's only max == n calls, and every call is cached in dictionary, once => O(n).
# -------------
# Just building standard by description given.


test: int = 2
test_out: int = 1
assert test_out == fib(test)

test = 3
test_out = 2
assert test_out == fib(test)

test = 4
test_out = 3
assert test_out == fib(test)

test = 30
test_out = 832040
assert test_out == fib(test)
