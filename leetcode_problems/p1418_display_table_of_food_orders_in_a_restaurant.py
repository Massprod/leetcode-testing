# Given the array orders, which represents the orders that customers
#  have done in a restaurant.
# More specifically orders[i]=[customerNamei,tableNumberi,foodItemi]
#  where customerNamei is the name of the customer, tableNumberi is the table
#  customer sit at, and foodItemi is the item customer orders.
# Return the restaurant's “display table”.
# The “display table” is a table whose row entries denote how many
#  of each food item each table ordered.
# The first column is the table number and the remaining columns correspond
#  to each food item in alphabetical order.
# The first row should be a header whose first column is “Table”,
#  followed by the names of the food items.
# Note that the customer names are not part of the table.
# Additionally, the rows should be sorted in numerically increasing order.
# ----------------------------
# 1 <= orders.length <= 5 * 10^4
# orders[i].length == 3
# 1 <= customerNamei.length, foodItemi.length <= 20
# customerNamei and foodItemi consist of lowercase
#  and uppercase English letters and the space character.
# tableNumberi is a valid integer between 1 and 500.
from collections import defaultdict


def display_table(orders: list[list[str]]) -> list[list[str]]:
    # working_sol (84.83%, 71.21%) -> (327ms, 29.90mb)  time: O(n * log n) | space: O(n)
    # { all unique food items }
    all_items: set[str] = set()
    # { table: { item: orders } }
    tables:  dict[str, dict[str, int]] = defaultdict(dict)
    for _, table, item in orders:
        all_items.add(item)
        item_quant: int  = tables[table].get(item)
        if item_quant is None:
            tables[table][item] = 1
            continue
        tables[table][item] += 1
    # ! each food item in alphabetical order !
    alph_items: list[str] = sorted(all_items)
    out: list[list[str]] = [ ['Table'] + alph_items ]
    # ! rows should be sorted in numerically increasing order !
    for table in sorted(tables.keys(), key=lambda x: int(x)):
        new_row: list[str] = [table]
        for item in alph_items:
            if item in tables[table]:
                new_row.append(str(tables[table][item]))
            else:
                new_row.append('0')
        out.append(new_row)

    return out


# Time complexity: O(n * log n) <- n - length of the input array `orders`.
# Traversing whole input array `orders` to get all the orders and tables => O(n).
# Sorting all the unique items we got, in the worst case:
#  every record is unique food item => O(n + n * log(n)).
# Sorting allt he unique tables we got, in the worst case:
#  every table id is unique => O(n + n * log(n) + n * log n).
# Finally traversing all the tables + items, because every record is unique item => O(n).
# ----------------------------
# Auxiliary space: O(n)
# `all_items` <- allocates space for each unique food item => O(n).
# `tables` <- allocates space for each unique table => O(2 * n).
# `out` <- allocates space for each unique table + all foods as columns => O(4 * n).
# `sorted` <- extra `n` for each convert => O(6 * n).


test: list[list[str]] = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]
]
test_out: list[list[str]] = [
    ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
    ["3", "0", "2", "1", "0"],
    ["5", "0", "1", "0", "1"],
    ["10", "1", "0", "0", "0"]
]
assert test_out == display_table(test)

test = [
    ["James", "12", "Fried Chicken"],
    ["Ratesh", "12", "Fried Chicken"],
    ["Amadeus", "12", "Fried Chicken"],
    ["Adam", "1", "Canadian Waffles"],
    ["Brianna", "1", "Canadian Waffles"]
]
test_out = [
    ["Table", "Canadian Waffles", "Fried Chicken"],
    ["1", "2", "0"],
    ["12", "0", "3"]
]
assert test_out == display_table(test)

test = [
    ["Laura", "2", "Bean Burrito"],
    ["Jhon", "2", "Beef Burrito"],
    ["Melissa", "2", "Soda"]
]
test_out = [
    ["Table", "Bean Burrito", "Beef Burrito", "Soda"],
    ["2", "1", "1", "1"]
]
assert test_out == display_table(test)
