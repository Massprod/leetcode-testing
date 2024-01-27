# You have a bomb to defuse, and your time is running out!
# Your informer will provide you with a circular array code of length of n and a key k.
# To decrypt the code, you must replace every number.
# All the numbers are replaced simultaneously.
#   - If k > 0, replace the ith number with the sum of the next k numbers.
#   - If k < 0, replace the ith number with the sum of the previous k numbers.
#   - If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0],
#  and the previous element of code[0] is code[n-1].
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
# -------------------------
# n == code.length
# 1 <= n <= 100
# 1 <= code[i] <= 100
# -(n - 1) <= k <= n - 1
from random import randint


def decrypt(code: list[int], k: int) -> list[int]:
    # working_sol (95.27%, 69.38%) -> (34ms, 16.64mb)  time: O(n) | space: O(n)
    k_sum: int = 0
    start_index: int = 0
    out: list[int] = []
    # All annulled.
    if not k:
        out = [k_sum for _ in code]
    # Standard sliding window.
    elif k > 0:
        last_index: int = k
        k_sum = sum(code[start_index: k])
        while start_index != len(code):
            if last_index == len(code):
                last_index = 0
            k_sum += code[last_index] - code[start_index]
            out.append(k_sum)
            start_index += 1
            last_index += 1
    elif k < 0:
        last_index = k
        k_sum = sum(code[k:])
        out.append(k_sum)
        while start_index != len(code) - 1:
            k_sum += code[start_index] - code[last_index]
            out.append(k_sum)
            start_index += 1
            last_index += 1
    return out


# Time complexity: O(n) <- length of input array `code`.
# Calculating original window sum() in the worst case it's (n - 1) size => O(n).
# And for every index of `code` we're changing this window in constant time => O(n).
# -------------------------
# Auxiliary space: O(n).
# Creating array `out` with the same size of `n` => O(n)


test: list[int] = [5, 7, 1, 4]
test_k: int = 3
test_out: list[int] = [12, 10, 16, 13]
assert test_out == decrypt(test, test_k)

test = [1, 2, 3, 4]
test_k = 0
test_out = [0, 0, 0, 0]
assert test_out == decrypt(test, test_k)

test = [2, 4, 9, 3]
test_k = -2
test_out = [12, 5, 6, 13]
assert test_out == decrypt(test, test_k)

test = [randint(1, 100) for _ in range(100)]
print(test)
