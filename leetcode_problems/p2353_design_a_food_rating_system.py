# Design a food rating system that can do the following:
#  - Modify the rating of a food item listed in the system.
#  - Return the highest-rated food item for a type of cuisine in the system.
# Implement the FoodRatings class:
#  - FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system.
#    The food items are described by foods, cuisines and ratings, all of which have a length of n.
#  - foods[i] is the name of the ith food,
#  - cuisines[i] is the type of cuisine of the ith food, and
#  - ratings[i] is the initial rating of the ith food.
#  - void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
#  - String highestRated(String cuisine) Returns the name of the food item
#    that has the highest rating for the given type of cuisine. If there is a tie,
#    return the item with the lexicographically smaller name.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order,
#  that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i],
#  then x[i] comes before y[i] in alphabetic order.
# -------------------------
# 1 <= n <= 2 * 10 ** 4
# n == foods.length == cuisines.length == ratings.length
# 1 <= foods[i].length, cuisines[i].length <= 10
# foods[i], cuisines[i] consist of lowercase English letters.
# 1 <= ratings[i] <= 10 ** 8
# All the strings in foods are distinct.
# food will be the name of a food item in the system across all calls to changeRating.
# cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
# At most 2 * 10 ** 4 calls in total will be made to changeRating and highestRated.
import heapq


class FoodRatings:
    # working_sol (92.86%, 61.31%) -> (713ms, 47.44mb)

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Every cuisine with reversed heapq to get maximum rating in constant.
        # {cuisine: [(current rating, food)]}
        self.cuisines: dict[str, list[tuple[int, str]]] = {
            cuisines: [] for cuisines in cuisines
        }
        for x in range(len(cuisines)):
            self.cuisines[cuisines[x]].append((ratings[x] * -1, foods[x]))
        for cuisine in self.cuisines:
            heapq.heapify(self.cuisines[cuisine])
        # {food, (cuisine, current rating)}
        self.ratings: dict[str, tuple[str, int]] = {
            foods[x]: (cuisines[x], ratings[x] * -1) for x in range(len(foods))
        }

    def changeRating(self, food: str, newRating: int) -> None:
        # All calls will be viable, no reasons to check if food is correct.
        new_rating: int = newRating * -1
        if self.ratings[food][1] == new_rating:
            return
        cuisine: str = self.ratings[food][0]
        self.ratings[food] = (cuisine, new_rating)
        heapq.heappush(self.cuisines[cuisine], (new_rating, food))

    def highestRated(self, cuisine: str) -> str:
        # ! If there is a tie, return the item with the lexicographically smaller name !
        # Heapq, deals with it by default.
        rating: int
        food: str
        # All calls will be viable, no reasons to check if cuisine is correct.
        # (rating, food)
        rating, food = self.cuisines[cuisine][0]
        while not self.ratings[food][1] == rating:
            heapq.heappop(self.cuisines[cuisine])  # rating changed
            heapq.heappush(self.cuisines[cuisine], (self.ratings[food][1], food))  # add new rating
            rating, food = self.cuisines[cuisine][0]  # check highest again
        return food


# Time complexity:
#   initiations: O(n * log n) <- n - length of input array `foods`, `cuisines`, `ratings`.
#                Traversing all indexes of `cuisines` to assign empty list for them => O(n)
#                Traversing all indexes again to populate all cuisines with (rating, food) => O(n)
#                Worst case: only 1 cuisine type, and we will heapify list with all `n` options => O(n * log n).
#                Traversing all indexes of `food` to populate dictionary with {food: (cuisine, rating)} => O(n).
#   changeRatings: O(log k) <- k - length of heapq for current cuisine of the input food `food`.
#                heappush() == log k, where k - elements in heap.
#   highestRated: O(log m) <- m - length of heapq for current cuisine.
#                Worst case: w.e number of elements we had in heap we will change rating for all of them to 1.
#                So, when we will try to find the highest rating, we're going to delete every type of food, once.
#                And only after this, we're going to get new highest rating => O(constant * 2 * log m).
#                No idea how to call `constant`, because we don't know how many elements were updated.
#                It can be 0 or 1000 or w.e. But for every single one of them we will use heappop() + heappush().
#                Both of them taking O(log m).
# Auxiliary space:
#   classObject: O(n)
#   changeRatings: O(1) -> only updating already existed, nothing new added.
#   highestRated: O(1) -> only operating with already stored values.
