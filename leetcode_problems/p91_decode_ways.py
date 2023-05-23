# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#       'A' -> "1"
#       'B' -> "2"
#       ...
#       'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped
# back into letters using the reverse of the mapping above (there may be multiple ways).
# For example, "11106" can be mapped into:
#       "AAJF" with the grouping (1 1 10 6)
#       "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06"
# cannot be mapped into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.
# ----------------------
# 1 <= s.length <= 100  ,  s contains only digits and may contain leading zero(s).


def num_decoding(s: str) -> int:
    # time_limit
    if len(s) == 0:
        return 1
    if s[0] == 0:
        return 0
    correct_paths: int = 0
    if 0 < int(s[0]) < 10:
        correct_paths += num_decoding(s[1:])
    if len(s) > 1 and 9 < int(s[0] + s[1]) < 27:
        correct_paths += num_decoding(s[2:])
    return correct_paths


# Time complexity: O(2 ** n) -> recursion tree with 2 branches and n depth.
# Space complexity: O(m * g) -> for every call we're storing some slice with g size, from original input string.
# m - number of recursion calls ^^
# g - size of a slice^^
# -----------------------
# No idea how to made this faster. There's no way for me without knowing some extra basics. like in p79 ->
# working_sol, but I just didn't know a trick. Better to google and rebuild.


def dp_num_decoding(s: str) -> int:
    # working_sol (31.34%, 33.31%) -> (46ms, 16.3mb)  time: O(n) | space: O(n + 1)
    if int(s[0]) == 0:
        return 0
    path: list[int] = [1, 1] + [0] * (len(s) - 1)
    for x in range(2, len(s) + 1):
        if 0 < int(s[x - 1]) < 10:
            path[x] += path[x - 1]
        if 9 < int(s[x - 2] + s[x - 1]) < 27:
            path[x] += path[x - 2]
    return path[-1]


# Time complexity: O(n) -> looping once through whole input_string => O(n) <- actual loop doesn't start from 0, but
#                          we're checking it before, so it's still use of every index of an input_string
# Space complexity: O(n + 1) -> creating extra list with (n + 1) size.
# n - size of input string ^^

# Ok. First time encounter with rebuilding recursion into dp. Maybe I could rebuild others but never did,
# and in this task we're forced to do this (time_limit).
# -----------------------
# ! path[x] = path[x - 1] + path[x - 2], for x >= 2 ->
# -> where path[x - 1] == correct ways to decode with starting recursion with slice of 1 digit ->
# -> path[x - 2] == correct ways to decode with starting recursion with slice of decimal.
#   basic case we're having correct number at s[0] and s[1] ->
#   -> leaving us with 1 correct way to decode with 1 digit start ->
#   -> and another correct way with decimal start => this is why we're creating path with path[0] == 1, path[1] == 1
# Starting dp loop to find correct_ways for any string = s[:x] ->
#  for x>= 2 => path[x] == number of correct recursion calls for s[:x] string ! <- as I understand this.
# -----------------------
# Flow for a better visualization:
# "1220" -> x = 2, s[:2] == "12" -> path[2] = path[2 - 1] + path[2 - 2] both options executable ->
#        s[:2] = 2 -> correct 2 options to call recursion, with digit start =>  1 + 2
#                     and decimal start => 12
# "1220" -> x = 3, s[:3] == "122" -> path[3] = path[3 - 1] + path[3 - 2] again both options executable ->
#        s[:3] = 3 -> correct 3 options to call recursion, with digit start => 1 + 2 + 2,  1 + 22
#                     and decimal start => 12 + 2
# "1220" -> x = 4, s[:4] == "1220" -> path[4] = path[4 - 2] only one option executes ->
#        s[:4] = 2 -> correct 2 options to call recursion, with digit start => 1 + 2 + 20
#                     and decimal start => 12 + 20
# if add to this 0 than all recursion calls will be False, because start with digit can't use 2 zeroes in a row,
# and start with decimal can't use 2 zeroes in a row as well. As we walk from left to right and full length of a string.
# but if we use another correct digit => it's again summ of correct ways for 2 different recursion starts ->
# like "12201" -> start with digit => 1 + 2 + 20 + 1,
#                 start with decimal => 12 + 20 + 1,
# and it's correct with our loop, because adding this "1" leading us to correct digit execute, but not decimal.
# looping for length of string we get.
# ^^How I understand this, we're just culling recursion which has this pattern.
#   How to see this pattern and make this culling is an actual question, and I didn't find any info on that, yet.
#   Or maybe it's wrong, and this whole dp pattern is not about recursion calls,
#      but why does it correct if we count like pattern above?


test1 = "12"
test1_out = 2
print(dp_num_decoding(test1))
print(num_decoding(test1))
assert dp_num_decoding(test1) == num_decoding(test1) == test1_out

test2 = "226"
test2_out = 3
print(dp_num_decoding(test2))
print(num_decoding(test2))
assert dp_num_decoding(test1) == num_decoding(test1) == test1_out

test3 = "06"
test3_out = 0
print(dp_num_decoding(test3))
print(num_decoding(test3))
assert dp_num_decoding(test1) == num_decoding(test1) == test1_out

test4 = "11106"
test4_out = 2
print(dp_num_decoding(test4))
print(num_decoding(test4))
assert dp_num_decoding(test1) == num_decoding(test1) == test1_out

test5 = "2570543"
test5_Out = 0
print(dp_num_decoding(test5))
print(num_decoding(test5))
assert dp_num_decoding(test1) == num_decoding(test1) == test1_out

test6 = "122"
print(dp_num_decoding(test6))
print(num_decoding(test6))
assert dp_num_decoding(test1) == num_decoding(test1) == test1_out

test7 = "111111111111111111111111111111111111111111111"
print(dp_num_decoding(test7))
# print(num_decoding(test7)) # time_limit -> infinity
