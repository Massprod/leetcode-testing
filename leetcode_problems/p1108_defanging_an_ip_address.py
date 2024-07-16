# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# ------------------------
# The given address is a valid IPv4 address.


def defang_ip_addr(address: str) -> str:
    # working_sol (95.72%, 46.08%) -> (26ms, 16.48mb)  time: O(n) | space: O(n)
    return address.replace('.', '[.]')
    # chars: list[str] = []
    # for char in address:
    #     if '.' != char:
    #         chars.append(char)
    #     else:
    #         chars.append('[.]')
    # return ''.join(chars)


# Time complexity: O(n) <- n - length of the input string `address`.
# Always traversing the whole input string `address`, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# Even if every char in `address` is going to be `.` we're still adding constant elements => O(n).


test: str ="1.1.1.1"
test_out: str = "1[.]1[.]1[.]1"
assert test_out == defang_ip_addr(test)

test = "255.100.50.0"
test_out = "255[.]100[.]50[.]0"
assert test_out == defang_ip_addr(test)
