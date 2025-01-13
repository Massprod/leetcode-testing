# You are given a 0-indexed string s that you must perform k replacement operations on.
# The replacement operations are given as three 0-indexed parallel arrays,
#  indices, sources, and targets, all of length k.
# To complete the ith replacement operation:
#  1. Check if the substring sources[i] occurs at index indices[i]
#     in the original string s.
#  2. If it does not occur, do nothing.
#  3. Otherwise if it does occur, replace that substring with targets[i].
# For example, if s = "abcd", indices[i] = 0, sources[i] = "ab",
#  and targets[i] = "eee", then the result of this replacement will be "eeecd".
# All replacement operations must occur simultaneously,
#  meaning the replacement operations should not affect the indexing of each other.
# The testcases will be generated such that the replacements will not overlap.
#  - For example, a testcase with s = "abc", indices = [0, 1],
#  and sources = ["ab","bc"] will not be generated because the "ab" and "bc"
#  replacements overlap.
# Return the resulting string after performing all replacement operations on s.
# A substring is a contiguous sequence of characters in a string.
# -------------------------
# 1 <= s.length <= 1000
# k == indices.length == sources.length == targets.length
# 1 <= k <= 100
# 0 <= indexes[i] < s.length
# 1 <= sources[i].length, targets[i].length <= 50
# s consists of only lowercase English letters.
# sources[i] and targets[i] consist of only lowercase English letters.
from collections import defaultdict


def find_replace_string(
        s: str, indices: list[int], sources: list[str], targets: list[str]
) -> str:
    # working_sol (100.0%, 12.97%) -> (0ms, 17.94mb)  time: O(s + n * g) | space: O(n)

    def check_start(index: int, check_string: str, start: str) -> bool:
        if index >= len(check_string):
            return False
        
        used: int = 0
        while (index < len(check_string)
               and used < len(start)
               and check_string[index] == start[used]):
            index += 1
            used += 1
        return used == len(start)
    
    # { start_index: index } <- `start_index` == index to start in `s`,
    #                           `index` == index to identify value in sources, targets
    fast_indices: dict[int, list[int]] = defaultdict(list)
    for index, start_index in enumerate(indices):
        fast_indices[start_index].append(index)
    
    out: list[str] = []
    # For every char we check => we need to skip.
    skips: int = 0
    for index, char in enumerate(s):
        if skips:
            skips -= 1
            continue
        if index in fast_indices:
            cor_len: int = 0
            cor_string: str = ''
            for check_index in fast_indices[index]:
                start_string: str = sources[check_index]
                # We need to use the longest valid option we have.
                if check_start(index, s, start_string):
                    cur_len: int = len(start_string)
                    if cur_len > cor_len:
                        cor_len, cor_string = cur_len, targets[check_index]
            if cor_string:
                out.append(cor_string)
                skips = cor_len - 1
                continue
        out.append(char)
    
    return ''.join(out)


# Time complexity: O(s + n * g) <- n - length of the input array `indices`,
#                                  g - maximum length of string in `sources`.
# In the worst case we can have `indices` with all indexes == `0`.
# So, we will just check all `sources` strings for this index => O(s + n * g).
# -------------------------
# Auxiliary space: O(n)
# `fast_indices` <- allocates space for each index of `indices` => O(n).


test: str = "abcd"
test_indices: list[int] = [0, 2]
test_sources: list[str] = ["a", "cd"]
test_targets: list[str] = ["eee", "ffff"]
test_out: str = "eeebffff"
assert test_out == find_replace_string(
    test, test_indices, test_sources, test_targets
)

test = "abcd"
test_indices = [0, 2]
test_sources = ["ab","ec"]
test_targets = ["eee","ffff"]
test_out = "eeecd"
assert test_out == find_replace_string(
    test, test_indices, test_sources, test_targets
)

test = "abcd"
test_indices = [0, 0]
test_sources = ["a", "b"]
test_targets = ["b", "c"]
test_out = "bbcd"
assert test_out == find_replace_string(
    test, test_indices, test_sources, test_targets
)
