# Given a string s, rearrange the characters of s so that
#  any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.
# -------------------
# 1 <= s.length <= 500
# s consists of lowercase English letters.
import heapq
from string import ascii_lowercase
from random import choice


def reorganize_string(s: str) -> str:
    # working_sol (90.18%, 78.11%) -> (37ms, 16.3mb)  time: O(n * log n) | space: O(n)
    occurrences: dict[str: int] = {}
    # Count every symbol and it's occurrences.
    for sym in s:
        if sym in occurrences:
            occurrences[sym] += 1
            continue
        occurrences[sym] = 1
    heap_occur: heapq = []
    heapq.heapify(heap_occur)
    # key -> symbol|letter.
    # value -> times it occur.
    # Reverse and save, so we can sort correctly.
    # We need to use mostPresented symbols first,
    #  otherwise only duplicates can be left.
    # And we could use lessPresented symbols as breakpoints between them.
    # So we need to place symbols from
    #  mostPresented -> lessPresented => maxHeap.
    for key, value in occurrences.items():
        heapq.heappush(heap_occur, (-value, key))
    reorganized: str = ''
    cur_symbol: tuple[int, str] = heapq.heappop(heap_occur)
    # If there's only 1 symbol present ->
    if len(heap_occur) == 0:
        # -> and it has only 1 occurrence.
        if cur_symbol[0] == -1:
            return cur_symbol[1]
        # Otherwise it has duplicates which cant be used correctly.
        return ''
    reorganized += cur_symbol[1]
    occur_left: int = cur_symbol[0] + 1
    # Ignore exhausted symbols, can't be used anymore.
    if occur_left != 0:
        heapq.heappush(heap_occur, (occur_left, cur_symbol[1]))
    # We need to exhaust every symbol possible.
    # From mostPresented -> lessPresented.
    while len(heap_occur) > 1:
        cur_symbol: tuple[int, str] = heapq.heappop(heap_occur)
        # Multiple symbols can have same Occurrence time.
        left_symbols: list[tuple[int, str]] = []
        # We need to filter them ->
        while cur_symbol[1] == reorganized[-1]:
            left_symbols.append(cur_symbol)
            cur_symbol = heapq.heappop(heap_occur)
        # -> and return them, after finding different.
        for _ in left_symbols:
            heapq.heappush(heap_occur, _)
        reorganized += cur_symbol[1]
        occur_left = cur_symbol[0] + 1
        if occur_left != 0:
            heapq.heappush(heap_occur, (occur_left, cur_symbol[1]))
    # Same approach for 1 last symbol, as before.
    cur_symbol = heapq.heappop(heap_occur)
    if cur_symbol[0] == -1:
        return reorganized + cur_symbol[1]
    return ''


# Time complexity: O(n * log n) -> traverse input_string once, to count and save every symbol => O(n) ->
# n - len of input_string^^| traverse created dictionary and store every pair (occurrences, symbol) into a heapq =>
#                           => O(n * log n) -> for every pair we're going to either just pop + use it and push again =>
#                           => O(log n + log n) -> or do this twice to find different symbol to use ->
#                           -> so it's still should be correct to say => O(n * log n).
# Auxiliary space: O(n) -> for every symbol we're creating a pair of (occurrences, symbol) and store them into
#                          dictionary and heapq as well, dunno how to calc correctly size diff ->
#                          -> like we're using not just str, but str + int for every index => O(2n)?
#                          Well it's Linear anyway, but how to say it correctly?
# -------------------
# ! Return any possible rearrangement ! <- So basically we can do w.e we want until we're placing
# ANYsymbol + notPREVsymbol until we have something to place after ANYsymbol.
# Store every symbol we have and it's occurrences and reuse it?
# Like we can use 3'a', 3'b', 3'c' -> then we can just place any of them first and choose different next,
#  place it and repeat. Until there's something different left to place, and if there's only same symbols?
# Then we can't use it -> so it's impossible to rearrange. Should be correct.
# But while it's easy to store Occurrences, how to choose symbol from this Max Occurrences fast?
# Can we store (occurrences, value) in a heap? Never done this, but otherwise I would need to
#  traverse dictionary with keys == Occurrences and values == Symbol, for every symbol used.
# Which is slow AF, with Heap it's faster, but does it work with tuple[0] indexes?
# ! https://docs.python.org/2/library/heapq.html#basic-examples
#  Heap elements can be tuples. And they're sorted by first index == tuple[0] !
# OK. Then it's easy to maintain which symbol to use. Let's try.
# OK. We can't do this in ascending order, cuz I will use lowest occurrences first and then
#  only duplicates can be left. So we need to use Most presented symbols first.
# MaxHeap instead of MinHeap should be enough.


test: str = 'aab'
test_out: str = 'aba'
assert test_out == reorganize_string(test)

test = 'aaab'
test_out = ''
assert test_out == reorganize_string(test)

test = ''
for _ in range(500):
    test += choice(ascii_lowercase)
# print(test)
