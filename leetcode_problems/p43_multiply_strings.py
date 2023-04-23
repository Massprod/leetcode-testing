# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# ! num1 and num2 consist of digits only.
#   Both num1 and num2 do not contain any leading zero, except the number 0 itself. !
#
# int(num) -> suppose it's direct
# first way comes up to me, is to use ASCII. ord(num) -> built in function, but maybe not allowed?


def multiply_ascii(num1: str, num2: str) -> str:
    # working_sol (84.1%, 57.90%) -> (32ms, 13.8mb) time: O(n) | space: O(n)
    to_check = {
        "0": 48,
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
    }
    first = []
    for _ in num1:
        first.append(to_check[_] - 48)
    second = []
    for _ in num2:
        second.append(to_check[_] - 48)
    first_int = 0
    for x in range(len(first)):
        first_int += first[x] * 10 ** ((len(first) - 1) - x)
    second_int = 0
    for y in range(len(second)):
        second_int += second[y] * 10 ** ((len(second) - 1) - y)
    product = first_int * second_int
    return str(product)

# Time complexity: O(n) -> linear scaling with len() of input.
# Space complexity: O(n) -> creating 2 lists of the same size as input.

# We're not allowed to ! convert the inputs to integer directly !
# But what about product to str? Try to rebuild without using str()


def multiply_ascii_no_str(num1: str, num2: str) -> str:
    # working_sol (73.95%, 95.23%) -> (34ms, 13.8mb)  time: O(n) | space: O(n)
    to_check = {
        "0": 48,
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
    }
    first = []
    for _ in num1:
        first.append(to_check[_] - 48)
    second = []
    for _ in num2:
        second.append(to_check[_] - 48)
    first_int = 0
    for x in range(len(first)):
        first_int += first[x] * 10 ** ((len(first) - 1) - x)
    second_int = 0
    for y in range(len(second)):
        second_int += second[y] * 10 ** ((len(second) - 1) - y)
    product = first_int * second_int
    if product == 0:
        return chr(48 + product % 10)
    product_list = []
    while product:
        product_list.append(chr(48 + product % 10))
        product = product // 10
    product_str = "".join(reversed(product_list))
    return product_str

# Time complexity: O(n) -> linear scaling with len() of input.
# Space complexity: O(n) -> creating 3 lists of the same size as input.
# Guess, now it's not using anything: no ord(), no str() -> somewhat reproducing them, actually.

# Every time, I submit same solution it's 54%(39ms) -> 84%(32ms)  memory: 18.15%(14mb) -> 57.90%(13.8mb) | changes..


test1_1 = "2"
test1_2 = "3"
test1_out = "6"
print(multiply_ascii(test1_1, test1_2))
print(multiply_ascii_no_str(test1_1, test1_2))

test2_1 = "123"
test2_2 = "456"
test2_out = "56088"
print(multiply_ascii(test2_1, test2_2))
print(multiply_ascii_no_str(test2_1, test2_2))

# Failed with product == 0. It didn't go into a loop -> unique option, we can just return chr(48) for this.
test3_1 = "0"
test3_2 = "0"
test3_out = "0"
print(multiply_ascii(test3_1, test3_2))
print(multiply_ascii_no_str(test3_1, test3_2))
