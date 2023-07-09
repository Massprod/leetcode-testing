
# SQL schema:
# DROP TABLE IF EXISTS users;
# Create table If Not Exists Users (user_id int, name varchar(30), mail varchar(50));
# Truncate table Users;
# insert into Users (user_id, name, mail) values ('1', 'Winston', 'winston@leetcode.com');
# insert into Users (user_id, name, mail) values ('2', 'Jonathan', 'jonathanisgreat');
# insert into Users (user_id, name, mail) values ('3', 'Annabelle', 'bella-@leetcode.com');
# insert into Users (user_id, name, mail) values ('4', 'Sally', 'sally.come@leetcode.com');
# insert into Users (user_id, name, mail) values ('5', 'Marwan', 'quarz#2020@leetcode.com');
# insert into Users (user_id, name, mail) values ('6', 'David', 'david69@gmail.com');
# insert into Users (user_id, name, mail) values ('7', 'Shapiro', '.shapo@leetcode.com');
# --------------------------
# Find the users who have valid emails.
# A valid e-mail has a prefix name and a domain where:
#   1) The prefix name is a string that may contain letters (upper or lower case),
#       digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
#   2) The domain is '@leetcode.com'.
# Return the result table in any order.

# PostgreSQL query:
# SELECT *
# FROM users
# WHERE mail ~* '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'

# MySQL query:
# SELECT *
# FROM users
# WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$';

# In MySQL, we can exclude '.'(any) by double -> \\ and in postgresql is enough to use one -> \.
# Only ~* -> case insensitive == REGEXP, syntax is different. ~ and REGEXP BINARY for sensitive.
