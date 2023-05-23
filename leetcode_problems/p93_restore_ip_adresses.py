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
    validated: list[str] = []
    if not 4 <= len(s) <= 12:
        return validated

    def recurs_slice(sliced: str, tempo_ip: list[str]) -> None:
        if len(sliced) == 0 and len(tempo_ip) == 4:
            validated.append("".join(tempo_ip))
            return
        if len(tempo_ip) == 4 and len(sliced) != 0:
            return
        if len(tempo_ip) != 4 and len(sliced) == 0:
            return
        if 0 <= int(sliced[0]) <= 9:
            if len(tempo_ip) == 3:
                tempo_ip.append(sliced[0])
            if len(tempo_ip) < 3:
                tempo_ip.append(f"{sliced[0]}.")
            recurs_slice(sliced[1:], tempo_ip)
            tempo_ip.pop()
        if len(sliced) > 1 and int(sliced[0]) != 0 and 10 <= int(sliced[0] + sliced[1]) <= 99:
            if len(tempo_ip) == 3:
                tempo_ip.append(sliced[0] + sliced[1])
            if len(tempo_ip) < 3:
                tempo_ip.append(f"{sliced[0]}{sliced[1]}.")
            recurs_slice(sliced[2:], tempo_ip)
            tempo_ip.pop()
        if len(sliced) > 2 and int(sliced[0]) != 0:
            if 100 <= int(sliced[0] + sliced[1] + sliced[2]) <= 255:
                if len(tempo_ip) == 3:
                    tempo_ip.append(sliced[0] + sliced[1] + sliced[2])
                if len(tempo_ip) < 3:
                    tempo_ip.append(f"{sliced[0]}{sliced[1]}{sliced[2]}.")
                recurs_slice(sliced[3:], tempo_ip)
                tempo_ip.pop()

    recurs_slice(s, [])
    return validated

# First of all this basic: 1 <= s.length <= 20.
# Ip address can be at low limit of length 4 and max limit of length 12, and in p91 I have been hitting time_limit.
# When tried to use every possible slice, but in this case it's limited to 12 and should be enough ok with speed.
# Otherwise, I need to find a way to cull some recursion calls.


test1 = "25525511135"
test1_out = ["255.255.11.135", "255.255.111.35"]
print(restore_ip(test1))
assert test1_out == restore_ip(test1)

test2 = "0000"
test2_out = ["0.0.0.0"]
print(restore_ip(test2))
assert test2_out == restore_ip(test2)

test3 = "101023"
test3_out = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
print(restore_ip(test3))
assert test3_out == restore_ip(test3)
