# You are given a binary string s and a positive integer k.
# A substring of s is beautiful if the number of 1's in it is exactly k.
# Let len be the length of the shortest beautiful substring.
# Return the lexicographically smallest beautiful substring of string s
#  with length equal to len.
# If s doesn't contain a beautiful substring, return an empty string.
# A string a is lexicographically larger than a string b (of the same length)
#  if in the first position where a and b differ,
#  a has a character strictly larger than the corresponding character in b.
# For example, "abcd" is lexicographically larger than "abcc" because the first position
#  they differ is at the fourth character, and d is greater than c.
# --- --- --- ---
# 1 <= s.length <= 100
# 1 <= k <= s.length


def shortest_beautiful_substring(s: str, k: int) -> str:
    # working_solution: (100%, 30.63%) -> (0ms, 19.33mb)  Time: O(s) Space: O(s)
    max_limit: int = 105
    out: str = ''.join(['1' for _ in range(max_limit)])
    current: int = 0
    start: int = 0
    end: int = 0
    while end < len(s):
        current += 1 if '1' == s[end] else 0
        while k < current or ('0' == s[start] and k == current):
            current -= 1 if '1' == s[start] else 0
            start += 1
        if k == current:
            cur_len: int = (end - start) + 1
            if cur_len < len(out):
                out = s[start: end + 1]
            elif cur_len == len(out):
                out = min(
                    s[start: end + 1],
                    out
                )
        end += 1
    
    return out if len(out) != max_limit else ''


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = '100011001'
test_k: int = 3
test_out: str = '11001'
assert test_out == shortest_beautiful_substring(test, test_k)

test = '1011'
test_k = 2
test_out = '11'
assert test_out == shortest_beautiful_substring(test, test_k)

test = '000'
test_k = 1
test_out = ''
assert test_out == shortest_beautiful_substring(test, test_k)
