# You are given three arrays of length n that describe the properties of n coupons:
#  code, businessLine, and isActive.
# The ith coupon has:
#  - code[i]: a string representing the coupon identifier.
#  - businessLine[i]: a string denoting the business category of the coupon.
#  - isActive[i]: a boolean indicating whether the coupon is currently active.
# A coupon is considered valid if all of the following conditions hold:
#  1. code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9)
#   and underscores (_).
#  2. businessLine[i] is one of the following four categories:
#   "electronics", "grocery", "pharmacy", "restaurant".
#  3. isActive[i] is true.
# Return an array of the codes of all valid coupons, sorted first by their businessLine
#  in the order: "electronics", "grocery", "pharmacy", "restaurant",
#  and then by code in lexicographical (ascending) order within each category.
# --- --- --- ---
# n == code.length == businessLine.length == isActive.length
# 1 <= n <= 100
# 0 <= code[i].length, businessLine[i].length <= 100
# code[i] and businessLine[i] consist of printable ASCII characters.
# isActive[i] is either true or false.
from string import ascii_letters, digits


def validate_coupons(
    code: list[str],
    businessLine: list[str],
    isActive: list[bool],
) -> list[str]:
    # working_solution: (100%, 55.43%) -> (0ms, 18.08mb)  Time: O(n * m) Space: O(n)
    chars_allowed: set[str] = {
        *ascii_letters,
        *digits, 
        '_'
    }
    blines_order: list[str] = ["electronics", "grocery", "pharmacy", "restaurant"]
    blines_allowed: dict[str, list[str]] = {
        bline: [] for bline in blines_order
    }
    for index in range(len(code)):
        promo, bline, active = code[index], businessLine[index], isActive[index]
        if not active:
            continue
        if bline not in blines_allowed:
            continue
        incorrect: bool = False
        if not promo:
            continue
        for char in promo:
            if char not in chars_allowed:
                incorrect = True
                break
        if incorrect:
            continue
        blines_allowed[bline].append(promo)

    out: list[str] = []
    for bline in blines_order:
        out.extend(
            sorted(blines_allowed[bline])
        )

    return out


# Time complexity: O(n * m)
# n - length of the input array `code`,
# m - average length of the `code` strings.
# We check every char of the strings in the `code`, once => O(n * m).
# --- --- --- ---
# Space complexity: O(n)
# `out` <- allocates space for each promo from the `code` => O(n).


test_code: list[str] = ["SAVE20", "", "PHARMA5", "SAVE@20"]
test_blines: list[str] = ["restaurant", "grocery", "pharmacy", "restaurant"]
test_active: list[bool] = [True, True, True, True]
test_out: list[str] = ["PHARMA5", "SAVE20"]
assert test_out == validate_coupons(test_code, test_blines, test_active)

test_code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"]
test_blines = ["grocery", "electronics", "invalid"]
test_active = [False, True, True]
test_out = ["ELECTRONICS_50"]
assert test_out == validate_coupons(test_code, test_blines, test_active)
