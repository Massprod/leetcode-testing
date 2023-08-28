# You are given an array items, where each items[i] = [typei, colori, namei]
#  describes the type, color, and name of the ith item.
# You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
#   ruleKey == "type" and ruleValue == typei.
#   ruleKey == "color" and ruleValue == colori.
#   ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.
# --------------------
# 1 <= items.length <= 10 ** 4
# 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
# ruleKey is equal to either "type", "color", or "name".
# All strings consist only of lowercase letters.


def count_matches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    # working_sol (87.95%, 99.18%) -> (251ms, 22.39mb)  time: O(n) | space: O(1)
    check_ind: int = 0
    if ruleKey == 'color':
        check_ind = 1
    elif ruleKey == 'name':
        check_ind = 2
    count: int = 0
    for item in items:
        if item[check_ind] == ruleValue:
            count += 1
    return count


# Time complexity: O(n) -> traversing whole input_array and check set index => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra INTs used, none of them depends on input => O(1).


test: list[list[str]] = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
test_key: str = "color"
test_val: str = "silver"
test_out: int = 1
assert test_out == count_matches(test, test_key, test_val)

test = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
test_key = "type"
test_val = "phone"
test_out = 2
assert test_out == count_matches(test, test_key, test_val)
