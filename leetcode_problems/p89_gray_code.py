# An n-bit gray code sequence is a sequence of 2n integers where:
#   Every integer is in the inclusive range [0, 2n - 1],
#   The first integer is 0,
#   An integer appears no more than once in the sequence,
#   The binary representation of every pair of adjacent integers differs by exactly one bit, and
#   The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.
# 1 <= n <= 16


def gray_code(n: int) -> list[int]:
    # working_sol (20.26%, 11.24%) -> (144ms, 24.9mb)  time: O(2 ** n) | space: O(2 ** n)
    gray: list[str | int] = ["0", "1"]
    count: int = 2
    if n == 1:
        for g in range(len(gray)):
            gray[g] = int(gray[g], 2)
        return gray
    while count <= n:
        last_index: int = len(gray) - 1
        for x in range(last_index, -1, -1):
            new: str = "0" + gray[x]
            reverse: str = "1" + gray[x]
            gray[x] = new
            gray.append(reverse)
        count += 1
    for y in range(len(gray)):
        gray[y] = int(gray[y], 2)
    return gray

# Time complexity: O(2 ** n) -> we're creating n-bit Gray code from basic n=1 ->
#                               -> by repeating loop for every index in gray n times, every while_loop instance
#                                  size of gray_list grows by x2 (gray_size + gray_size)
#                               -> base size of 2 and while_loop for n times ->
#                               -> looping through 2 times for 1, loop 2 * 2 times for 2, loop 4 * 2 for 3 .etc =>
#                               => O(2 ** n)
# Space complexity: O(2 ** n) -> for every loop we're expending our base gray_list of 2 size to (2 ** n) size.

# -----------------
# Had no idea about Gray_code before, so I made a function by wiki_description.
# Failed to convert bits to correct int of base 2.
# Don't know why this is medium task, but I didn't see restrictions on using int().
# Because if we're restricted to do this, I would need to make conversion by myself and it would be harder.
# Not going to make it tho, no limit == not problem.
# -----------------
# int(bits_value, n) -> bit to int convert with base of n


test1 = 2
test1_out = [0, 1, 3, 2]
assert gray_code(test1) == test1_out
print(gray_code(test1))

test2 = 1
test2_out = [0, 1]
assert gray_code(test2) == test2_out
print(gray_code(test2))

# test3 - failed -> I was thinking that n is a base, but we just need ints with base of 2
test3 = 3
test3_out = [0, 1, 3, 2, 6, 7, 5, 4]
assert gray_code(test3) == test3_out
print(gray_code(test3))
