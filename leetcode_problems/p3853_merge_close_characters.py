# You are given a string s consisting of lowercase English letters and an integer k.
# Two equal characters in the current string s are considered close
#  if the distance between their indices is at most k.
# When two characters are close, the right one merges into the left.
# Merges happen one at a time, and after each merge,
#  the string updates until no more merges are possible.
# Return the resulting string after performing all possible merges.
# Note: If multiple merges are possible, always merge the pair
#  with the smallest left index. If multiple pairs share the smallest left index,
#  choose the pair with the smallest right index.
# --- --- --- ---
# 1 <= s.length <= 100
# 1 <= k <= s.length
# s consists of lowercase English letters.


def merge_characters(s: str, k: int) -> str:
    # working_solution: (100%, 95.24%) -> (0ms, 19.20mb)  Time: O(s) Space: O(s)
    # Essentially we're just deleting everything we meet.
    # If it fits in the `<= k` window.
    # { char: last_index before `> k`}
    fast_indexes: dict[str, int] = {}
    # Adjustment we need after every deleted char.
    index_shift: int = 0
    out: list[str] = []
    for index, char in enumerate(s):
        if char not in fast_indexes:
            fast_indexes[char] = index - index_shift
            out.append(char)
            continue
        distance: int = (index - index_shift) - fast_indexes[char]
        # Update char starting point and add this in the result.
        if distance > k:
            out.append(char)
            fast_indexes[char] = index - index_shift
        else:
            index_shift += 1
            
    return ''.join(out)


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "abca"
test_k: int = 3
test_out: str = "abc"
# assert test_out == merge_characters(test, test_k)

# test = "aabca"
# test_k = 2
# test_out = "abca"
# assert test_out == merge_characters(test, test_k)

test = "yybyzybz"
test_k = 2
test_out = "ybzybz"
assert test_out == merge_characters(test, test_k)
