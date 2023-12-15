# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path
#  going from cityAi to cityBi.
# Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore,
#  there will be exactly one destination city.
# ----------------------
# 1 <= paths.length <= 100
# paths[i].length == 2
# 1 <= cityAi.length, cityBi.length <= 10
# cityAi != cityBi
# All strings consist of lowercase and uppercase English letters and the space character.


def dest_city(paths: list[list[str]]) -> str:
    # working_sol (95.85%, 45.28%) -> (52ms, 16.33mb)  time: O(n) | space: O(n)
    # ! there will be exactly one destination city !
    # Only one city from whom we can't travel anywhere,
    #  and we're guaranteed it will exist.
    # {cities from whom we can travel}
    starts: set[str] = set()
    for x in range(len(paths)):
        starts.add(paths[x][0])
    for x in range(len(paths)):
        if paths[x][1] not in starts:
            return paths[x][1]


# Time complexity: O(n) <- n - length of input array `paths`.
# We traverse every cities pair to get START cities => O(n).
# Worst case: we will have desired city on last index.
# Extra traverse of original cities pairs to get city without outgoing path => O(n).
# O(2n) => O(n).
# ----------------------
# Auxiliary space: O(n).
# Same worst case, we will just store every start city in `starts` and their # equal to 'n'.


test: list[list[str]] = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
test_out: str = "Sao Paulo"
assert test_out == dest_city(test)

test = [["B", "C"], ["D", "B"], ["C", "A"]]
test_out = "A"
assert test_out == dest_city(test)

test = [["A", "Z"]]
test_out = "Z"
assert test_out == dest_city(test)
