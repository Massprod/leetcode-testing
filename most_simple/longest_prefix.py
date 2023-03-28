
def longest_prefix(strings: list[str]) -> str:
    # prefix = ""
    # x = 0
    #strings.sort()
    # check = strings[x]
    # for letter in check:
    #     for _ in strings:
    #         if letter in _[x]:
    #             continue
    #         return prefix
    #     x += 1
    #     prefix += letter
    # return prefix

    # both working this one is just more *pretty*
    # prefix = ""
    # strings.sort()
    # for x in range(len(strings[0])):
    #     for word in strings:
    #         if strings[0][x] in word[x]:
    #             continue
    #         return prefix
    #     prefix += strings[0][x]
    # return prefix

    prefix = ""
    strings.sort()
    for x in range(len(strings[0])):
        if strings[0][x] != strings[-1][x]:
            return prefix
        prefix += strings[0][x]
    return prefix


print(longest_prefix(["flower", "flow", "flight"]))
