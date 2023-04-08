# Given an input string s and a pattern p,
# implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


def is_match(s: str, p: str) -> bool:
    if s == p:
        return True
    original = list(s)
    pattern = list(p)
    many = "*"
    once = "."
    valid = ""
    cursor = 0
    for x in range(0, len(pattern)):
        if cursor == len(original) and p[x] != many and p[x] != once:
            return False
        elif x == (len(pattern) - 1) and p[x] != many:
            check = p[x]
            if check == once:
                valid += original[cursor]
                cursor += 1
            elif original[cursor] == check:
                valid += original[cursor]
                cursor += 1
                break

        elif p[x] == many:
            check = p[x - 1]
            for y in range(cursor, len(original)):
                if check == once:
                    valid += original[y]
                    cursor += 1
                    continue
                elif original[y] == check:
                    valid += original[y]
                    cursor += 1
                    continue
                elif original[y] != check:
                    break
        elif p[x] == once and p[x + 1] == many:
            check = once
            for y in range(cursor, len(original)):
                valid += original[y]
                cursor += 1
        elif p[x] == once:
            valid += original[cursor]
            cursor += 1
            continue

        elif x < (len(pattern) - 1) and p[x + 1] != many:
            check = p[x]
            if original[cursor] == check:
                valid += original[cursor]
                cursor += 1
            else:
                break

    if valid == "".join(original):
        return True
    return False


test0 = "aba"
ptest0 = "aa"
test1 = "aa"
ptest1 = "a"
test2 = "aa"
ptest2 = "a*"
test3 = "ab"
ptest3 = ".*"
test4 = "ab"
ptest4 = ".*c"
test5 = "aab"
ptest5 = "c*a*b"
test6 = "mississippi"
ptest6 = "mis*is*ip*."
# print(is_match(test0, ptest0))
# print(is_match(test1, ptest1))
# print(is_match(test2, ptest2))
# print(is_match(test3, ptest3))
# print(is_match(test4, ptest4))
# print(is_match(test5, ptest5))
print(is_match(test6, ptest6))
