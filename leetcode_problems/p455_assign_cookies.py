# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child
#  will be content with; and each cookie j has a size s[j]. If s[j] >= g[i],
#  we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
# ----------------------
# 1 <= g.length <= 3 * 10 ** 4
# 0 <= s.length <= 3 * 10 ** 4
# 1 <= g[i], s[j] <= 2 ** 31 - 1
from random import randint


def find_content_children(g: list[int], s: list[int]) -> int:
    # working_sol (98.83%, 13.41%) -> (128ms, 19.19mb)  time: O(n * log n) | space: O(n)
    # 0-cookies.
    if not s:
        return 0
    # We only care if we can give cookie of size, which child demands.
    # So, just sort() and keep giving cookies while we can.
    g.sort()
    s.sort()
    cookie_ind: int = 0
    child_ind: int = 0
    out: int = 0
    while cookie_ind < len(s) and child_ind < len(g):
        if g[child_ind] <= s[cookie_ind]:
            out += 1
            cookie_ind += 1
            child_ind += 1
        else:
            cookie_ind += 1
    return out


# Time complexity: O(n * log n) <- n - length of input array `g` or `s`.
# Worst case: len(g) == len(s), and we can distribute all cookies.
# We will sort both arrays => O(2 * (n * log n)).
# And we will traverse both arrays once => O(2n).
# ----------------------
# Auxiliary space: O(n).
# Standard builtin sort will take `n` to sort() => O(2n).
# Extra 3 constant INTs which doesn't depend on input.


test: list[int] = [1, 2, 3]
test_s: list[int] = [1, 1]
test_out: int = 1
assert test_out == find_content_children(test, test_s)

test = [1, 2]
test_s = [1, 2, 3]
test_out = 2
assert test_out == find_content_children(test, test_s)

test = [randint(1, 2 ** 31 - 1) for _ in range(3 * 10 ** 3)]
test_s = [randint(1, 2 ** 31 - 1) for _ in range(3 * 10 ** 3)]
print(test)
print('===========!')
print(test_s)
