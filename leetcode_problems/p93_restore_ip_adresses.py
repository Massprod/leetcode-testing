# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#   For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
#   but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses
#   that can be formed by inserting dots into s.
# You are not allowed to reorder or remove any digits in s.
# You may return the valid IP addresses in any order.
# ----------------
# 1 <= s.length <= 20  ,  s - consists of digits only.


def restore_ip(s: str) -> list[str]:
    pass


test1 = "25525511135"
test1_out = ["255.255.11.135", "255.255.111.35"]

test2 = "0000"
test2_out = ["0.0.0.0"]

test3 = "101023"
test3_out = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
