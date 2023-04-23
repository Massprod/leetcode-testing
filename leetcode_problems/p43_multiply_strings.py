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
    print("% s" % product)
    return str(product)


test1_1 = "2"
test1_2 = "3"
test1_out = "6"
print(multiply_ascii(test1_1, test1_2))

test2_1 = "123"
test2_2 = "456"
test2_out = "56088"
print(multiply_ascii(test2_1, test2_2))
