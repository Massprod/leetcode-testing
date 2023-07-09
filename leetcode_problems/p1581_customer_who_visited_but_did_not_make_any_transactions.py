
# SQL schema:
# DROP TABLE IF EXISTS visits, transactions;
# Create table If Not Exists Visits(visit_id int, customer_id int);
# Create table If Not Exists Transactions(transaction_id int, visit_id int, amount int);
# Truncate table Visits;
# insert into Visits (visit_id, customer_id) values ('1', '23');
# insert into Visits (visit_id, customer_id) values ('2', '9');
# insert into Visits (visit_id, customer_id) values ('4', '30');
# insert into Visits (visit_id, customer_id) values ('5', '54');
# insert into Visits (visit_id, customer_id) values ('6', '96');
# insert into Visits (visit_id, customer_id) values ('7', '54');
# insert into Visits (visit_id, customer_id) values ('8', '54');
# Truncate table Transactions;
# insert into Transactions (transaction_id, visit_id, amount) values ('2', '5', '310');
# insert into Transactions (transaction_id, visit_id, amount) values ('3', '5', '300');
# insert into Transactions (transaction_id, visit_id, amount) values ('9', '5', '200');
# insert into Transactions (transaction_id, visit_id, amount) values ('12', '1', '910');
# insert into Transactions (transaction_id, visit_id, amount) values ('13', '2', '970');
# ------------------------
# Write a SQL query to find the IDs of the users who visited without making any transactions
#   and the number of times they made these types of visits.
# Return the result table sorted in any order.

# SQL query:
# SELECT e3.customer_id, e3.count_no_trans
# FROM (
# 	SELECT
# 	e1.customer_id,
# 	SUM(CASE WHEN e1.visit_id NOT IN (SELECT e2.visit_id FROM transactions AS e2) THEN 1
# 		ELSE 0
# 		END
# 	   ) AS count_no_trans
# 	FROM visits AS e1
# 	GROUP BY e1.customer_id
# ) AS e3
# WHERE e3.count_no_trans > 0
# ORDER BY e3.count_no_trans DESC;

