# Given an array of strings nums containing n unique binary strings each of length n,
#  return a binary string of length n that does not appear in nums.
# If there are multiple answers, you may return any of them.
# ----------------------
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.


def find_different_bs(nums: list[str]) -> str:
    # working_sol (46.90%, 14.4%) -> (44ms, 16.6mb)  time: O(n * n) | space: O(n)
    uniques: set[str] = set(nums)

    def recur(bstring: str) -> str:
        # Small constraints, and we only have 16 options used in `nums` at max.
        # So, it's fine to just use standard recursion with 2 options.
        # Because we will always break at 17 option at max.
        if len(bstring) == len(nums[0]):
            if bstring not in uniques:
                return bstring
            else:
                return ''
        out: str = recur(bstring + '1')
        if out:
            return out
        return recur(bstring + '0')

    return recur('')


# Time complexity: O(n * n) <- n - len of input array 'nums' + len of every string inside <- ! nums[i].length == n !.
#   Creating set with all original strings => O(n * n).
#   Recursion could have 2 ** n options to create, but because we're given that there's only 16 options in 'nums'.
#   We're always going to check only 17 options at max, cuz after 16 option created it's always correct one => O(n + 1).
# Auxiliary space: O(n).
#   Creating set with all original strings => O(n).
#   Recursion will always stop at max size == 'n' and all calls before is (n - 1, n - 2, n - 3 .. 0) => O(n).


test: list[str] = ["01", "10"]
test_out: str = "11"
assert test_out == find_different_bs(test)

test = ["00", "01"]
test_out = "11"
assert test_out == find_different_bs(test)

test = ["111", "011", "001"]
test_out = "101"
assert test_out == find_different_bs(test)
