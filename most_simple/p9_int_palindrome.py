# Given an integer x, return true if x is a
# palindrome, and false otherwise.
# Follow up: Could you solve it without converting the integer to a string?


def is_palindrome(x: int) -> bool:
    # string sol
    # num = list(str(x))
    # if len(num) == 1:
    #     return True
    # for n in range(len(num)):
    #     if num[n] == num[-n - 1]:
    #         continue
    #     else:
    #         return False
    # return True
    # int sol?
    if x < 0 or x % 10 == 0 and x != 0:  # can't be negative and only 0 can be palindrome
        return False
    new: int = 0
    while x > new:
        new = int(new * 10 + x % 10)  # appending last digit of x to a new and adding multiplied prev modulus
        x = x // 10  # removing last digit from x
    return x == new or x == new // 10  # if length is odd remove 1 extra digit from new, cuz x < new after loop


print(is_palindrome(121121121))
print(is_palindrome(-202202202))
print(is_palindrome(-1))
print(is_palindrome(202202202))
print(is_palindrome(121))
print(is_palindrome(150))