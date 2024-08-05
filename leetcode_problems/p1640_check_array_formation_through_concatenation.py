# You are given an array of distinct integers arr and an array of integer arrays pieces,\
#  where the integers in pieces are distinct.
# Your goal is to form arr by concatenating the arrays in pieces in any order.
# However, you are not allowed to reorder the integers in each array pieces[i].
# Return true if it is possible to form the array arr from pieces.
# Otherwise, return false.
# --------------------
# 1 <= pieces.length <= arr.length <= 100
# sum(pieces[i].length) == arr.length
# 1 <= pieces[i].length <= arr.length
# 1 <= arr[i], pieces[i][j] <= 100
# The integers in arr are distinct.
# The integers in pieces are distinct
# (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).


def can_form_array(arr: list[int], pieces: list[list[int]]) -> bool:
    # working_sol (61.08%, 94.07%) -> (43ms, 16.38mb)  time: O(n) | space: O(n)
    # { opener: [whole_sequence] }
    first_occur: dict[int, list[int]] = {}
    for piece in pieces:
        opener: int = piece[0]
        sequence: list[int] = piece[1:]
        first_occur[opener] = sequence
    index: int = 0
    while index < len(arr):
        cur_val: int = arr[index]
        # We can either have full sequence used, and we have only unique integers in `pieces`.
        if cur_val in first_occur:
            index += 1
            # We can skip values check if we can't use a whole sequence => False
            if len(arr) - index < len(first_occur[cur_val]):
                return False
            for integer in first_occur[cur_val]:
                # Or we can't use some particular value in the sequence => False.
                if integer != arr[index]:
                    return False
                index += 1
        # If we can't even start using some sequence, then we can't use any number in it => False.
        else:
            return False
    return True


# Time complexity: O(n) <- n - length of the input array `arr`.
# We have constraints that there's equal number of values in `arr` and flattened `pieces`.
# So, if we can use every sequence and values in it.
# We're going to traverse whole `arr`, once => O(n).
# Extra, we're building `first_occur` with the same size as `arr`|`flatPieces` => O(2 * n).
# --------------------
# Auxiliary space: O(n)
# Every value from a flattened `pieces` is stored in `first_occur` => O(n).


test: list[int] = [15, 88]
test_pieces: list[list[int]] = [[88], [15]]
test_out: bool = True
assert test_out == can_form_array(test, test_pieces)

test = [49, 18, 16]
test_pieces = [[16, 18, 49]]
test_out = False
assert test_out == can_form_array(test, test_pieces)

test = [91, 4, 64, 78]
test_pieces = [[78], [4, 64], [91]]
test_out = True
assert test_out == can_form_array(test, test_pieces)
