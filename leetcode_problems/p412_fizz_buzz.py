# Given an integer n, return a string array answer (1-indexed) where:
#  - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#  - answer[i] == "Fizz" if i is divisible by 3.
#  - answer[i] == "Buzz" if i is divisible by 5.
#  - answer[i] == i (as a string) if none of the above conditions are true.
# ------------------
# 1 <= n <= 10 ** 4


def fizz_buzz(n: int) -> list[str]:
    # working_sol (92.32%, 51.92%) -> (38ms, 17.66mb)  time: O(n) | space: O(n)
    out: list[str] = []
    for val in range(1, n + 1):
        by_5: int = val % 5
        by_3: int = val % 3
        if 0 == by_5 and 0 == by_3:
            out.append('FizzBuzz')
        elif 0 == by_3:
            out.append('Fizz')
        elif 0 == by_5:
            out.append('Buzz')
        else:
            out.append(str(val))
    return out


# Time complexity: O(n).
# We're always looping through `n` values => O(n).
# ------------------
# Auxiliary space: O(n).
# And every `val` we use we add into `out` => O(n).


test: int = 3
test_out: list[str] = ["1", "2", "Fizz"]
assert test_out == fizz_buzz(test)

test = 5
test_out = ["1", "2", "Fizz", "4", "Buzz"]
assert test_out == fizz_buzz(test)

test = 15
test_out = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
assert test_out == fizz_buzz(test)
