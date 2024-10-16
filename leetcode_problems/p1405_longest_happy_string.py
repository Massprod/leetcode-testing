# A string s is called happy if it satisfies the following conditions:
#  - s only contains the letters 'a', 'b', and 'c'.
#  - s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#  - s contains at most a occurrences of the letter 'a'.
#  - s contains at most b occurrences of the letter 'b'.
#  - s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string.
# If there are multiple longest happy strings, return any of them.
# If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.
# ---------------------------------
# 0 <= a, b, c <= 100
# a + b + c > 0
import heapq


def longest_diverse_string(a: int, b: int, c: int) -> str:
    # working_sol (77.68%, 68.60%) -> (32ms, 16.53mb)  time: O(a + b + c) | space: O(1)
    count: int
    char: str
    next_count: int
    next_char: str
    que: list[tuple[int, str]] = []
    heapq.heapify(que)
    _vars: list[tuple[int, str]] = [(a, 'a'), (b, 'b'), (c, 'c')]
    for var in _vars:
        if 0 < var[0]:
            heapq.heappush(que, (var[0] * -1, var[1]))
    out: str = ''
    while que:
        count, char = heapq.heappop(que)
        count *= -1
        if (2 <= len(out)
                and out[-2] == char
                and out[-1] == char):
            if not que:
                break
            next_count, next_char = heapq.heappop(que)
            out += next_char
            if 0 > (next_count + 1):
                heapq.heappush(
                    que, (next_count + 1, next_char)
                )
            heapq.heappush(
                que, (count * -1, char)
            )
        else:
            count -= 1
            out += char
            if 0 < count:
                heapq.heappush(
                    que, (count * -1, char)
                )
    return out


# Time complexity: O(a + b + c)
# Always using every char possible from `a`, `b`, `c` => O(a + b + c).
# ---------------------------------
# Auxiliary space: O(1)


test_a: int = 1
test_b: int = 1
test_c: int = 7
test_out: str = "ccaccbcc"
assert test_out == longest_diverse_string(test_a, test_b, test_c)

test_a = 7
test_b = 1
test_c = 0
test_out = "aabaa"
assert test_out == longest_diverse_string(test_a, test_b, test_c)
