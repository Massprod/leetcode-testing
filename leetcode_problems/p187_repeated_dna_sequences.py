# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#   For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence,
#   return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
# You may return the answer in any order.
# --------------
# 1 <= s.length <= 10 ** 5
# s[i] is either 'A', 'C', 'G', or 'T'.
from random import choice


def find_repeated_dna(s: str) -> list[str]:
    # working_sol (99.32%, 38.93%) -> (59ms, 30mb)  time: O(n) | space: O(n)
    # unique case
    if len(s) < 10:
        return []
    # first sequence
    cur_seq: str = s[:10]
    # all correct sequenced stored and counted
    repeated: dict[str, int] = {cur_seq: 1}
    # start from 10, cuz 0-9 already considered
    for x in range(10, len(s)):
        cur_seq = cur_seq[1:] + s[x]
        if cur_seq in repeated:
            repeated[cur_seq] += 1
            continue
        repeated[cur_seq] = 1
    all_repeated: list[str] = []
    for seq, occur in repeated.items():
        if occur > 1:
            all_repeated.append(seq)
    return all_repeated


# Time complexity: O(n) -> traversing whole input_string once to recreate every sequence with len == 10 => O(n) ->
# n - len of input_string^^| -> in the worst case every stored 10len sequence in a string is unique, then
#                            first [:10] is unique [1:11] is unique ...etc. to the end. In this case it should be
#                            something like 1 + 1 + 1 + .. until the last index => (n - 10) <- because every index
#                            after [9] is going to be unique and added into repeated, and after that we're checking
#                            every sequence in repeated which should be equal to (n - 10) => O(n - 10) ->
#                            -> O(n) + O(n - 10) => O(n).
# Auxiliary space: O(n) -> with the same worst case we're storing at max (n - 10) sequences with length of 10 as keys
#                          and values of them are constant INTs => O(n).
# --------------
# Well, tested with limit constraints, and it's working, unique case with len < 10 covered as well.
# Should be correct.
# --------------
# Should be default window problem with storing of all windows and simply recheck of them.


test1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
test1_out = ["AAAAACCCCC", "CCCCCAAAAA"]
print(find_repeated_dna(test1))
assert test1_out == find_repeated_dna(test1)

test2 = "AAAAAAAAAAAAA"
test2_out = ["AAAAAAAAAA"]
print(find_repeated_dna(test2))
assert test2_out == find_repeated_dna(test2)

test3 = "AAA"
test3_out = []
print(find_repeated_dna(test3))
assert test3_out == find_repeated_dna(test3)

# choices: list[str] = ["A", "C", "G", "T"]
# test: str = ""
# for _ in range(10 ** 4):
#     for y in range(10):
#         test += choice(choices)
# print(test)
# print(find_repeated_dna(test))
