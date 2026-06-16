# You are given a string s consisting of lowercase English letters
#  and the special characters: *, #, and %.
# Build a new string result by processing s according to the following rules from left to right:
#  - If the letter is a lowercase English letter append it to result.
#  - A '*' removes the last character from result, if it exists.
#  - A '#' duplicates the current result and appends it to itself.
#  - A '%' reverses the current result.
# Return the final string result after processing all characters in s.
# --- --- --- ---
# 1 <= s.length <= 20
# s consists of only lowercase English letters and special characters *, #, and %.
from string import ascii_lowercase


def process_str(s: str) -> str:
    # working_solution: (13.82%, 12.50%) -> (50ms, 30.01mb)  Time: O(s) Space: O(s)
    out: list[str] = []

    def _append(target: list[str], char: str) -> None:
        target.append(char)

    def _remove(target: list[str], char: str) -> None:
        if not target:
            return
        target.pop()

    def _duplicate(target: list[str], char: str) -> None:
        target.extend(target[:])

    def _reverse(target: list[str], char: str) -> None:
        target[:] = target[::-1]

    calls: dict = {char: _append for char in ascii_lowercase}
    calls['*'] = _remove
    calls['#'] = _duplicate
    calls['%'] = _reverse
    for char in s:
        action = calls.get(char, None)
        if not action:
            continue
        action(out, char)
    
    return ''.join(out)


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "a#b%*"
test_out: str = "ba"
assert test_out == process_str(test)

test = "z*#"
test_out = ""
assert test_out == process_str(test)
