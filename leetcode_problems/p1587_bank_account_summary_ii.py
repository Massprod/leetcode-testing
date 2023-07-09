
# SQL schema:
# DROP TABLE IF EXISTS users, transactions;
# Create table If Not Exists Users (account int, name varchar(20));
# Create table If Not Exists Transactions (trans_id int, account int, amount int, transacted_on date);
# Truncate table Users;
# insert into Users (account, name) values ('900001', 'Alice');
# insert into Users (account, name) values ('900002', 'Bob');
# insert into Users (account, name) values ('900003', 'Charlie');
# Truncate table Transactions;
# insert into Transactions (trans_id, account, amount, transacted_on) values ('1', '900001', '7000', '2020-08-01');
# insert into Transactions (trans_id, account, amount, transacted_on) values ('2', '900001', '7000', '2020-09-01');
# insert into Transactions (trans_id, account, amount, transacted_on) values ('3', '900001', '-3000', '2020-09-02');
# insert into Transactions (trans_id, account, amount, transacted_on) values ('4', '900002', '1000', '2020-09-12');
# insert into Transactions (trans_id, account, amount, transacted_on) values ('5', '900003', '6000', '2020-08-07');
# insert into Transactions (trans_id, account, amount, transacted_on) values ('6', '900003', '6000', '2020-09-07');
# insert into Transactions (trans_id, account, amount, transacted_on) values ('7', '900003', '-4000', '2020-09-11');
# ------------------------
# Write an SQL query to report the name and balance of users with a balance higher than 10000.
# The balance of an account is equal to the sum of the amounts of all transactions involving that account.
# Return the result table in any order.

# SQL query:
# SELECT e2.name, SUM(e1.amount) AS balance
# FROM transactions AS e1
# JOIN users AS e2 ON e1.account = e2.account
# GROUP BY e2.name
# HAVING SUM(e1.amount) > 10000;
