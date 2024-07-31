# You are given an array books where books[i] = [thicknessi, heighti]
#  indicates the thickness and height of the ith book.
# You are also given an integer shelfWidth.
# We want to place these books in order onto bookcase shelves that have a total width shelfWidth.
# We choose some of the books to place on this shelf such that the sum of their thickness
#  is less than or equal to shelfWidth, then build another level of the shelf of the bookcase
#  so that the total height of the bookcase has increased by the maximum height of the books we just put down.
# We repeat this process until there are no more books to place.
# Note that at each step of the above process,
#  the order of the books we place is the same order as the given sequence of books.
# For example, if we have an ordered list of 5 books,
#  we might place the first and second book onto the first shelf,
#  the third book on the second shelf, and the fourth and fifth book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
# -----------------------
# 1 <= books.length <= 1000
# 1 <= thicknessi <= shelfWidth <= 1000
# 1 <= heighti <= 1000
from functools import cache


def min_height_shelves(books: list[list[int]], shelf_width: int) -> int:
    # working_sol (53.67%, 19.21%) -> (52ms, 17.85mb)  time: O(n * m) | space: O(n * m)
    # max height is 1000 ** 2
    limit: int = 10000 ** 2

    @cache
    def check(cur_book: int, distance_left: int, shelf_height: int) -> int:
        nonlocal limit
        # If we continue populating the same row, it's HEIGHT can change.
        # If we put a book with higher HEIGHT, it will become a new height of the row.
        shelf_height_updated = max(shelf_height, books[cur_book][1])
        if cur_book == len(books) - 1:
            # Last book placed on the same row, enough space.
            if distance_left >= books[cur_book][0]:
                return shelf_height_updated
            # The Last book is on a new row with hers HEIGHT used as row HEIGHT.
            return shelf_height + books[cur_book][1]
        # Building a new row, no matter how many space left.
        new_row: int = shelf_height + check(
            cur_book + 1,
            shelf_width - books[cur_book][0],  # `distance_left` after placing this book
            books[cur_book][1],  # new row basic height == first used book
        )
        # Placing book on the same row.
        old_row: int = limit
        if distance_left >= books[cur_book][0]:
            old_row = check(
                cur_book + 1,
                distance_left - books[cur_book][0],
                shelf_height_updated,  # last height data of the current row.
            )
        out: int = min(old_row, new_row)
        return out

    return check(0, shelf_width, 0)


# Time complexity: O(n * m) <- n - length of the input array `books`, m - input value `shelf_width`.
# In the worst case, every BOOK can be placed on the newRow, and every row can be fully populated with them.
# We will try to use every BOOK on a new row and for each row we will populate it until we can => O(n * m).
# -----------------------
# Auxiliary space: O(n * m)
# Every call will be stored in `cache` => O(n * m).


test: list[list[int]] = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
test_width: int = 4
test_out: int = 6
assert test_out == min_height_shelves(test, test_width)

test = [[1, 3], [2, 4], [3, 2]]
test_width = 6
test_out = 4
assert test_out == min_height_shelves(test, test_width)
