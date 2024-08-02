# You are given a 0-indexed array of strings details.
# Each element of details provides information about a given passenger
#  compressed into a string of length 15.
# The system is such that:
#  - The first ten characters consist of the phone number of passengers.
#  - The next character denotes the gender of the person.
#  - The following two characters are used to indicate the age of the person.
#  - The last two characters determine the seat allotted to that person.
# Return the number of passengers who are strictly more than 60 years old.
# ------------------------
# 1 <= details.length <= 100
# details[i].length == 15
# details[i] consists of digits from '0' to '9'.
# details[i][10] is either 'M' or 'F' or 'O'.
# The phone numbers and seat numbers of the passengers are distinct.


def count_seniors(details: list[str]) -> int:
    # working_sol (97.50%, 32.17%) -> (35ms, 16.57mb)  time: O(n) | space: O(n)
    out: int = 0
    for citizen_d in details:
        if 60 < int(citizen_d[-4:-2]):
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `details`.
# Every element in `details` has the same size.
# We traverse every element for slicing it => O(n).
# ------------------------
# Auxiliary space: O(1)
# Slice creates a new string which is converted to the INT, and it's always of the same size => O(1).


test: list[str] = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
test_out: int = 2
assert test_out == count_seniors(test)

test = ["1313579440F2036", "2921522980M5644"]
test_out = 0
assert test_out == count_seniors(test)
