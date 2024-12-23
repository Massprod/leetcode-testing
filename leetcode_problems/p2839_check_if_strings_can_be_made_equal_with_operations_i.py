# You are given two strings s1 and s2, both of length 4,
#  consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
#  - Choose any two indices i and j such that j - i = 2,
#    then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
# ------------------------
# s1.length == s2.length == 4
# s1 and s2 consist only of lowercase English letters.


def can_be_equal(s1: str, s2: str) -> bool:
    # working_sol: (100.00%, 11.29%) -> (0ms, 17.63mb)  time: O(1) | space: O(1)
    # We can either switch 0 + 2 and leave 1 + 3 as it is.
    # Or we can leave 0 + 2 and switch 1 + 3
    # Or we can switch both of them.
    # Only three options?
    # First
    if s1 == s2:
        return True
    new_s1: str = ''.join(
        [s1[2], s1[1], s1[0], s1[3]]
    )
    if new_s1 == s2:
        return True
    # Second
    new_s1 = ''.join(
        [s1[0], s1[3], s1[2], s1[1]]
    )
    if new_s1 == s2:
        return True
    # Third
    new_s1 = ''.join(
        [s1[2], s1[3], s1[0], s1[1]]
    )
    return new_s1 == s2


# Time complexity: O(1)
# Always the same # of switch operations.
# ------------------------
# Auxiliary space: O(1)


test_1: str = "abcd"
test_2: str = "cdab"
test_out: bool = True
assert test_out == can_be_equal(test_1, test_2)

test_1 = "abcd"
test_2 = "dacb"
test_out = False
assert test_out == can_be_equal(test_1, test_2)
