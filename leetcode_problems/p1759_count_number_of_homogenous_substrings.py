# Given a string s, return the number of homogenous substrings of s.
# Since the answer may be too large, return it modulo 10 ** 9 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.
# -------------------
# 1 <= s.length <= 10 ** 5
# s consists of lowercase letters.


def count_homog(s: str) -> int:
    # working_sol (84.53%, 96.76%) -> (97ms, 17.1mb)  time: O(n) | space: O(1)
    # subs == (len(seq) * (len(seq) + 1)) // 2.
    # seq <- current sequence we have.
    subs: int = 0
    cur_index: int = 0
    for x in range(len(s)):
        if s[x] != s[cur_index]:
            seq_len: int = x - cur_index
            subs += seq_len * (seq_len + 1) // 2
            cur_index = x
    # Last index never checked.
    # So, we need extra addition.
    seq_len = len(s) - cur_index
    subs += seq_len * (seq_len + 1) // 2
    return subs % (10 ** 9 + 7)


# Time complexity: O(n) -> every index used once + 1 extra use for last sequence => O(n + 1).
# n - length of input string 's'^^|
# Auxiliary space: O(1) -> only 3 constant INTs used, none of them depends on input => O(1).
# -------------------
# There's 2 options I remember:
# 1 -> (len(seq) * (len(seq) + 1)) // 2
# 2 -> we take basic as sequence with 1 element and for every correct element we can use in
# combination we're adding new length to our basic (1 + len(new_seq) + len(new_seq) etc.)
# where: new_seq is new length of sequence we currently have.
# Both should be correct.
# Actually first faster, better to  use it.


test: str = "abbcccaa"
test_out: int = 13
assert test_out == count_homog(test)

test = "xy"
test_out = 2
assert test_out == count_homog(test)

test = "zzzzz"
test_out = 15
assert test_out == count_homog(test)

test = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
test_out = 561
assert test_out == count_homog(test)
