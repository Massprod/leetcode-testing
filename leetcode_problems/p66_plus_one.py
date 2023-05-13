# You are given a large integer represented as an integer array digits,
# where each digit[i] is the ith digit of the integer.
# The digits are ordered from most significant to the least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# 1 <= digits.length <= 100  ,  0 <= digits[i] <= 9  ,  digits does not contain any leading 0's.


def plus_one(digits: list[int]) -> list[int]:
    # working_sol (7.48%, 14.55%) -> (53ms, 16.3mb)  time: O(n)  | space: O(n)
    num: str = ""
    for _ in digits:
        num += str(_)
    integer: int = int(num)
    integer += 1
    num = str(integer)
    incremented: list[int] = []
    for _ in num:
        incremented.append(int(_))
    return incremented

# Time complexity: O(n) -> lopping once through whole input_list to create num => O(n) ->
#                          -> looping through created string(num) of input_list size => O(n) -> O(2n) => O(n)
#                  Ω(n) = O(n) = Θ(n) -> always looping whole input_list, no matter what.
# Space complexity: O(n) -> creating extra string of input_list size => O(n) ->
#                           -> creating extra integer and string of this integer = size of input_list => O(n) ->
#                           -> creating extra list of input_list size => O(n) -> O(3n) => O(n)
# -----------------------------
# Most basic way is: make str from list -> make int from string -> increment by 1 -> make str from int -> list string
# But it's a lot of transformations and if there's time_limit, then I will rebuild but try this one.


test1 = [1, 2, 3]
test1_out = [1, 2, 4]
print(plus_one(test1))
for _ in range(len(test1_out)):
    assert test1_out[_] == plus_one(test1)[_]

test2 = [4, 3, 2, 1]
test2_out = [4, 3, 2, 2]
print(plus_one(test2))
for _ in range(len(test2_out)):
    assert test2_out[_] == plus_one(test2)[_]

test3 = [9]
test3_out = [1, 0]
print(plus_one(test3))
for _ in range(len(test3_out)):
    assert test3_out[_] == plus_one(test3)[_]
