# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
from itertools import combinations
from numpy import matrix as mt


def total_combs(digits: str) -> list[str]:
    # working_sol (23.18%, 19.89%) - brute is no Good.
    # if len(digits) == 0:
    #     return []
    # options = {
    #     "2": ["a", "b", "c"],
    #     "3": ["d", "e", "f"],
    #     "4": ["g", "h", "i"],
    #     "5": ["j", "k", "l"],
    #     "6": ["m", "n", "o"],
    #     "7": ["p", "q", "r", "s"],
    #     "8": ["t", "u", "v"],
    #     "9": ["w", "x", "y", "z"],
    # }
    # if len(digits) == 1:
    #     return options[digits[0]]
    # combs = []
    # to_use = []
    # for digit in digits:
    #     to_use.append(options[digit])
    # for x in range(len(to_use[0])):
    #     first = to_use[0][x]
    #     for y in range(len(to_use[1])):
    #         second = to_use[1][y]
    #         if len(to_use) == 2:
    #             to_add = first + second
    #             combs.append(to_add)
    #             continue
    #         for z in range(len(to_use[2])):
    #             third = to_use[2][z]
    #             if len(to_use) == 3:
    #                 to_add = first + second + third
    #                 combs.append(to_add)
    #                 continue
    #             for g in range(len(to_use[3])):
    #                 fourth = to_use[3][g]
    #                 to_add = first + second + third + fourth
    #                 combs.append(to_add)
    # return combs
    # working sol - googled (41.43% , 98.2%)
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
    added = total_combs(digits[:-1])
    to_add = options[digits[-1]]
    combs = [a + b for a in added for b in to_add]
    return combs




test1 = "23"
test1_out = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(total_combs(test1))
assert test1_out == total_combs(test1)
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
test6 = "22"
print(total_combs(test6))
# failed tes6, cuz im using SET and instead of using sorted() on str I was brute checking more or less and forgot equal
test7 = "234"
test7_out = ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
print(total_combs(test7))
assert test7_out == total_combs(test7)
# task limiting numbers from 0-4, so I can make brute options for 2, 3, 4 or ????
# try to commit and not hit TLE with brute at least for 1 time
# Brute is working 23.18% , 19.89%. But it's only for 0-4  it's a bad solution....
test8 = "954"
print(total_combs(test8))
