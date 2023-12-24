# In a project, you have a list of required skills req_skills, and a list of people.
# The ith person people[i] contains a list of skills that the person has.
# Consider a sufficient team: a set of people such that for every required skill in req_skills,
#  there is at least one person in the team who has that skill.
# We can represent these teams by the index of each person.
#  - For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
# Return any sufficient team of the smallest possible size, represented by the index of each person.
# You may return the answer in any order.
# It is guaranteed an answer exists.
# -------------------
# 1 <= req_skills.length <= 16
# 1 <= req_skills[i].length <= 16
# req_skills[i] consists of lowercase English letters.
# All the strings of req_skills are unique.
# 1 <= people.length <= 60
# 0 <= people[i].length <= 16
# 1 <= people[i][j].length <= 16
# people[i][j] consists of lowercase English letters.
# All the strings of people[i] are unique.
# Every skill in people[i] is a skill in req_skills.
# It is guaranteed a sufficient team exists.
from functools import cache


def smallest_sufficient_team(req_skills: list[str], people: list[list[str]]) -> list[int]:
    # working_sol (45.62%, 59.85%) -> (616ms, 22.5mb)  time: O(2 ** n * k) | space: O(2 ** n)
    # {skill, bit placement}
    skills_placement: dict[str, int] = {skill: placement for placement, skill in enumerate(req_skills)}
    fully_covered: int = 0
    for _ in req_skills:
        fully_covered = (fully_covered << 1) + 1
    hired: set[int] = set()

    @cache
    def check(uncovered: int) -> int:
        if uncovered == fully_covered:
            return 0
        # Best hiring strategy from current call -> to fully covered.
        best_option: int = 0
        for index, skillset in enumerate(people):
            new_coverage: int = uncovered
            # Already hired this person on this path.
            if index in hired:
                continue
            # Place '1' bit for every skill this person have, we already marked them.
            for skill in skillset:
                new_coverage = new_coverage | (1 << skills_placement[skill])
            # Only way it changes, it's when we get a new skill we need.
            if new_coverage != uncovered:
                hired.add(index)
                # Backtrack from 0 -> w.e we hired. So we just place '1' bit on unique person index.
                cur_option: int = check(new_coverage) | (1 << index)
                hired.remove(index)
                if not best_option:
                    best_option = cur_option
                # We only care about minimum option, and bits placed == persons hired on this path.
                elif cur_option.bit_count() < best_option.bit_count():
                    best_option = cur_option
        return best_option
    # We don't care about '0b' part.
    out: list[int] = [person_index for person_index, placement in enumerate(bin(check(0))[:1:-1]) if placement == '1']
    return out


# Time complexity: O(2 ** n * k) <- n - length of input array `req_skills`,  k - length of input array `people`.
# Worst case: every person only covers 1 skill.
# We will have (2 ** n) options to cover all skills == recursion calls, and for every call we check all persons
#  we could hire => O(2 ** n * k).
# Even if we skip some persons, which already in `hired` it's still linear.
# -------------------
# Auxiliary space: O(2 ** n).
# Worst case: every person only covers 1 skill.
# We will have set `hired` with all persons in it => O(k).
# We will have @cache with all calls made => O(2 ** n).
# We will have `skills_placement` of size n, key for every skill => O(n).
# And if we have k == n, and they cover all skills one by one, we will have `out` with size k => O(k).
# Extra we will have string `smallest_team` with size of k, because we include first + last indexes of workers => O(k).
# O(2 ** n + n + 3k), 2 ** n dominates all of them completely, so it's just => O(2 ** n).
# -------------------
# Only 16 options of skills, so we can use INT as bitmap to remember them.
# Only question is from what is best to start: '000..00' or '111..11'.
# Both should be the same, because we still need to store what skill placed on some (# bit).
# Workers? Never used unsigned integer for bitmap, but I guess it's doable. Yeah, bin(1<<60) 60 bit set.
# So, we use hired workers as INT as well.
# Backtrack or path? We need minimum workers option, so we can just backtrack from last call with all skills covered
#  and choose lowest bitcount() from all calls.
# Otherwise I need another argument with how many we already hired, and then find difference between:
# (all covered(last) call hired) - (how many we hired on current call) and choose minimum of every call from this.
# Which is doable, but it's extra memory, and we still need to use INT to store who we hire.
# So, it's better to just bitcount() from them.
# Different workers can cover same skills, and lead us to same uncovered options, so we can use dict() to memorise.
# Or it's better to use @cache, it's faster and I already practiced enough with memorisation,
#  at least in such simple case.
# Should be correct.


test: list[str] = ["java", "nodejs", "reactjs"]
test_ppl: list[list[str]] = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
test_out: list[int] = [0, 2]
assert test_out == smallest_sufficient_team(test, test_ppl)

test = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
test_ppl = [
    ["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
    ["java", "csharp", "aws"], ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]
]
test_out = [1, 2]
assert test_out == smallest_sufficient_team(test, test_ppl)
