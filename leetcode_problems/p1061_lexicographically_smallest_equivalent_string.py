# You are given two strings of the same length s1 and s2 and a string baseStr.
# We say s1[i] and s2[i] are equivalent characters.
#  - For example, if s1 = "abc" and s2 = "cde",
#   then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:
#  - Reflexivity: 'a' == 'a'.
#  - Symmetry: 'a' == 'b' implies 'b' == 'a'.
#  - Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc"
#  and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed",
#  and "aab" is the lexicographically smallest equivalent string of baseStr.
# Return the lexicographically smallest equivalent string of baseStr
#  by using the equivalency information from s1 and s2.
# ---------------------------
# 1 <= s1.length, s2.length, baseStr <= 1000
# s1.length == s2.length
# s1, s2, and baseStr consist of lowercase English letters.
from collections import defaultdict


def smallest_equivalent_string(s1: str, s2: str, baseStr: str) -> str:
    # working_sol (5.11%, 7.30%) -> (57ms, 18.26mb)  time: O(s1 + s2) | space: O(s1 + s2)
    char1: str
    char2: str

    # { char: set(equivalent) }
    graph: dict[str, set[str]] = defaultdict(set)
    for index in range(len(s1)):
        char1, char2 = s1[index], s2[index]
        graph[char1].add(char2)
        graph[char2].add(char1)
    
    # { char: min_equivalent }
    minimals: dict[str, str] = {}
    # We can use DFS to get the smallest, and cache it for each with `minimals`.
    def dfs(node: str, visited: set[str]) -> str:
        nonlocal minimals
        if node in minimals and node < minimals[node]:
            return minimals[node]

        min_equiv: str = min('z', node)
        for edge in graph[node]:
            if edge in visited:
                continue
            visited.add(edge)
            min_equiv = min(
                min_equiv,
                dfs(edge, visited)
            )
    
        return min_equiv
    
    out: list[str] = []
    for b_char in baseStr:
        checked: set[str] = set(b_char)
        min_path: str = dfs(b_char, checked)
        out.append(min_path)
        # We found minimal for all the values in the DFS chain => cache it.
        for char in checked:
            if char in minimals:
                minimals[char] = min(
                    min_path,
                    minimals[char]
                )
            else:
                minimals[char] = min_path
    
    return ''.join(out)


# Time complexity: O(s1 + s2)
# Always using DFS and check every char of the `s1` and `s2`, once => O(s1 + s2).
# ---------------------------
# Auxiliary space: O(s1 + s2)
# `graph` <- allocates space for each char of `s1`, `s2` => O(s1 + s2).
# `minimals` <- allocates space for each char of `s1`, `s2` => O(2 * (s1 + s2)).
# In the worst case, path will include every char from `s1` and `s2`.
# `checked` <- allocates space for this path => O(3 * (s1 + s2)).


test_s1: str = 'parker'
test_s2: str = 'morris'
test_base: str = 'parser'
test_out: str = 'makkek'
assert test_out == smallest_equivalent_string(test_s1, test_s2, test_base)

test_s1 = 'hello'
test_s2 = 'world'
test_base = 'hold'
test_out = 'hdld'
assert test_out == smallest_equivalent_string(test_s1, test_s2, test_base)

test_s1 = 'leetcode'
test_s2 = 'programs'
test_base = 'sourcecode'
test_out = 'aauaaaaada'
assert test_out == smallest_equivalent_string(test_s1, test_s2, test_base)
