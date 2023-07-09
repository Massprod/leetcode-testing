
# SQL schema:
# DROP TABLE IF EXISTS dailysales;
# Create table If Not Exists DailySales(date_id date, make_name varchar(20), lead_id int, partner_id int);
# Truncate table DailySales;
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'toyota', '0', '1');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'toyota', '1', '0');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'toyota', '1', '2');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'toyota', '0', '2');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'toyota', '0', '1');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'honda', '1', '2');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'honda', '2', '1');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'honda', '0', '1');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'honda', '1', '2');
# insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'honda', '2', '1');
# --------------------
# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
# Return the result table in any order.

# SQL query:
# SELECT
# e1.date_id,
# e1.make_name,
# COUNT(DISTINCT e1.lead_id) AS unique_leads,
# COUNT(DISTINCT e1.partner_id) AS unique_partners
# FROM dailysales AS e1
# GROUP BY e1.date_id, e1.make_name;

# Expected output:
# +-----------+-----------+--------------+-----------------+
# | date_id   | make_name | unique_leads | unique_partners |
# +-----------+-----------+--------------+-----------------+
# | 2020-12-8 | toyota    | 2            | 3               |
# | 2020-12-7 | toyota    | 1            | 2               |
# | 2020-12-8 | honda     | 2            | 2               |
# | 2020-12-7 | honda     | 3            | 2               |
# +-----------+-----------+--------------+-----------------+
