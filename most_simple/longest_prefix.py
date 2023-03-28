
def longest_prefix(strings: list[str]) -> str:
    # prefix = ""
    # x = 0
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
    prefix = ""
    for x in range(len(strings[0])):
        for words in strings:
            if strings[0][x] in words[x]:
                continue
            return prefix
        prefix += strings[0][x]
    return prefix


print(longest_prefix(["kn", "k", "k"]))
