# You are given a non-negative floating point number rounded to two decimal places celsius,
#  that denotes the temperature in Celsius.
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
# Return the array ans. Answers within 10-5 of the actual answer will be accepted.
# Note that:
#  - Kelvin = Celsius + 273.15
#  - Fahrenheit = Celsius * 1.80 + 32.00
# -------------------
# 0 <= celsius <= 1000


def convert_temperature(celsius: float) -> list[float]:
    # working_sol (74.02%, 66.62%) -> (32ms, 16.46mb)  time: O(1) | space: O(1)
    out: list[float] = [celsius + 273.15, celsius * 1.80 + 32.00]
    return out


# Time complexity: O(1)
# -------------------
# Auxiliary space: O(1)


test: float = 36.50
test_out: list[float] = [309.65000, 97.70000]
assert test_out == convert_temperature(test)

test = 122.11
test_out = [395.26000, 251.79800]
assert test_out == convert_temperature(test)
