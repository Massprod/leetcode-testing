# You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
#  indicates the birth and death years of the ith person.
# The population of some year x is the number of people alive during that year.
# The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
# Note that the person is not counted in the year that they die.
# Return the earliest year with the maximum population.
# ------------------------
# 1 <= logs.length <= 100
# 1950 <= birthi < deathi <= 2050


def maximum_population(logs: list[list[int]]) -> int:
    # working_sol (91.63%, 51.15%) -> (37ms, 16.52mb)  time: O(n) | space: O(1)
    # [all possible years shifted to 0 -> 100]
    #  ^^ otherwise we need to create an array with empty 1500 indexes.
    all_years: list[int] = [0 for _ in range(101)]
    for start, end in logs:
        all_years[start - 1950] += 1  # born == increase
        all_years[end - 1950] -= 1  # died == decrease
    out: int = 1950
    max_population: int = all_years[0]
    # We start from 1950 and collect all population changes from every Year.
    for index in range(1, len(all_years)):
        all_years[index] += all_years[index - 1]
        if all_years[index] > max_population:
            max_population = all_years[index]
            out = index + 1950  # returned shifted value
    return out


# Time complexity: O(n) <- n - length of the input array `logs`.
# Always traversing whole input array `logs`, once => O(n).
# ------------------------
# Auxiliary space: O(1).
# `all_years` <- always of the same size == `101` => O(1).


test: list[list[int]] = [[1993, 1999], [2000, 2010]]
test_out: int = 1993
assert test_out == maximum_population(test)

test = [[1950, 1961], [1960, 1971], [1970, 1981]]
test_out = 1960
assert test_out == maximum_population(test)
