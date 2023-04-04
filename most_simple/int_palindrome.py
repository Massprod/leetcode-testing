# Given an integer x, return true if x is a
# palindrome, and false otherwise.


def is_palindrome(x: int) -> bool:
    num = list(str(x))
    if len(num) == 1:
        return True
    for n in range(len(num)):
        if num[n] == num[-n - 1]:
            continue
        else:
            return False
    return True


print(is_palindrome(121))