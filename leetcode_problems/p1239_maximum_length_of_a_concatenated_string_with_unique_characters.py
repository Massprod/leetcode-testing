# You are given an array of strings arr.
# A string s is formed by the concatenation of a subsequence of arr that has unique characters.
# Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting some
#  or no elements without changing the order of the remaining elements.
# -------------------------
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.
from random import choice, randint
from string import ascii_lowercase


def max_length(arr: list[str]) -> int:
    # working_sol (99.00%, 75.18%) -> (51ms, 16.6mb)  time: O(n * 2 ** n) | space: O(n)
    # Maximum length == 26 == whole lowercase ENG alph.
    # So, we can use set() with all used symbols or just INT with LSB -> MSB (0 -> 26).

    # We're using (index + 1) as step, so we need to have extra bit_mask to check index == len(arr).
    # Extra, if we have duplicates in subsequence itself, we can't use it.
    # But we can't leave it as 0, because (0 & w.e) will always give us False.
    # And we need to completely ignore this values, so we're marking it with full bits 0 -> 26 placed.
    full_taken: int = 0
    for _ in range(26):
        full_taken += 1
        full_taken <<= 1

    def to_bits(string: str) -> int:
        cur: int = 0
        for char in string:
            position: int = ord(char) - ord('a')
            if cur & (1 << position):
                return full_taken
            cur = cur ^ (1 << position)
        return cur

    # Convert all subsequences into bitmasks, for easier comparing and less lines in check().
    # And extra [0] for: ! cur_path & bit_masks[option] when option == len(arr) !.
    bit_masks: list[int] = [to_bits(subseq) for subseq in arr] + [0]

    def check(index: int, path: int) -> int:
        if index == len(arr):
            return path
        # Subsequence have duplicated chars in itself => not usable, ignore.
        if bit_masks[index] == full_taken:
            return check(index + 1, path)
        # Otherwise, we need to include it in our `path`.
        cur_path: int = path ^ bit_masks[index]
        out: int = 0
        # Continue building from current subsequence to the end.
        for option in range(index + 1, len(arr) + 1):
            # Values with no duplicated bits always gives 0.
            if not cur_path & bit_masks[option]:
                new_seq = check(option, cur_path)
                # We need maximum size.
                if out.bit_count() < new_seq.bit_count():
                    out = new_seq
        return out

    max_bits: int = 0
    # We should start building from any subsequence.
    for start in range(len(arr)):
        res: int = check(start, 0)
        res_bits: int = res.bit_count()
        if max_bits < res_bits:
            max_bits = res_bits
    return max_bits


# Time complexity: O(n * 2 ** n) <- n - length of input array `arr`.
# Creating array with all bit masks for every subsequence in `arr` == `bit_masks`.
# For every subsequence we traverse it's whole size => O(n * m) <- m - average length of subsequence in `arr`.
# Looping through all possible `start` index position, from whom we can start building our maximum path.
# And for every `start` index, we're always check what's left and 2 option (take, or not) => O(n * 2 ** n).
# Maybe not, maybe it's O(n ** 2), because we just check every combination.
# -------------------------
# Auxiliary space: O(n).
# Creating array with all bit masks for every subsequence in `arr` == `bit_masks` => O(n).
# Extra recursion stack can be a max size of `n`, if we can build (0 -> last) subsequences chain => O(n).


test: list[str] = ["un", "iq", "ue"]
test_out: int = 4
assert test_out == max_length(test)

test = ["aa", "bb"]
test_out = 0
assert test_out == max_length(test)

test = ["cha", "r", "act", "ers"]
test_out = 6
assert test_out == max_length(test)

test = ["abcdefghijklmnopqrstuvwxyz"]
test_out = 26
assert test_out == max_length(test)

test = ["rg", "t", "m", "nmj", "nyw", "bij", "osm", "x", "ao", "wr", "n", "cel", "n", "kr", "w", "d"]
test_out = 17
assert test_out == max_length(test)

test = ["a", "abc", "d", "de", "def"]
test_out = 6
assert test_out == max_length(test)

test = [''.join(choice(ascii_lowercase) for char in range(randint(1, 3))) for sub in range(16)]
print(test)
