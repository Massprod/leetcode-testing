# Given two binary strings a and b, return their sum as a binary string.

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def add_binary(a: str, b: str) -> str:
    length_a: int = len(a)
    length_b: int = len(b)
    max_length: int = -1
    min_length: int = -1
    highest: str = ""
    lowest: str = ""
    if length_a > length_b:
        max_length = length_a * -1
        min_length = length_b * -1
        highest = a
        lowest = b
    if length_a < length_b:
        max_length = length_b * -1
        min_length = length_a * -1
        highest = b
        lowest = a
    if length_a == length_b:
        max_length = min_length = length_a * -1
        highest, lowest = a, b
    max_x: int = min_length
    max_y: int = max_length
    x: int = -1
    y: int = -1
    carry: int = 0
    result: list[int | str] = []
    index_sum: int = 0
    while y >= max_y:
        if x >= max_x:
            index_sum = int(lowest[x]) + int(highest[y])
        if x < max_x:
            index_sum = int(highest[y])
        if index_sum == 0 and carry == 0:
            result.insert(0, 0)
            carry = 0
        if index_sum == 1 and carry == 0:
            result.insert(0, 1)
            carry = 0
        if index_sum == 0 and carry == 1:
            result.insert(0, 1)
            carry = 0
        if index_sum == 1 and carry == 1:
            result.insert(0, 0)
            carry = 1
        if index_sum == 2 and carry == 1:
            result.insert(0, 1)
            carry = 1
        if index_sum == 2 and carry == 0:
            result.insert(0, 0)
            carry = 1
        if x >= max_x:
            x -= 1
        if y >= max_y:
            y -= 1
    if carry != 0:
        result.insert(0, 1)
    for x in range(len(result)):
        result[x] = str(result[x])
    return "".join(result)

# Binary rules for add:
#       0 + 1 = 1
#       1 + 0 = 1
#       0 + 0 = 0
#       1 + 1 = 0 -> 1 carry


test1_a = "11"
test1_b = "1"
test1_out = "100"
print(add_binary(test1_a, test1_b))
assert test1_out == add_binary(test1_a, test1_b)

test2_a = "1010"
test2_b = "1011"
test2_out = "10101"
print(add_binary(test2_a, test2_b))
assert test2_out == add_binary(test2_a, test2_b)

test3_a = "110111"
test3_b = "1011000"
test3_out = "10001111"
print(add_binary(test3_a, test3_b))
assert test3_out == add_binary(test3_a, test3_b)
