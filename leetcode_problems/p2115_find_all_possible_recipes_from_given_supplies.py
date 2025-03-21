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
from collections import defaultdict
from email.policy import default


def find_all_recipes(
        recipes: list[str], ingredients: list[list[str]], supplies: list[str]
) -> list[str]:
    fast_sups: set[str] = set(supplies)

    rec_graph: dict[str, list[str]] = {}
    for index in range(len(recipes)):
        recipe: str = recipes[index]
        rec_graph[recipe] = ingredients[index]

    def check(
            recipe: str,
            used: dict[str, set[str]]
    ) -> bool:
        if recipe not in rec_graph:
            return False
        
        res: bool = True
        for ingredient in rec_graph[recipe]:
            # Cycle
            if ingredient in used[recipe]:
                return False
            # Ingredient is different `recipe`
            elif ingredient in rec_graph:
                used[recipe].add(ingredient)
                res = check(ingredient, used)
            # Not present
            elif ingredient not in fast_sups:
                return False
            
        return res

    # We can have `recipe` itself in the `ingredients` == cycle.
    out: list[str] = []
    for recipe in rec_graph:
        cycle_ingredients: dict[str, set[str]] = defaultdict(set)
        if not check(recipe, cycle_ingredients):
            continue
        out.append(recipe)

    return out


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
test_ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
test_supplies = ["yeast", "flour", "meat"]
test_out = ["bread", "sandwich", "burger"]
assert test_out == find_all_recipes(test_recipes, test_ingredients, test_supplies)
