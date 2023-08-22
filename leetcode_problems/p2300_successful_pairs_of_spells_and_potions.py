# You are given two positive integer arrays spells and potions,
#   of length n and m respectively, where spells[i] represents the strength of the ith spell
#   and potions[j] represents the strength of the jth potion.
# You are also given an integer success.
# A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions
#   that will form a successful pair with the ith spell.
# ------------------
# n == spells.length
# m == potions.length
# 1 <= n, m <= 10 ** 5
# 1 <= spells[i], potions[i] <= 10 ** 5
# 1 <= success <= 10 ** 10
from random import randint


def successful_pairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    # working_sol (87.41%, 5.4%) -> (1123m,s 57mb)  time: O(n * log n + m * log m) | space: O(n)
    # Instead of standard BS for every spell, we can just save the lowest potion.
    # Because if we sort Spells, everything lower will either build same Pair with potions,
    #  or we can move by 1 potion higher and recheck.
    # At some point we can reach END of the Potions, and just ignore them.
    # Cuz None of the Lower spell options will build correct Pair.
    # So we need to check Potions only 1 Time for all Spells.
    # Only problem is resetting Values into original List == Spells.
    # Because we can't change order of the original spells.
    original_spells: dict[int, list[int]] = {}
    # So I'm saving every possible Value from Spells into a dictionary,
    #  and for every Value saving its original Indexes.
    for _ in range(len(spells)):
        if spells[_] in original_spells:
            original_spells[spells[_]] += [_]
            continue
        original_spells[spells[_]] = [_]
    # We need extra array with sorted Spells.
    sorted_spells: list[int | tuple[int, int]] = sorted(spells)
    potions.sort()
    # Minimal limit, we can start from.
    min_potion: int = 0
    # For every lower Spell, start checking from Minimal correct Potion
    #  for Higher spell found before.
    for x in range(len(sorted_spells) - 1, -1, -1):
        try_spell: int = sorted_spells[x]
        found: bool = False
        # If Potions exhausted ->
        while min_potion != len(potions):
            check_suc: int = try_spell * potions[min_potion]
            if check_suc >= success:
                found = True
                break
            min_potion += 1
        # -> we can Annul every Lower spell.
        correct_potions: int = 0
        # Otherwise, we can use everything Higher + including this Potion.
        if found:
            correct_potions = len(potions) - min_potion
        # Saving original SpellValue and number of correct Potions.
        sorted_spells[x] = (sorted_spells[x], correct_potions)
    # Reset every saved Index of original SpellValue with
    #  number of correct Potions.
    for pair in sorted_spells:
        while original_spells[pair[0]]:
            spells[original_spells[pair[0]].pop()] = pair[1]
    return spells


# Time complexity: O(n * log n + m * log m) -> traversing whole input_spells once to save indexes => O(n) ->
# n - len of input_spells^^|  -> sorting and saving input_spells => O(n * log n) ->
# m - len of input_potions^^| -> sorting input_potions => O(m * log m) ->
#                             -> traversing copied input_spells, same values but sorted and for every index
#                             check for correct potions, input_potions indexes will be used only once => O(n + m) ->
#                             -> resetting original spells with counted correct_potions => O(n).
#                             So sorting will take maximum time:
#                               O(n * log n + m * log m) or O(max(n * log n + m * log m))?
# Auxiliary space: O(n) -> saving every unique Spells value, and it's index into a dictionary => O(2n) ->
#                       -> saving copy of original Spells, sorted => O(n) ->
#                       -> resetting every value in a copy with tuple[int, int] instead of Int so it's x2 => O(2n).
# ------------------
# Ok. Working correctly with big constraint, time to fail and see tricky parts.
# Nah. Actually worked and even normal speed, but Memory is like 50% more than average :)
# Well it's working and without BS and in time so it's Success.
# ------------------
# Ok. It's marked like a Binary search problem and in Hints they say:
# ! Thus, for each spell, we need to find the potion with the least strength that will form a successful pair. !
# ! We can efficiently do this by sorting the potions based on strength and using binary search. !
# But do I really need to do this? Like we can just sort Spells and Potions, and start from Highest spell.
# On first encounter of correct potion, we can just count everything else as correct potions as well.
# And start check for this First potion for every other Spell, if it's correct then it's the same number of potions.
# If it's not correct we just move 1 index and re check.
# Every spell after will either start from this First potion, or it just can build correct Pair at all.
# Cuz every spell is Lower and potions are the same.
# So we can just Maintain the smallest possible Potion to use, and if there's None left,
#  other spells 100% can't make a correct pair.
# Let's try this one, cuz I see it should be faster. We don't need to search for every spell, just reuse.
# Actually there's a problem, we need to return Array with correct order of spells.
# Then I need to save correct state of original, and it's slow to reproduce later.
# Like save every value from spells into a dictionary with list of indexes, cuz we can have duplicates.
# And replace original spells array with counter values with taking indexes from this dictionary, is it slower tho?
# Actually I can try this to pass TLE and see.


test_spells: list[int] = [5, 1, 3]
test_potions: list[int] = [1, 2, 3, 4, 5]
test_success: int = 7
test_out: list[int] = [4, 0, 3]
assert test_out == successful_pairs(test_spells, test_potions, test_success)

test_spells = [3, 1, 2]
test_potions = [8, 5, 8]
test_success = 16
test_out = [2, 0, 2]
assert test_out == successful_pairs(test_spells, test_potions, test_success)

test_spells = []
test_potions = []
test_success = randint(1, 10 ** 10)
for _ in range(10 ** 3):
    test_spells.append(randint(1, 10 ** 5))
    test_potions.append(randint(1, 10 ** 5))
print(test_spells)
print('-----------')
print(test_potions)
print('------------!')
print(test_success)
