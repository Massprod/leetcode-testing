# You are given a string s of length 10 consisting of digits.
# The dial contains the digits 0 through 9 in order and is circular,
#  so 0 and 9 are adjacent. The pointer initially points to 0.
# To dial each digit of s in order, rotate the pointer until it points to that digit.
# Each rotation moves the pointer to an adjacent digit, and you may rotate
#  in either direction.
# Dialing a digit that the pointer already points to requires no rotations.
# Return the minimum total number of rotations needed to dial every digit of s.
# --- --- --- ---
# s.length == 10
# s consists only of digits '0' to '9'


def min_rotations(s: str) -> int:
    # working_solution: (100%, 19.87%) -> (0ms, 19.33mb)  Time: O(s) Space: O(1)
    out: int = 0
    current: int = 0
    for index in range(len(s)):
        target: int = int(s[index])
        # Distance we need to cover between them
        diff: int = abs(current - target)
        # 10 - diff <- counterpart, if we move in the opposite direction
        out += min(diff, 10 - diff)
        current = target
    
    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(1)


test: str = '0192837465'
test_out: int = 25
assert test_out == min_rotations(test)

test = '1200210200'
test_out = 12
assert test_out == min_rotations(test)
