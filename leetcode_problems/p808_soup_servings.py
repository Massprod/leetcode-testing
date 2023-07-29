# There are two types of soup: type A and type B. Initially, we have n ml of each type of soup.
# There are four kinds of operations:
#   Serve 100 ml of soup A and 0 ml of soup B,
#   Serve 75 ml of soup A and 25 ml of soup B,
#   Serve 50 ml of soup A and 50 ml of soup B, and
#   Serve 25 ml of soup A and 75 ml of soup B.
# When we serve some soup, we give it to someone, and we no longer have it.
# Each turn, we will choose from the four operations with an equal probability 0.25.
# If the remaining volume of soup is not enough to complete the operation,
#   we will serve as much as possible.
# We stop once we no longer have some quantity of both types of soup.
# Note that we do not have an operation where all 100 mil's of soup B are used first.
# Return the probability that soup A will be empty first,
#   plus half the probability that A and B become empty at the same time.
# Answers within 10 ** -5 of the actual answer will be accepted.
# -------------------
# 0 <= n <= 10 ** 9


def soup_servings(n: int) -> float:
    # working_sol (83.96%, 29.72%) -> (49ms, 18.6mb)  time: O(4 ** (n / 25)) | space: O(4  ** (n / 25)) / 4)
    # Recursion cache.
    rec_cache: dict[tuple[int, int], float] = {}
    # Only 4 options to serve a soup.
    serve_options: list[tuple[int, int]] = [(100, 0),  (75, 25), (50, 50), (25, 75)]

    def serve(soup_a: int, soup_b: int) -> float:
        # If both exhaust at the same time,
        # it should be 1, but we're given rule ->
        # -> ! Plus half the probability that A and B become empty at the same time !
        if soup_a <= 0 and soup_b <= 0:
            return 0.5
        # Any correct outcome is 1, until we divide it by ALL options.
        if soup_a <= 0:
            return 1.0
        # Incorrect is 0.
        if soup_b <= 0:
            return 0.0
        if (soup_a, soup_b) in rec_cache:
            return rec_cache[soup_a, soup_b]

        # Probability of soup A being emptied first + half of equal.
        probability: float = 0.0
        for option in serve_options:
            # There's always 4 options, so if we get correct or incorrect result
            # we still need to divide result probability by all available options.
            # It's either ! serve * 0.25 ! or ! serve / 4 !
            probability += serve(soup_a - option[0], soup_b - option[1]) / 4

        rec_cache[soup_a, soup_b] = probability
        return probability

    # Anything higher is recursion_max_depths.
    # And by the LLN(Law of the Large Numbers) ->
    # -> we can assume it tends to 1.
    if n >= 10 ** 4:
        return 1.0
    return serve(n, n)


# Time complexity: O(4 ** (n / 25)) -> well for n >= 10 ** 4 it's constant O(1) -> but for cases lower it's should be
# n - input soup_amounts^^| recursion tree with depths n / 25, cuz in the worst case we're taking soup A
#                           by -25 and calling recursion again -> so it's 4 options and (n / 25) depths =>
#                           => O(4 ** (n / 25)), at least correct for 100 and 500.
# Auxiliary space: O((4  ** (n / 25)) / 4) -> we're saving 1/4 of all recursion calls => O((4 ** (n / 25)) / 4).
#                            ^^Extra I think it should be CEIL() division, but w.e. Doubt its correctness anyway.
# -------------------
# Ok. At least working, but there's recursion limit for 10 ** 5 and higher constraints.
# So it's either can't be solved with recursion or I don't know something.
# Extra math about probability -> IF n becomes larger our probability of A being empty first is always growing.
# So every value after 10 ** 5 is going to be ~1. Actually tested with 10 ** 4, same.
# -------------------
# Well first two cases is easy, but what if we have more than 1 iteration?
# Should we summarize all outcomes? Like full probability should consider all outcomes so yeah, let's try  to
# just build recursion with all 3 outcomes -> A is first, B is fist, A == B:
# 1 -> 0.25 for A is first, 1/4 options is correct
# 2 -> 0.125 for A == B, half of the standard
# 3 -> 0 for B first, A can't be first at all
# Like for test2 -> 0.25 * ( 0.25 + 0.25 + 0.25 + 0.25 + 0.125 + 0.75 + 0.125 + 0.5 + 0.125 + 0.25) ->
# -> but im taking 1/4 for the last option, and it's correct for small test_case but if there's more than 2 servings ->
# -> then every option we take should be 1/4 of all options which could be taken on this serving =>
# => so I need to take 0.25 * result of any option, to get correct probability for all of them.


test1 = 50
test1_out = 0.62500
assert test1_out == round(soup_servings(test1), 5)

test2 = 100
test2_out = 0.71875
assert test2_out == round(soup_servings(test2), 5)

test3 = 10 ** 4
test3_out = 1
assert test3_out == round(soup_servings(test3), 5)
