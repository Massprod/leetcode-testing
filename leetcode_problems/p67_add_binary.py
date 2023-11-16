# Given two binary strings a and b, return their sum as a binary string.
# ----------------------
# 1 <= a.length, b.length <= 10 ** 4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


def add_binary(a: str, b: str) -> str:
    # working_sol (82.02%, 48.75%) -> (37ms, 16.4mb)  time: O(max(len(a), len(b)))  | space: O(a + b)
    # Bin sum rules:
    # 1 + 1 -> (0 or 1 if carry) + always carry == 1
    # 1 + 0 -> 1 or (0 if carry + carry == 1)
    # 0 + 0 -> 0 or (1 if carry)
    # Iterative approach:
    out: str = ''
    # They can be different size, and we're doing right -> left traverse.
    higher: str = max(a, b, key=lambda x: len(x))
    lower: str = min(a, b, key=lambda x: len(x))
    if higher == lower:
        higher = a
        lower = b
    carry: int = 0
    index: int = -1
    # Last index we can use in smaller string.
    last_index: int = -len(lower) - 1
    while index != last_index:
        if lower[index] == '1' and higher[index] == '1':
            if carry:
                out += '1'
            else:
                out += '0'
            carry = 1
        elif (lower[index] == '0' and higher[index] == '1') or (lower[index] == '1' and higher[index] == '0'):
            if carry:
                out += '0'
                carry = 1
            else:
                out += '1'
                carry = 0
        elif lower[index] == '0' and higher[index] == '0':
            if carry:
                out += '1'
                carry = 0
            else:
                out += '0'
        index -= 1
    # Last index we can use in longer string.
    last_index = -len(higher) - 1
    while index != last_index:
        if higher[index] == '1':
            if carry:
                out += '0'
                carry = 1
            else:
                out += '1'
                carry = 0
        elif higher[index] == '0':
            if carry:
                out += '1'
                carry = 0
            else:
                out += '0'
        index -= 1
    if carry:
        out += '1'
    # Reverse for correct order == left -> right.
    return out[::-1]


# Time complexity: O(max(len(a), len(b))) -> essentially traversing both string and using their indexes only once.
# Space complexity: O(a + b) -> creating copy of both input strings + 'out' is max(len(a), len(b)) =>
#                               => O(2a + b) or O(a + 2b) == O(a + b) without constant.
# --------------------------------
# Binary rules for add:
#       0 + 1 = 1
#       1 + 0 = 1
#       0 + 0 = 0
#       1 + 1 = 0 -> 1 carry


test_a: str = "11"
test_b: str = "1"
test_out: str = "100"
assert test_out == add_binary(test_a, test_b)

test_a = "1010"
test_b = "1011"
test_out = "10101"
assert test_out == add_binary(test_a, test_b)

test_a = "110111"
test_b = "1011000"
test_out = "10001111"
assert test_out == add_binary(test_a, test_b)

test_a = "11000000111001"
test_b = "1101010000110001"
test_out = "10000010001101010"
assert test_out == add_binary(test_a, test_b)
