# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
from itertools import combinations
from numpy import matrix as mt


def total_combs(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    options = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    if len(digits) == 1:
        return options[digits[0]]
    combs = []
    to_use = []
    for digit in digits:
        to_use.append(options[digit])
    print(to_use)
    for x in range(len(to_use[0])):
        first = to_use[0][x]
        for y in range(len(to_use[1])):
            second = to_use[1][y]
            for z in range(len(to_use[2])):
                third = to_use[2][z]
                to_add = first + second + third
                combs.append(to_add)



    return combs


# test1 = "23"
# test1_out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# print(total_combs(test1))
# test2 = "23456789"
# print(total_combs(test2))
# combb = combinations(test2, r=2)
# test3 = set()
# for _ in combb:
#     strs = _[0] + _[1]
#     test3.add(strs)
# for _ in test3:
#     assert _ in total_combs(test2)

# test3 = ""
# print(total_combs(test3))
# test4 = "2"
# print(total_combs(test4))
# test5 = "6"
# print(total_combs(test5))
# failed test5, cuz made a typo in dict m, m, o -> m, n, o  .......................nc
# test6 = "22"
# print(total_combs(test6))
# failed tes6, cuz im using SET and instead of using sorted() on str I was brute checking more or less and forgot equal
test7 = "234"
test7_out = ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
print(total_combs(test7))
assert test7_out == total_combs(test7)

# rebuild. cuz we need to check whole number not just combs of 2 digits
# test8 = "954"
# print(total_combs(test8))