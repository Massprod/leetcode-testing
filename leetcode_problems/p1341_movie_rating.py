
# SQL schema:
# DROP TABLE IF EXISTS movies, users, movieratings;
# Create table If Not Exists Movies (movie_id int, title varchar(30));
# Create table If Not Exists Users (user_id int, name varchar(30));
# Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date);
# Truncate table Movies;
# insert into Movies (movie_id, title) values ('1', 'Avengers');
# insert into Movies (movie_id, title) values ('2', 'Frozen 2');
# insert into Movies (movie_id, title) values ('3', 'Joker');
# Truncate table Users;
# insert into Users (user_id, name) values ('1', 'Daniel');
# insert into Users (user_id, name) values ('2', 'Monica');
# insert into Users (user_id, name) values ('3', 'Maria');
# insert into Users (user_id, name) values ('4', 'James');
# Truncate table MovieRating;
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22');
# insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25');
# ----------------------------
# Find the name of the user who has rated the greatest number of movies.
#   In case of a tie, return the lexicographically smaller user name.
# Find the movie name with the highest average rating in February 2020.
#   In case of a tie, return the lexicographically smaller movie name.


# SQL query:
# (SELECT name AS results
# FROM(
#   -- all who voted and their vote count() --
# 	SELECT(
#         SELECT e4.name
# 		  FROM users AS e4
# 		  WHERE e3.user_id = e4.user_id
# 		  ) AS name,
# 	COUNT(user_id) AS count2
# 	FROM movierating AS e3
# 	GROUP BY e3.user_id) AS  count_for_all_2
# -- filtering all voters to leave only voters with max count() --
# WHERE count_for_all_2.count2 = (
#   -- max count() from all voters --
# 	SELECT MAX(count1)
#  	FROM(
# 		SELECT(
# 			  SELECT e2.name
# 			  FROM users AS e2
# 			  WHERE e1.user_id = e2.user_id
# 			  ) AS name,
# 		COUNT(user_id) AS count1
# 		FROM movierating AS e1
# 		GROUP BY e1.user_id
# 		) AS count_for_all
# )
# -- order them in lexicographic --
# ORDER BY results
# LIMIT 1)
# -- combining both results, including duplicates --
# -- because users can have a unique name, and it's name can be equal to a movie_title --
# UNION ALL
# (SELECT title AS results
# FROM (
#   -- all movies and their avg() rating in february --
# 	SELECT e22.title, AVG(e11.rating) AS average_feb
# 	FROM movierating AS e11
# 	JOIN movies AS e22 ON e11.movie_id = e22.movie_id
# 	WHERE
# 	EXTRACT(year FROM e11.created_at) = 2020
# 	AND
# 	extract(month FROM e11.created_at) = 2
# 	GROUP BY e22.title) AS average_rates_feb2
# -- filtering all movies to leave only with max rating --
# WHERE average_rates_feb2.average_feb = (
#   -- max rating of rated movies in february --
# 	SELECT MAX(average_feb) AS max_rate
# 	FROM(
# 		SELECT e22.title, AVG(e11.rating) AS average_feb
# 		FROM movierating AS e11
# 		JOIN movies AS e22 ON e11.movie_id = e22.movie_id
# 		WHERE
# 		EXTRACT(year FROM e11.created_at) = 2020
# 		AND
# 		extract(month FROM e11.created_at) = 2
# 	GROUP BY e22.title ) AS average_rates_feb1)
# -- order them in lexicographic --
# ORDER BY results
# LIMIT 1);

# Failed first commit, only because rushed and didn't think about cases.
# And actually get to think about case when User can name itself as some film, only after pressed_commit,
#   and if they collide we need to use UNION ALL.
# Sure there's some better way to filter all of that,
#   but I don't want to google if I made it correct and with 80+% result.
