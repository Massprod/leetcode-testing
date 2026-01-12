# You are given a string s consisting only of lowercase English letters.
# A prefix of s is called a residue if the number of distinct characters
#  in the prefix is equal to len(prefix) % 3.
# Return the count of residue prefixes in s.
# A prefix of a string is a non-empty substring that starts from the beginning
#  of the string and extends to any point within it.
# --- --- --- ---
# 1 <= s.length <= 100
# s contains only lowercase English letters.


def residue_prefixes(s: str) -> int:
    # working_solution: (100%, 100%) -> (0ms, 19.36mb)  Time: O(s) Space: O(s)
    out: int = 0
    prefix: set[str] = set()
    prefix_length: int = 0
    for char in s:
        prefix.add(char)
        prefix_length += 1
        if len(prefix) == (prefix_length % 3):
            out += 1
    
    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)
# In the worst case, there's only unique chars in `s` => O(s).


test: str = "abc"
test_out: int = 2
assert test_out == residue_prefixes(test)

test = "dd"
test_out = 1
assert test_out == residue_prefixes(test)

test = "bob"
test_out = 2
assert test_out == residue_prefixes(test)
