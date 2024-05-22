# Given a string s, partition s such that every substring of the partition
#  is a palindrome.
# Return all possible palindrome partitioning of s.
# ---------------------------
# 1 <= s.length <= 16
# s contains only lowercase English letters.
from random import choice
from string import ascii_lowercase


def partition(s: str) -> list[list[str]]:
    # working_sol (43.07%, 66.68%) -> (472ms, 35.20mb)  time: O(n * 2 ** n) | space: O(n)
    out: list[list[str]] = []

    def is_pal(sub: str) -> bool:
        middle: int = len(sub) // 2
        if len(sub) % 2:
            return sub[:middle] == sub[:middle:-1]
        return sub[:middle] == sub[:middle - 1:-1]

    def check(start: int, path: list[str]) -> None:
        if len(s) <= start:
            out.append(path)
            return
        # Create a palindrome if we can and continue from it.
        for index in range(start, len(s)):
            cur_pal: str = s[start: index + 1]
            if is_pal(cur_pal):
                check(index + 1, path + [cur_pal])

    check(0, [])
    return out


# Time complexity: O(n * 2 ** n) <- n - length of an input string `s`.
# Worst case: we will start palindrome from every index `start` => O(n * 2 ** n).
# ---------------------------
# Auxiliary space: O(n)
# We're always going to have `path` with the same # of symbols in stored strings, but # of these strings...
# Recursion stack is linear and depth == `n`, because in the worst case, every symbol is palindrome => O(n).
# Slicing to check for a `is_pal` also will take O(n), because we're creating two halves of the `s` => O(2n).
# Dunno, how we can get a # of partitions, but guess it should be linear as well => O(konst * n).


test: str = "aab"
test_out: list[list[str]] = [["a", "a", "b"], ["aa", "b"]]
assert test_out == partition(test)

test = "a"
test_out = [["a"]]
assert test_out == partition(test)

test = "abbab"
test_out = [["a", "b", "b", "a", "b"], ["a", "b", "bab"], ["a", "bb", "a", "b"], ["abba", "b"]]
assert test_out == partition(test)

test = ''.join([choice(ascii_lowercase) for _ in range(16)])
print(test)
