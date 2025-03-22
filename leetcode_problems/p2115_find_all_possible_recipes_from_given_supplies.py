# You have information about n different recipes.
# You are given a string array recipes and a 2D string array ingredients.
# The ith recipe has the name recipes[i],
#  and you can create it if you have all the needed ingredients from ingredients[i].
# A recipe can also be an ingredient for other recipes, i.e., ingredients[i]
#  may contain a string that is in recipes.
# You are also given a string array supplies containing all the ingredients
#  that you initially have, and you have an infinite supply of all of them.
# Return a list of all the recipes that you can create.
# You may return the answer in any order.
# Note that two recipes may contain each other in their ingredients.
# ------------------------
# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.


def find_all_recipes(
        recipes: list[str], ingredients: list[list[str]], supplies: list[str]
) -> list[str]:
    # working_sol (72.85%, 17.91%) -> (60ms, 26.24mb)  time: O(n + m + k) | space: O(n + m + k)
    # { ingredient | recipe: present | can be created }
    fast_sups: dict[str, bool] = {
        supply: True for supply in supplies
    }

    # { recipe: ingredients for the recipe }
    rec_graph: dict[str, list[str]] = {}
    for index in range(len(recipes)):
        recipe: str = recipes[index]
        rec_graph[recipe] = ingredients[index]

    def check(
        recipe: str,
        used: set[str],
    ) -> bool:
        # Already builded == use cached. Or it's basic ingredient.
        if fast_sups.get(recipe, False):
            return True
        
        # We don't have info about recipe. Or it's a cycle.
        if recipe not in rec_graph or recipe in used:
            return False      

        res: bool = True
        used.add(recipe)
        for ingredient in rec_graph[recipe]:
            if not check(ingredient, used):
                res = False
                break
            
        fast_sups[recipe] = res
        return res

    out: list[str] = []
    for recipe in rec_graph:
        # We can have `recipe` itself in the `ingredients` == cycle.
        cycle_ingredients: set[str] = set()
        if not check(recipe, cycle_ingredients):
            continue
        out.append(recipe)

    return out


# Time complexity: O(n + m + k) <- n - length of the input array `recipes`,
#                                  m - length of the input array `ingredients`,
#                                  k - length of the input array `supplies`.
# Traversing `supplies` to build `fast_sups` => O(k).
# Traversing `recipes` & `ingredients` to build `rec_graph` => O(n + m + k).
# In out case every node is a `recipe` | ingredient
# `fast_sups` is a cache and we're traversing all of the nodes, once => O(2 * (n + m + k)).
# ------------------------
# Auxiliary space: O(n + m + k)
# `fast_sups` <- allocates space for each supply from original and cache from
# ingrediends (in the worst case, we will have every ingredient as a unique extra build) =>
#  => O(m + k).
# `rec_graph` <- allocates space for each `recipe` and all assigned to it `ingredient`s =>
# => O(n + m).
# In the worst case, we will use every `recipe` in one traverse.
# Like `recipe_1` -> built from `recipe_2`...`recipe_n`
# `cycle_ingredients` <- allocates space for each `recipe` from `recipes` => O(n).


test_recipes: list[str] = ["bread"] 
test_ingredients: list[list[str]] = [["yeast", "flour"]]
test_supplies: list[str] = ["yeast", "flour", "corn"]
test_out: list[str] = ["bread"]
assert test_out == find_all_recipes(test_recipes, test_ingredients, test_supplies)

test_recipes = ["bread", "sandwich"]
test_ingredients = [["yeast", "flour"], ["bread", "meat"]]
test_supplies = ["yeast", "flour", "meat"]
test_out = ["bread", "sandwich"]
assert test_out == find_all_recipes(test_recipes, test_ingredients, test_supplies)

test_recipes = ["bread", "sandwich", "burger"]
test_ingredients = [
    ["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]
    ]
test_supplies = ["yeast", "flour", "meat"]
test_out = ["bread", "sandwich", "burger"]
assert test_out == find_all_recipes(test_recipes, test_ingredients, test_supplies)
