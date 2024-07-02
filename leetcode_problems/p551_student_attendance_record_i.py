# You are given a string s representing an attendance record
#  for a student where each character signifies whether the student was absent, late, or present on that day.
# The record only contains the following three characters:
#   - 'A': Absent.
#   - 'L': Late.
#   - 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
#   - The student was absent ('A') for strictly fewer than 2 days total.
#   - The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.
# ----------------------------
# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.


def check_record(s: str) -> bool:
    # working_sol (96.955, 96.81%) -> (25ms, 16.32mb)  time: O(n) | space: O(1)
    absent: int = 0
    late_sequence: int = 0
    for symbol in s:
        if 'L' == symbol:
            late_sequence += 1
            if 2 < late_sequence:
                return False
            continue
        if 'A' == symbol:
            absent += 1
            if 1 < absent:
                return False
        late_sequence = 0
    return True


# Time complexity: O(n) <- n - length of the input string `s`.
# Worst case: a student is eligible for the award.
# So, we will traverse whole `s`, once => O(n).
# ----------------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on the input `s` => O(1).


test: str = "PPALLP"
test_out: bool = True
assert test_out == check_record(test)

test = "PPALLL"
test_out = False
assert test_out == check_record(test)
