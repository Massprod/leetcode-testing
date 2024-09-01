# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k,
#  return the array-form of the integer num + k.
# -----------------------
# 1 <= num.length <= 10 ** 4
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 10 ** 4


def add_to_array_form(num: list[int], k: int) -> list[int]:
    # working_sol (97.35%, 30.31%) -> (178ms, 17.79mb)  time: O(num + k) | space: O(k)
    new_val: int
    carry: int
    # We just need to include every digit from `k`.
    if 0 == num[0]:
        out: list[int] = []
        while k:
            out.append(k % 10)
            k //= 10
        return out[::-1]
    index: int = len(num) - 1
    carry: int = 0
    while k:
        # Standard sum with carry over value.
        if 0 <= index:
            new_val = num[index] + (k % 10) + carry
            if 9 < new_val:
                carry = 1
                num[index] = new_val % 10
            else:
                carry = 0
                num[index] = new_val
        # [1, 0], k = 999 <- we need to include extra values we get
        else:
            new_val = (k % 10) + carry
            if 9 < new_val:
                carry = 1
                num.insert(0, new_val % 10)
            else:
                carry = 0
                num.insert(0, new_val)
        index -= 1
        k //= 10
    # [9,9,9,9,9,9,9], k = 1 <- we need to use every carry value we get
    while carry:
        if 0 > index:
            break
        new_val = num[index] + carry
        if 9 < new_val:
            carry = 1
            num[index] = new_val % 10
        else:
            carry = 0
            num[index] = new_val
        index -= 1
    if carry:
        return [carry] + num
    return num


# Time complexity: O(num + k)
# Always using every index of `num` and every digit from `k` => O(num + k).
# -----------------------
# Auxiliary space: O(k)
# In the worst case `num` = [0], so we will use `out` and store every digit from `k` in it => O(k).
# Otherwise we're reusing `num` and at max add 1 value to it.


test: list[int] = [1, 2, 0, 0]
test_k: int = 34
test_out: list[int] = [1, 2, 3, 4]
assert test_out == add_to_array_form(test, test_k)

test = [2, 7, 4]
test_k = 181
test_out = [4, 5, 5]
assert test_out == add_to_array_form(test, test_k)

test = [2, 1, 5]
test_k = 806
test_out = [1, 0, 2, 1]
assert test_out == add_to_array_form(test, test_k)

test = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
test_k = 1
test_out = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert test_out == add_to_array_form(test, test_k)

test = [1, 0]
test_k = 899
test_out = [9, 0, 9]
assert test_out == add_to_array_form(test, test_k)
