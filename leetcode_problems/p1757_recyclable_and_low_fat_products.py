
# SQL schema:
# DROP TYPE IF EXISTS low_fats_enum;
# CREATE TYPE low_fats_enum AS ENUM('Y', 'N');
# DROP TABLE IF EXISTS products;
# Create table If Not Exists Products (product_id int, low_fats low_fats_enum, recyclable low_fats_enum);
# Truncate table Products;
# insert into Products (product_id, low_fats, recyclable) values ('0', 'Y', 'N');
# insert into Products (product_id, low_fats, recyclable) values ('1', 'Y', 'Y');
# insert into Products (product_id, low_fats, recyclable) values ('2', 'N', 'Y');
# insert into Products (product_id, low_fats, recyclable) values ('3', 'Y', 'Y');
# insert into Products (product_id, low_fats, recyclable) values ('4', 'N', 'N');
# ---------------------
# Find the ids of products that are both low fat and recyclable.
# Return the result table in any order.

# SQL query:
# SELECT product_id
# FROM products
# WHERE
# low_fats = 'Y'
# AND
# recyclable = 'Y';
