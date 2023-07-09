
# SQL schema:
# DROP TYPE IF EXISTS operation_enum;
# CREATE TYPE operation_enum AS ENUM('Sell', 'Buy');
# DROP TABLE IF EXISTS stocks;
# Create Table If Not Exists Stocks (stock_name varchar(15), operation operation_enum, operation_day int, price int);
# Truncate table Stocks;
# insert into Stocks (stock_name, operation, operation_day, price) values ('Leetcode', 'Buy', '1', '1000');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Buy', '2', '10');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Leetcode', 'Sell', '5', '9000');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Handbags', 'Buy', '17', '30000');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Sell', '3', '1010');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Buy', '4', '1000');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Sell', '5', '500');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Buy', '6', '1000');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Handbags', 'Sell', '29', '7000');
# insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Sell', '10', '10000');
# -------------------------
# Write an SQL query to report the Capital gain/loss for each stock.
# The Capital gain/loss of a stock is the total gain or loss after
#   buying and selling the stock one or many times.
# Return the result table in any order.
# -------------------------
# SQL query:
# SELECT
# stock_name,
# SUM(CASE WHEN operation = 'Buy' THEN -price
#    		 WHEN operation = 'Sell' THEN price
#    		 END) AS capital_gain_loss
# FROM stocks
# GROUP BY stock_name;
# -------------------------
# !
# It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day.
# It is also guaranteed that each 'Buy' operation for
#   a stock has a corresponding 'Sell' operation in an upcoming day.
# ! Because we're guaranteed that  there's an order in operation_day it's easy filter.
#   But if there was no order an operations could be like BUY at DAY 5 and sell at DAY 1,
#   then we need to filter these days or order them before using.

# Expected output:
# +---------------+-------------------+
# | stock_name    | capital_gain_loss |
# +---------------+-------------------+
# | Corona Masks  | 9500              |
# | Leetcode      | 8000              |
# | Handbags      | -23000            |
# +---------------+-------------------+
