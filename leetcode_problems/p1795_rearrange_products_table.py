
# SQL schema:
# DROP TABLE IF EXISTS products;
# Create table If Not Exists Products (product_id int, store1 int, store2 int, store3 int);
# Truncate table Products;
# insert into Products (product_id, store1, store2, store3) values ('0', '95', '100', '105');
# insert into Products (product_id, store1, store2, store3) values ('1', '70', Null, '80');
# ----------------------
# Rearrange the Products table so that each row has (product_id, store, price).
# If a product is not available in a store, do not include a row with that product_id
#   and store combination in the result table.
# Return the result table in any order.

# SQL query:
# -- store1 pivot --
# SELECT
# product_id,
# 'store1' AS store,
# store1 AS price
# FROM products
# WHERE store1 IS NOT Null
# UNION ALL
# -- store2 pivot --
# SELECT
# product_id,
# 'store2' AS store,
# store2 AS price
# FROM products
# WHERE store2 IS NOT Null
# UNION ALL
# -- store3 pivot --
# SELECT
# product_id,
# 'store3' AS store,
# store3 AS price
# FROM products
# WHERE store3 IS NOT Null
# ORDER BY product_id;

# Expected output:
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
# | 1          | store3 | 80    |
# +------------+--------+-------+
