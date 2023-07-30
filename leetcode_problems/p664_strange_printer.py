# There is a strange printer with the following two special properties:
#   The printer can only print a sequence of the same character each time.
#   At each turn, the printer can print new characters starting from and ending
#     at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.
# -------------------------
# 1 <= s.length <= 100
# s consists of lowercase English letters.
from string import ascii_lowercase
from random import choice


def strange_printer(s: str) -> int:
    # working_sol (77.42%, 28.39%) -> (436ms, 19.5mb)  time: O((log n) * 2 ** n) | space: O(2 ** n)
    recur_cache: dict[tuple[int, int], int] = {}

    def sub(start: int, end: int) -> int:
        if (start, end) in recur_cache:
            return recur_cache[start, end]
        # Any symbol by itself == 0, cuz
        # extra adding +1 for everyone.
        if start >= end:
            return 0
        # 1 turn to place Any, and recalling to find
        # slices for this start_index.
        turns: int = sub(start + 1, end) + 1
        # If there's only 1 symbol from start_index to end.
        # Always getting +1
        for x in range(start + 1, end + 1):
            # If there's duplicates, then we need to
            # recheck slices for a minimum construct way.
            if s[start] == s[x]:
                turns = min(turns, sub(start, x - 1) + sub(x, end))
        recur_cache[start, end] = turns
        return turns
    # Always extra +1 for symbol itself, cuz we're starting from start_index + 1.
    return sub(0, len(s) - 1) + 1


# Time complexity: O((log n) * 2 ** n) -> recursion tree with depths of n and 2 options for duplicates,
# n - len of input_array^^|  if there's no duplicates then it's just n -> extra we're searching part of the array
#                            for every call, in the worst case part == (n - 1) for index == 0 => O((log n) * 2 ** n).
# Auxiliary space: O(2 ** n) -> saving every call with inputs into dictionary for reuse => O(2 ** n).
# -------------------------
# Any symbol by itself always takes 1 turn, if there's another symbol, and it's after some1 else
# it's still 1 turn. But if we're reusing this symbol after other symbols, like -> "ababa" then it's 3 turns.
# "aabb" -> no reuse of 'a' always just 1 for each.
# "aabba" -> we're reusing it but there's no other symbol(breaker), so it's still only 2.
# "aababa" -> now we're having breaker 'b', so we need to replace 'a' after all 'b' placed -> turns == 3.
# We need to check all sub-arrays from
# start == cur_symbol_index + 1 and end == end of the array <- inclusive
# start == cur_symbol_index and end == duplicate_index - 1
# start == duplicate_index and end == end of the array <- inclusive
# Because we need to know how much other symbols placed between cur_symbol and its duplicate,
# extra we need to know if there's other symbols after duplicate, cuz if there's other symbols then it's extra
# turns to place them if they aren't met before.
# Like "aababa" -> starting from end, we have subarray "a", it's only 1 option by itself, turns == 1 ->
# -> next "ba", there's no duplicates turns == 1 for already returned 'a' and + 1 for symbol itself
# ! every call of recursion is always added +1 cuz it's 1turn to place symbol by itself ! ->
# -> next "aba", there's 1 duplicate, and we need to check how many turns it's taking to place everything between
# cur_symbol 'a' and duplicate at [-1] == 'a', extra to this if there's anything after duplicate? ->
# -> in this case there's only 1 symbol between and duplicate => +1 by itself +1 for other symbol, turns == 2 ->
# -> next "baba", we already stored result for symbols between, in this cas it's only 'a' so it's going to take 2 turns
# and +1 for itself, turns == 3 ->
# -> next "ababa", now it's 2 duplicates of 'a' we already know how many turns it's taking to place them,
# [-1] is just 1, [-3] its 2 turns, we need minimum value of turns.
# So we're slicing original string like -> "aababa":
# [-2] slices: "a" just [-1], start == end == 1 turn -> 1 turn
# [-3] slices: "ab" and "a" 2 calls leading to start == end == 1turn -> 2 turns
# [-4] slices: "ba" and "ba", both calls will give 2 turns => min(3, 2 + 2) <- having 3 from recursion return with
# previous slice given us 2 turns, and +1 for our current symbol.
# [-5] slices: "ab" and "aba", to form "ab" -> 1 turns, return from 0 and itself, to form "aba" -> 2 turns,
# still 3 turns.
# [-6] slices: "a" and "ababa" + "aab" and "aba" -> 3 turns. "a" -> 0 start == end, + "ababa" -> already stored
# from [-5] == 3 => 3 turns, "aab" -> 0 + 1, + "aba" -> 0 + 1 => 2 turns.
# Extra +1 after recursion end, cuz we're not including symbol_itself until we're done with slices.
# ^^Really bad understanding need to learn more about DP problems.


test1 = "aaabbb"
test1_out = 2
assert test1_out == strange_printer(test1)

test2 = "aba"
test2_out = 2
assert test2_out == strange_printer(test2)

test3 = "aaatbbbabt"
test3_out = 4
assert test3_out == strange_printer(test3)

test4 = "aaabbbab"
test4_out = 3
assert test4_out == strange_printer(test4)

test5 = "wekhkvkjticmlvtqoqez"
test5_out = 15
assert test5_out == strange_printer(test5)

test: str = ""
for _ in range(100):
    test += choice(ascii_lowercase)
print(test)
