# A binary watch has 4 LEDs on the top to represent the hours (0-11),
#  and 6 LEDs on the bottom to represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# Given an integer turnedOn which represents the number of LEDs that are currently on
#  (ignoring the PM), return all possible times the watch could represent.
# You may return the answer in any order.
# The hour must not contain a leading zero.
# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.
# For example, "10:2" is not valid. It should be "10:02".
# --- --- --- ---
# 0 <= turnedOn <= 10


def read_binary_watch(turned_on: int) -> list[str]:
    # working_solution: (100%, 60.29%) -> (0ms, 19.38mb)  Time: O(1) Space: O(1)
    # We can only have 10 `lights` turned on.
    # Represent them in the binary and check all of the combinations.
    out: list[str] = []
    # First 6 bits represent minutes
    # Other bits represent hours + pm/am switch
    minutes_mask: int = int('111111', 2)
    for val in range(2 ** 10):
        # Remove the minutes.
        hours: int = val >> 6
        minutes: int = val & minutes_mask
        # Maximum hours we can have is `11` => `am/pm`.
        # Maximum minutes are `59`.
        # And leds we need to have is `turned_on`.
        if (
            11 < hours
            or 59 < minutes
            or turned_on != bin(val).count('1')
        ):
            continue
        time_string: str = f'{hours}:{minutes:02d}'
        out.append(time_string)

    return out


# Time complexity: O(1)
# --- --- --- ---
# Space complexity: O(1)


test: int = 1
test_out: list[str] = [
    "0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"
]
assert test_out == read_binary_watch(test)

test = 9
test_out = []
assert test_out == read_binary_watch(test)
