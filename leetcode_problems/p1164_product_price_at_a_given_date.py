
# Write an SQL query to find the prices of all products on 2019-08-16.
# Assume the price of all products before any change is 10.
# Return the result table in any order.
# ---------------------------
# SQL schema:
# DROP TABLE IF EXISTS products;
#  Create table If Not Exists Products (product_id int, new_price int, change_date date);
# Truncate table Products;
# insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14');
# insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14');
# insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15');
# insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16');
# insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17');
# insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18');
# ---------------------------

# Grotesque SQL query:
# SELECT
# DISTINCT e1.product_id,
# CASE
# 	-- correct
# 	WHEN e1.product_id IN (
# 		SELECT DISTINCT product_id
# 		FROM products
# 		WHERE change_date = '2019-08-16'
# 	)
# 	THEN (
# 		SELECT new_price
# 		FROM products AS test6
# 		WHERE
# 		change_date = '2019-08-16'
# 		AND
# 		e1.product_id = test6.product_id
# 	)
# 	-- correct
# 	WHEN e1.product_id IN (
# 			SELECT DISTINCT product_id
# 			FROM products
# 			WHERE change_date < '2019-08-16'
# 			GROUP BY product_id
# 	)
# 	THEN (
# 		SELECT DISTINCT new_price
# 		FROM products AS test5
# 		WHERE e1.product_id = test5.product_id
# 		AND test5.change_date = (
# 			SELECT DISTINCT last_update
# 			FROM (
# 				SELECT DISTINCT product_id, MAX(change_date) AS last_update
# 				FROM products
# 				WHERE change_date < '2019-08-16'
# 				GROUP BY product_id) AS test3
# 			WHERE test3.product_id = e1.product_id
# 		)
# 	)
# 	ELSE 10
# 	END AS "price"
# FROM
# products AS e1;
# ---------------------------
# Well I guess I'm too focused on using CASE in every task now.
# This Query works, but too slow.
# Still a good practice with CASE.
# ---------------------------
# Rebuild:
# There's 2 options we need:
#   1) All products with changed price before 2019-08-16.
#   2) All products with changed price exactly at 2019-08-16.
# Any other is 10. We ignore everything after this date^^.

# First option:
# SELECT product_id, MAX(change_date) AS "last_change"
# FROM products
# WHERE change_date < '2019-08-16'
# GROUP BY product_id;

# Second option:
# SELECT product_id, MAX(change_date) AS "last_change"
# FROM products
# WHERE change_date < '2019-08-16'
# GROUP BY product_id;

# ^^Ok. Combine them, and we get every possible option of product and change_date before AND at '2019-08-16'.
# Filter on that:
# SELECT product_id, new_price AS "price"
# FROM products
# WHERE (product_id, change_date) IN (
#   SELECT product_id, MAX(change_date) AS "last_change"
#   FROM products
#   WHERE change_date <= '2019-08-16'
#   GROUP BY product_id
# )
# Add everything else:
# UNION
# SELECT product_id, 10 AS price
# FROM products
# GROUP BY product_id
# HAVING MIN(change_date) > '2019-08-16';
# ---------------------------

# SQL query:
# SELECT product_id, new_price AS "price"
# FROM products
# WHERE (product_id, change_date) IN (
# 	SELECT product_id, MAX(change_date)
# 	FROM products
# 	WHERE change_date <= '2019-08-16'
# 	GROUP BY product_id
# )
# UNION
# SELECT product_id, 10 AS "price"
# FROM products
# GROUP BY product_id
# HAVING MIN(change_date) > '2019-08-16';
