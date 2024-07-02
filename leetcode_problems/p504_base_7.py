# Given an integer num, return a string of its base 7 representation.
# ---------------------
# -10 ** 7 <= num <= 10 ** 7


def convert_to_base_7(num: int) -> str:
    # working_sol (99.39%, 82.68%) -> (21ms, 16.48mb)  time: O(num) | space: O(num)
    if 0 == num:
        return '0'
    base_7: str = ''
    negative: bool = True if num < 0 else False
    value: int = abs(num)
    while value:
        base_7 += str(value % 7)
        value = value // 7
    base_7 = base_7[::-1]
    return '-' + base_7 if negative else base_7


# Time complexity O(num)
# Always depleting `abs(num)` to 0 => O(num).
# Auxiliary space: O(num)
# Higher `abs(num)` => longer string `base_7` => O(num).


test: int = 100
test_out: str = '202'
assert test_out == convert_to_base_7(test)

test = -7
test_out = '-10'
assert test_out == convert_to_base_7(test)
