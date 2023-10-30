# You are given an integer array arr.
# Sort the integers in the array in ascending order by the number of 1's in their binary representation
#  and in case of two or more integers have the same number of 1's you have to sort them
#  in ascending order.
# Return the array after sorting it.
# -------------------------
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10 ** 4


def sort_by_bits(arr: list[int]) -> list[int]:
    # working_sol (53.66%, 94.41%) -> (70ms, 16.23mb)  time: O(n * log n) | space: O(n)
    bits: dict[int, list[int]] = {}
    for num in arr:
        cur_bits: int = 0
        cur_num: int = num
        while cur_num:
            if cur_num & 1:
                cur_bits += 1
            cur_num >>= 1
        if cur_bits in bits:
            bits[cur_bits].append(num)
        else:
            bits[cur_bits] = [num]
    out: list[int] = []
    for x in range(33):
        if x in bits:
            out += sorted(bits[x])
    return out


# Time complexity: O(n * log n) -> we can say that count is constant, almost instant + we have low bound of 10 ** 4
# n - len of input array 'arr'^^|  then it's just O(n) to get all bits counted. Extra sorting which essentially
#                                  uses every element of input 'arr' and sort them partially => O(n * log n).
#              OR: O(k * (m * log m) -> 'k' - number of unique counted bits, 'm' - number of values with 'k' bits.
#                  But, no idea how we can find this values without knowing the array values.
#                  So, O(n * log n) should be more correct.
# Auxiliary space: O(n) -> dictionary 'bits' with slices of original array, which essentially have same size => O(n) ->
#                          -> extra list 'out' with same size as original array => O(2n).


test: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test_out: list[int] = [0, 1, 2, 4, 8, 3, 5, 6, 7]
assert test_out == sort_by_bits(test)

test = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
test_out = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
assert test_out == sort_by_bits(test)

test = [num for num in range(0, 500)]
print(test)
