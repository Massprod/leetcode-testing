# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

def reverse(x: int) -> int:
    if -2 ** 31 < x < 2 ** 31 - 1:
        new: int = 0
        if x < 0:
            x *= - 1
            while x > 0:
                new = int(new * 10 + x % 10)
                x = x // 10
            if new > 2 ** 31 - 1 or new < -2 ** 31:
                return 0
            return new * -1
        while x > 0:
            new = int(new * 10 + x % 10)
            x = x // 10
        if new > 2 ** 31 - 1 or new < -2 ** 31:
            return 0
        return new
    return 0


print(reverse(155))
print(reverse(-155))
print(reverse(11111111111))
print(reverse(1234567890))
print(reverse(-1534236469))
print(reverse(1534236469))