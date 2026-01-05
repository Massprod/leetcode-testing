# You are given a string s consisting only of the characters '1' and '2'.
# You may delete any number of characters from s without changing the order
#  of the remaining characters.
# Return the largest possible resultant string that represents an even integer.
# If there is no such string, return the empty string "".
# --- --- --- ---
# 1 <= s.length <= 100
# s consists only of the characters '1' and '2'.


def largest_even(s: str) -> str:
    # working_solution: (100%, 100%) -> (0ms, 17.51mb)  Time: O(s) Space: O(s)
    # Largest is always already there,
    #  or we need to delete the last digit - until value iseven.
    # Because it's the lowest impact digit
    #  and we can't have `even` value when last digit is `odd`.
    while s and int(s[-1]) % 2:
        s = s[:-1]
    
    return s


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = '1112'
test_out: str = '1112'
assert test_out == largest_even(test)

test = '221'
test_out = '22'
assert test_out == largest_even(test)

test = '1'
test_out = ''
assert test_out == largest_even(test)
