from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from tasks_database.db import get_session


# Table: Tree
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | p_id        | int  |
# +-------------+------+
# id is the primary key column for this table.
# Each row of this table contains information about the id of
#   a node and the id of its parent node in a tree.
# The given structure is always a valid tree.
# ------------------------
# Each node in the tree can be one of three types:
#   "Leaf": if the node is a leaf node.
#   "Root": if the node is the root of the tree.
#   "Inner": If the node is neither a leaf node nor a root node.
# Write an SQL query to report the type of each node in the tree.
# Return the result table in any order.


# SQL schema:
# DROP TABLE IF EXISTS tree;
# Create table Tree (id int, p_id int);
# insert into Tree (id, p_id) values ('1', Null);
# insert into Tree (id, p_id) values ('2', '1');
# insert into Tree (id, p_id) values ('3', '1');
# insert into Tree (id, p_id) values ('4', '2');
# insert into Tree (id, p_id) values ('5', '2');

db: Session = next(get_session())
db.execute(
    text(
        "DROP TABLE IF EXISTS tree;"
        "CREATE TABLE tree("
        "   id INTEGER,"
        "   p_id INTEGER"
        ");"
        "INSERT INTO tree(id, p_id) "
        "VALUES "
        "(1, Null),"
        "(2, 1),"
        "(3, 1),"
        "(4, 2),"
        "(5, 2);"
    )
)
db.commit()

# SQL query:
# SELECT e1.id,
# 	CASE
# 		WHEN e1.p_id IS NULL THEN 'Root'
# 		WHEN e1.p_id IN (
# 				SELECT id
# 				FROM tree
# 			 )
# 			 AND e1.id IN(
# 				SELECT p_id
# 				FROM tree
# 		) THEN 'Inner'
# 		ELSE 'Leaf'
# 		END AS type
# FROM tree as e1;

# Encountered only 1 problem when I was filtering Leafs:
# I was trying to filter them by checking their presence IN (SELECT id FROM TREE) AND NOT IN (SELECT p_id FROM TREE)
# Still don't know why it's conflicting, but it's always returning NULL instead of Leaf.
# Only info on that I found, that if there's Null row in any of these checks than Postgres
#  returning uncertain result a.k.a Null. Tried to fix that, but only working way is that just ignore these conditions
#  and use it as ELSE option.

data: Result = db.execute(
    text(
        "SELECT e1.id, "
        "   CASE "
        "       WHEN e1.p_id IS NULL THEN 'Root' "
        "       WHEN e1.p_id IN ("
        "               SELECT id "
        "               FROM tree "
        "           )"
        "           AND e1.id IN ("
        "               SELECT p_id "
        "               FROM tree"
        "           ) THEN 'Inner' "
        "       ELSE 'Leaf' "
        "       END AS type "
        "FROM tree AS e1;"
    )
)

for _ in data:
    print(_)

# Expected output:
# +----+-------+
# | id | type  |
# +----+-------+
# | 1  | Root  |
# | 2  | Inner |
# | 3  | Leaf  |
# | 4  | Leaf  |
# | 5  | Leaf  |
# +----+-------+
