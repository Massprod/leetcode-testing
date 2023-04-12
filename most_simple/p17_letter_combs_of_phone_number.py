# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
from itertools import combinations


def total_combs(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    options = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "m", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    if len(digits) == 1:
        return options[digits[0]]
    digits = list(digits)
    digits.sort()
    to_use = set()
    combs = []
    for x in range(len(digits)):
        first = digits[x]
        for y in range(len(digits)):
            if y == x:
                continue
            second = digits[y]
            if first > second:
                digit = second + first
                to_use.add(digit)
            elif second > first:
                digit = first + second
                to_use.add(digit)
    for num in to_use:
        first_values = options[num[0]]
        second_values = options[num[1]]
        for x in range(len(first_values)):
            first = first_values[x]
            for y in range(len(second_values)):
                second = second_values[y]
                comb = first + second
                combs.append(comb)
    return combs


test1 = "23"
test1_out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(total_combs(test1))
test2 = "23456789"
# print(total_combs(test2))
# combb = combinations(test2, r=2)
# test3 = set()
# for _ in combb:
#     strs = _[0] + _[1]
#     test3.add(strs)
# for _ in test3:
#     assert _ in total_combs(test2)

test3 = ""
print(total_combs(test3))
test4 = "2"
print(total_combs(test4))
