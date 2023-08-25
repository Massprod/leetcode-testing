# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings
#  respectively, such that:
#   s = s1 + s2 + ... + sn
#   t = t1 + t2 + ... + tm
#   |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.
# -----------------
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
from random import choice, sample
from string import ascii_lowercase


def is_inter_leave(s1: str, s2: str, s3: str) -> bool:
    # working_sol (95.55%, 40.52%) -> (39ms, 17.14mb)  time: O(m * n) | space: O(m * n)
    # Interleaving == s1 + s2, insta False is lenght isn't correct.
    if len(s1) + len(s2) != len(s3):
        return False
    recur_cache: dict[tuple[int, int, int]: bool] = {}

    def check(s1_index: int, s2_index: int, s3_index: int) -> bool:
        # Reuse
        if (s1_index, s2_index) in recur_cache:
            return recur_cache[s1_index, s2_index, s3_index]
        # s1 + s2 exhausted at the same time -> correct path.
        if s1_index == len(s1) and s2_index == len(s2):
            return True
        # We don't care about symbols used and in what order,
        #  all we care is that they need's to be used from S1 or S2.
        # One by one, so we can just take correct symbol from S1 or S2,
        #  until they're not exhausted.
        if s1_index != len(s1) and s3[s3_index] == s1[s1_index]:
            # And if any correct path found, insta return.
            if check(s1_index + 1, s2_index, s3_index + 1):
                return True
        if s2_index != len(s2) and s3[s3_index] == s2[s2_index]:
            if check(s1_index, s2_index + 1, s3_index + 1):
                return True
        # Cull extra calcs.
        recur_cache[s1_index, s2_index, s3_index] = False
        return False

    return check(0, 0, 0)


# Time complexity: O(m * n) -> recursion with memorization, so it will cull repeats, and we're checking
# n - len of input_s1^^|  all m * n pairs of indexes from S1 and S2 => O(m * n).
# m - len of input_s2^^|  S3 index doesn't matter, cuz we're making calls depending on S1 and S2.
# Auxiliary space: O(m * n) -> every index pair check is saved into a dict_cache => O(m * n).
# -----------------
# Check for correct symbol to use from s1 or s2 and use it?
# correct_symbol == s3_symbol
# And we don't actually care from who we use s1 or s2 until it's correct_symbol.
# Actually we should care, but if we will check every index then it doesn't matter it just Incorrect path and False.
# And if we built correct path == s1 + s2 = s3 -> then there's way to get interleaving.
# So it should be like -> take any correct_symbol for s1 or s2 until they're present. Should be correct..


test_s1: str = "aabcc"
test_s2: str = "dbbca"
test_s3: str = "aadbbcbcac"
test_out: bool = True
assert test_out == is_inter_leave(test_s1, test_s2, test_s3)

test_s1 = "aabcc"
test_s2 = "dbbca"
test_s3 = "aadbbbaccc"
test_out = False
assert test_out == is_inter_leave(test_s1, test_s2, test_s3)

test_s1 = ""
test_s2 = ""
test_s3 = ""
test_out = True
assert test_out == is_inter_leave(test_s1, test_s2, test_s3)

test_s3 = ''
for _ in range(200):
    test_s3 += choice(ascii_lowercase)
test_s2 = ''.join(sample(test_s3[:100], 100))
test_s1 = ''.join(sample(test_s3[100:], 100))
print(test_s1)
print('------')
print(test_s2)
print('------')
print(test_s3)
