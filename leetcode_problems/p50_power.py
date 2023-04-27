# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

def my_power(x: float, n: int) -> float:
    if n == 0:
        return 1
    base = x
    for _ in range(abs(n) - 1):
        base *= x
    if n < 0:
        return 1 / base
    return base


#   x ** n == x * ((x ** 2) ** ((n - 1) / 2 ))  <- if n is odd
#   x ** n == (x ** 2) ** n / 2   <- if n is even
# Why did I expect this as the simplest task? W.e didn't know that ^

# Brain-lag? Why do I even use sign for?
# Unique moment with x ** 0 == 1 <- always
# Hmm. We're returning float, but should we limit digits after decimal_point or not?
# Cuz if we do than it's not a float. but in tests_out they give us 2.00000 with 5 digits after decimal_point.


test1 = 2.00000
test1_pow = 10
test1_out = 1024.00000
print(my_power(test1, test1_pow))

test2 = 2.10000
test2_pow = 3
test2_out = 9.26100
print(my_power(test2, test2_pow))

test3 = 2.00000
test3_pow = -2
test3_out = 0.25000
print(my_power(test3, test3_pow))

test4 = 0.00001
test4_pow = 2147483647
print(my_power(test4, test4_pow))
