# You are given a string password.
# The strength of the password is calculated based on the following rules:
#  - 1 point for each distinct lowercase letter ('a' to 'z').
#  - 2 points for each distinct uppercase letter ('A' to 'Z').
#  - 3 points for each distinct digit ('0' to '9').
#  - 5 points for each distinct special character from the set "!@#$".
# Each character contributes at most once, even if it appears multiple times.
# Return an integer denoting the strength of the password.
# --- --- --- ---
# 1 <= password.length <= 10 ** 5
# password consists of lowercase and uppercase English letters, digits,
#  and special characters from "!@#$".
from string import ascii_lowercase, ascii_uppercase, digits


def password_strength(password: str) -> int:
    # working_solution: (18.07%, 98.67%) -> (52ms, 19.58mb)  Time: O(n) Space: O(1)
    specials: str ='!@#$'
    points: dict[str, dict[str, int]] = {}
    for char in ascii_lowercase:
        points[char] = {
            "score": 1,
            "used": 0,
        }
    for char in ascii_uppercase:
        points[char] = {
            "score": 2,
            "used": 0
        }
    for char in digits:
        points[char] = {
            "score": 3,
            "used": 0
        }
    for char in specials:
        points[char] = {
            "score": 5,
            "used": 0
        }
    out: int = 0
    for char in password:
        if char in points and 0 == points[char]["used"]:
            out += points[char]["score"]
            points[char]["used"] = 1
    
    return out


# Time complexity: O(n)
# n - length of the input string `password`
# --- --- --- ---
# Space complexity: O(1)


test: str = "aA1!"
test_out: int = 11
assert test_out == password_strength(test)

test = "bbB11#"
test_out = 11
assert test_out == password_strength(test)
